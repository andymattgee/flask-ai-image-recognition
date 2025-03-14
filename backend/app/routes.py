from flask import Blueprint, request, jsonify, current_app
import os
import base64
from openai import OpenAI
import tempfile
import logging

main_bp = Blueprint('main', __name__)

@main_bp.route('/api/test', methods=['GET'])
def test_route():
    return jsonify({'status': 'success', 'message': 'API is working correctly'})

@main_bp.route('/api/analyze-image', methods=['POST', 'OPTIONS'])
def analyze_image():
    # Handle preflight OPTIONS request
    if request.method == 'OPTIONS':
        return '', 204
        
    try:
        # Log request information for debugging
        current_app.logger.info(f"Received request: {request.method} {request.path}")
        current_app.logger.info(f"Request headers: {dict(request.headers)}")
        current_app.logger.info(f"Request files: {request.files}")
        
        # Check if the post request has the file part
        if 'image' not in request.files:
            current_app.logger.error("No image part in the request")
            return jsonify({'error': 'No image part in the request'}), 400
        
        file = request.files['image']
        
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            current_app.logger.error("No selected file")
            return jsonify({'error': 'No selected file'}), 400
        
        # Save the file temporarily
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        file.save(temp_file.name)
        temp_file.close()
        
        # Initialize OpenAI client
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            current_app.logger.error("OpenAI API key not found in environment variables")
            print("ERROR: OpenAI API key not found in environment variables")
            print(f"Environment variables: {os.environ.keys()}")
            return jsonify({'error': 'OpenAI API key not configured'}), 500
            
        current_app.logger.info(f"Using OpenAI API key: {api_key[:5]}...")
        # Initialize OpenAI client with only the required parameters
        client = OpenAI(
            api_key=api_key
        )
        
        # Open the image file and encode it to base64
        with open(temp_file.name, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        
        # Delete the temporary file
        os.unlink(temp_file.name)
        
        # Call OpenAI API with the image
        current_app.logger.info("Calling OpenAI API")
        
        # Determine the image format (default to jpeg if unknown)
        image_format = "jpeg"
        if file.filename:
            ext = file.filename.split('.')[-1].lower()
            if ext in ['png', 'jpg', 'jpeg', 'gif', 'webp']:
                image_format = ext
        
        response = client.chat.completions.create(
            model="gpt-4-turbo",  # This is the correct model name for GPT-4 with vision
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What is in this picture?"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/{image_format};base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=300
        )
        
        # Extract the response text
        result = response.choices[0].message.content
        current_app.logger.info(f"OpenAI response received: {result[:50]}...")
        
        return jsonify({'result': result})
    
    except Exception as e:
        current_app.logger.error(f"Error processing request: {str(e)}", exc_info=True)
        return jsonify({'error': str(e)}), 500 