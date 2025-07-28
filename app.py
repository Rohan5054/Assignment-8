from rag_pipeline import get_context
from llm_utils import call_llm

print("Loan Chatbot (type 'exit' to quit)")
while True:
    user_q = input("\nYou: ")
    if user_q.lower() == "exit":
        break
    context = get_context(user_q)
    answer = call_llm(user_q, context)
    print("Bot:", answer)
