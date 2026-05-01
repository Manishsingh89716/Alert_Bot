# Bolna → Slack Integration

## 🚀 Overview
This project integrates a call system (Bolna) with Slack using a webhook-based architecture.

When a call ends, the system receives call data and sends a formatted alert message to a Slack channel.

---

## 🧠 Architecture

Bolna → Webhook → FastAPI → Slack

---

## ⚙️ Tech Stack
- Python (FastAPI)
- Slack Webhooks
- Requests
- ngrok (for local testing)

---

## 📦 Setup Instructions

### 1. Clone the repo
git clone <your-repo-url>
cd <repo-folder>

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Setup environment variables
Create a `.env` file:

SLACK_WEBHOOK_URL=your_slack_webhook_url

---

## ▶️ Run the server

uvicorn main:app --reload

Server runs on:
http://127.0.0.1:8000

---

## 🧪 Test API

POST /webhook/bolna

Sample payload:
```json
{
"id": "CALL_101",
"agent_id": "AGENT_X",
"duration": "180",
"transcript": "Test call"
}
```

---

## 📩 Sample Slack Output

📞 Call Ended Alert  
• ID: CALL_101  
• Agent: AGENT_X  
• Duration: 180 sec  
• Transcript: Test call

---

## ⚠️ Notes

- Webhook endpoint is ready to receive call events from Bolna
- Manual testing done using curl / Postman
- Environment variables are secured using `.env`

---