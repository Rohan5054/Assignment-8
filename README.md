An intelligent RAG-based chatbot that answers questions related to loan approvals using a real dataset and a fine-tuned lightweight language model. Built with Streamlit for an interactive user interface and uses ChromaDB for fast semantic search.

Features
-RAG (Retrieval-Augmented Generation): Combines document retrieval with generative AI for accurate and grounded answers.

-Semantic Search: Uses embeddings from sentence-transformers to retrieve the most relevant context.

-Fine-tuned QA Model: Trained on custom Q&A pairs derived from a loan approval dataset.

-Interactive UI: Streamlit-based frontend for real-time Q&A with answer highlighting.

-Real Dataset: Uses the Loan Approval Prediction dataset for realistic answers


STEPS FOR SETUP:

1) git clone https://github.com/yourusername/loan-qa-chatbot.git
cd loan-qa-chatbot
Install dependencies


pip install -r requirements.txt



Start the Streamlit app
streamlit run app.py
