from youtube_transcript_api import YouTubeTranscriptApi

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]

def fetch_transcript(video_id):
    ytt = YouTubeTranscriptApi()
    transcript = ytt.fetch(video_id)
    chunks = []
    for entry in transcript:
        start= entry.start
        mins=int(start)// 60
        secs = int(start) % 60
        timestamp = f"{mins:02d}:{secs:02d}"
        chunks.append({
            "text": entry.text,
            "timestamp": timestamp,
            "start": entry.start
        })
    return chunks

def build_vectorstore(chunks):
    texts = [c['text'] for c in chunks]
    metadatas = [{"timestamp": c['timestamp']} for c in chunks]
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.from_texts(texts, embeddings, metadatas=metadatas)
    return vectorstore

def answer_question(vectorstore, question):
    docs = vectorstore.similarity_search(question, k=3)
    results = []
    for doc in docs:
        results.append({
            "text": doc.page_content,
            "timestamp": doc.metadata['timestamp']
        })
    return results