import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_health_remark(
        glucose,
        haemoglobin,
        cholesterol):

    prompt = f"""
You are a health screening assistant.

Glucose: {glucose}
Haemoglobin: {haemoglobin}
Cholesterol: {cholesterol}

Return ONLY ONE SHORT HEALTH REMARK.

Examples:

Normal

High Diabetes Risk

Elevated Cholesterol

Possible Anaemia

Multiple Risk Factors Detected

Maximum 4 words.

No explanation.
No bullet points.
No recommendations.
"""

    response = model.generate_content(
        prompt
    )

    return response.text