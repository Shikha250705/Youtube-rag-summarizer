# Youtube-rag-summarizer
# 🎬 YouTube Video Q&A with Timestamps

An AI-powered RAG (Retrieval-Augmented Generation) system that lets you 
ask questions about any YouTube video and get answers with exact timestamps.

## 🚀 Features
- Paste any YouTube video URL
- Ask questions in natural language
- Get relevant answers with exact timestamps
- Powered by FAISS vector search + HuggingFace embeddings

## 🛠️ Tech Stack
- Python, Streamlit
- LangChain, FAISS
- HuggingFace Sentence Transformers
- YouTube Transcript API

## ▶️ How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the app:
streamlit run app.py

3. Paste any YouTube URL and ask questions!

## 📸 Demo
Ask: "What is a neuron?"
Result: Relevant video segments with timestamps like 02:48, 02:52
