import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

EXAMPLES = """
Q: Can someone with a credit history of 1 and income of ₹5000 get a loan?
A: Yes. Credit history of 1 and stable income generally leads to loan approval.

Q: Can someone with a credit history of 0 get a loan?
A: No. Most loans are rejected for applicants with credit history 0.
"""

def call_llm(query, context):
    prompt = f"{EXAMPLES}\n\nContext: {context}\nQ: {query}\nA:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"].strip()
