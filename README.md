🚀 AI Chatbot (FastAPI + React)

A simple AI chatbot project built using:

FastAPI (Python) — backend API

Google FLAN-T5 model — for AI responses

React — frontend UI

📂 Project Structure
fastapi-service/
    main.py

frontend/
    my-app/
        src/
        public/

▶ Run Backend
cd fastapi-service
pip install fastapi uvicorn transformers
uvicorn main:app --reload


Runs at: http://localhost:8000

▶ Run Frontend
cd frontend/my-app
npm install
npm start


Runs at: http://localhost:3000

🔗 API Endpoint

POST /generate

{
  "message": "Hello"
}


Returns AI-generated reply.
