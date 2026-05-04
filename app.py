import streamlit as st
from rag_pipeline import get_video_id, fetch_transcript, \
                         build_vectorstore, answer_question

st.title("🎬 YouTube Video Q&A with Timestamps")
st.write("Koi bhi YouTube video ka URL daalo aur questions pucho!")

url = st.text_input("YouTube URL daalo:")

if url:
    with st.spinner("Transcript fetch ho raha hai..."):
        video_id = get_video_id(url)
        chunks = fetch_transcript(video_id)
        vectorstore = build_vectorstore(chunks)
        st.success(f"✅ Video ready! {len(chunks)} segments processed.")

    question = st.text_input("Apna question pucho:")

    if question:
        results = answer_question(vectorstore, question)
        st.subheader("📍 Relevant Moments:")
        for r in results:
            st.markdown(f"**⏱ Timestamp: {r['timestamp']}**")
            st.write(r['text'])
            st.divider()