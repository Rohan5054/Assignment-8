import pandas as pd
import json

df = pd.read_csv("data/Training_Dataset.csv")
df = df.dropna(subset=["Credit_History", "Loan_Status"])[:100]  # limit for demo

qa_pairs = []

for _, row in df.iterrows():
    question = f"Can someone with a credit history of {int(row['Credit_History'])} and an income of ₹{int(row['Applicant_Income'])} get a loan?"
    context = f"Gender: {row['Gender']}, Married: {row['Married']}, Education: {row['Education']}, Credit_History: {int(row['Credit_History'])}, ApplicantIncome: ₹{int(row['Applicant_Income'])}, Loan_Status: {row['Loan_Status']}"
    answer = "Yes" if row["Loan_Status"] == "Y" else "No"
    qa_pairs.append({"question": question, "context": context, "response": f"{answer}. {context}"})

with open("qa_data.json", "w") as f:
    json.dump(qa_pairs, f, indent=2)
