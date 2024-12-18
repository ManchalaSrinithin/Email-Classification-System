from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import csv
from io import StringIO
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/images", StaticFiles(directory="images"), name="images")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Replace with your actual API key
client = Groq(api_key="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")

VALID_CATEGORIES = {'Resume', 'Application', 'HR', 'Meeting', 'Spam'}

class EmailRequest(BaseModel):
    user_id: str
    subject: str
    body: str

class ClassificationResponse(BaseModel):
    is_spam: bool
    category: str
    original_category: str
    relevance: str

@app.get("/", response_class=HTMLResponse)
async def homepage():
    return HTMLResponse(content=open("index.html").read())

@app.post("/classify", response_model=ClassificationResponse)
async def classify_email(request: EmailRequest):
    try:
        spam_prompt = f"Classify the following email as spam or not spam:\n\n{request.body}"
        category_prompt = (
            "Categorize the following email into one of the categories: Resume, Application, "
            "Meeting, HR, Spam, etc. Respond with only the category name as a single word. "
            "\n\n"
            f"{request.body}"
        )

        relevance_prompt = f"Assess the relevance of the following email and respond with 'High' or 'Low':\n\n{request.body}"

        spam_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a spam filter system."},
                {"role": "user", "content": spam_prompt}
            ],
            model="llama3-8b-8192"
        )
        is_spam = "Spam" in spam_completion.choices[0].message.content.strip()

        category_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a categorization system."},
                {"role": "user", "content": category_prompt}
            ],
            model="llama3-8b-8192"
        )
        original_category = category_completion.choices[0].message.content.strip().split()[0]
        category = original_category if original_category in VALID_CATEGORIES else 'Other'

        relevance_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a relevance assessment system."},
                {"role": "user", "content": relevance_prompt}
            ],
            model="llama3-8b-8192"
        )
        relevance = relevance_completion.choices[0].message.content.strip()

        return ClassificationResponse(
            is_spam=is_spam,
            category=category,
            original_category=original_category,
            relevance=relevance
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="File must be a CSV")

        contents = await file.read()
        decoded = contents.decode("utf-8").splitlines()
        csv_reader = csv.DictReader(decoded)

        results = {category: [] for category in VALID_CATEGORIES}
        results['Other'] = []

        for row in csv_reader:
            email = row.get("email")
            subject = row.get("subject")
            body = row.get("body")

            if email and subject and body:
                classification = await classify_email(EmailRequest(user_id=email, subject=subject, body=body))
                
                category = classification.category
                results[category].append({
                    "sender": email,
                    "subject": subject,
                    "message": body,
                    "category": category,
                    "original_category": classification.original_category,
                    "relevance": classification.relevance
                })
            else:
                raise HTTPException(status_code=400, detail="CSV missing required fields")

        return {"success": True, "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")