from fastapi import FastAPI, Request, HTTPException
import requests
import os
from dotenv import load_dotenv

#load environment variables
load_dotenv()
app = FastAPI()
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

@app.get("/")
def health_check():
    return {"status": "running"}

@app.post("/webhook/bolna")
async def bolna_webhook(request: Request):
    try:
        #handle empty or invalid JSON safely
        try:
            data = await request.json()
        except Exception:
            data = {}
        print("Incoming data:", data)

        #check webhook
        if not SLACK_WEBHOOK_URL:
            raise Exception("SLACK_WEBHOOK_URL missing in .env")
        print("Using webhook:", SLACK_WEBHOOK_URL)

        #safe extraction
        call_id = data.get("id", "N/A")
        agent_id = data.get("agent_id", "N/A")
        duration = data.get("duration", "N/A")
        transcript = data.get("transcript", "N/A")

        #slack message
        message = {
            "text": f"""
 *Call Ended Alert*
• ID: {call_id}
• Agent: {agent_id}
• Duration: {duration}
• Transcript: {transcript}
"""
        }
        #send request to Slack
        response = requests.post(SLACK_WEBHOOK_URL, json=message)
        print("Slack response:", response.status_code, response.text)
        if response.status_code != 200:
            raise Exception(f"Slack API error: {response.text}")
        return {"status": "success"}

    except Exception as e:
        print("Error:", str(e))
        raise HTTPException(status_code=500, detail=str(e))