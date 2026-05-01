import streamlit as st
from src.agents import analyze_meeting
from src.rag import load_knowledge, build_index, retrieve

st.title("🧠 AI Meeting Intelligence System")

query = st.text_input("Ask about meeting insights")

if st.button("Analyze Meeting"):
    
    summary, actions, decisions = analyze_meeting()
    
    st.subheader("📄 Summary")
    st.write(summary)
    
    st.subheader("📌 Action Items")
    for a in actions:
        st.write(a)
    
    st.subheader("🎯 Decisions")
    for d in decisions:
        st.write(d)
    
    # RAG
    docs = load_knowledge()
    index = build_index(docs)
    
    if query:
        insights = retrieve(query, docs, index)
        
        st.subheader("🔎 Insights")
        for i in insights:
            st.write(i)