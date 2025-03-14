# Image Analysis App

A full-stack application that allows users to upload images and get AI-powered analysis using OpenAI's GPT-4 Turbo with vision capabilities.

## Project Structure

- `frontend/`: Next.js application with TypeScript and Tailwind CSS
- `backend/`: Flask API server that communicates with OpenAI

## Setup Instructions

### Prerequisites

- Node.js 18+
- Python 3.8+
- OpenAI API key

### Environment Setup

1. Clone this repository
2. Create a `.env` file in the `backend/` directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   FLASK_ENV=development
   ```

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Start the Flask server:
   ```
   python run.py
   ```
   The backend will run on http://localhost:5001

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm run dev
   ```
   The frontend will run on http://localhost:3000

## Usage

1. Open your browser and go to http://localhost:3000
2. Click the "Test API Connection" button to verify that the backend is running and accessible
3. Upload an image using the drag-and-drop interface or file selector
4. Click "Analyze Image" to send the image to the OpenAI API
5. View the analysis results displayed on the page

## Troubleshooting

### CORS Issues

If you encounter CORS errors in the browser console:

1. Make sure both the frontend and backend are running
2. Verify that the backend is running on port 5001
3. Check that the frontend is making requests to http://localhost:5001
4. Try using the "Test API Connection" button to verify basic connectivity

### OpenAI API Issues

If the image analysis fails:

1. Verify that your OpenAI API key is correctly set in the `.env` file
2. Check that your OpenAI account has access to the GPT-4 Vision API
3. Look at the backend logs for detailed error messages

## Technologies Used

- **Frontend**: Next.js, TypeScript, Tailwind CSS
- **Backend**: Python, Flask
- **AI**: OpenAI GPT-4 Turbo