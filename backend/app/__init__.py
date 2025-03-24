# init file could also be called app.py or main.py
# This file is the entry point for the Flask application
# This is where you create and configure the app via a factory function (create_app)
# You could initialize database connections, configure extensions, and register blueprints here


from flask import Flask
from flask_cors import CORS
import os
import logging
from dotenv import load_dotenv

# Load environment variables from the .env file
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
load_dotenv(dotenv_path)

# Check if the OpenAI API key is loaded
api_key = os.environ.get("OPENAI_API_KEY")
print(f"API Key found: {'Yes' if api_key else 'No'}")

def create_app():
    """
    Create and configure the Flask application.
    
    Returns:
        app: The Flask application instance.
    """
    app = Flask(__name__)  # Initialize the Flask app
    
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    app.logger.setLevel(logging.INFO)
    
    # Enable CORS for all routes
    CORS(app, 
         resources={r"/*": {"origins": "*"}},  # Allow all origins
         supports_credentials=True,  # Allow credentials
         allow_headers=["Content-Type", "Authorization", "Accept"],  # Allowed headers
         methods=["GET", "POST", "OPTIONS"])  # Allowed methods
    
    # Import and register the main blueprint
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    @app.after_request
    def after_request(response):
        """
        Add CORS headers to the response.
        
        Args:
            response: The response object.
        
        Returns:
            response: The modified response object.
        """
        response.headers.add('Access-Control-Allow-Origin', '*')  # Allow all origins
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Accept')  # Allowed headers
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')  # Allowed methods
        return response
    
    return app  # Return the configured app instance 