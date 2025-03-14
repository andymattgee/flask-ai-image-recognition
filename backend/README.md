# Backend - Flask Image Analysis API

This is the backend for the Image Analysis application. It uses Flask to provide an API endpoint that receives images, sends them to OpenAI's GPT-4 Turbo with vision capabilities, and returns the analysis results.

## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on `.env.example` and add your OpenAI API key.

## Running the Server

```
python run.py
```

The server will start on http://localhost:5001.

## API Endpoints

- `POST /api/analyze-image`: Accepts an image file and returns the analysis from OpenAI.
  - Request: Form data with an 'image' field containing the image file.
  - Response: JSON with a 'result' field containing the analysis text. 