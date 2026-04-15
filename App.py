import streamlit as st
from transformers import pipeline
@st.cache_resource
def load_summerizer():
  return pipeline("summarization",model="sshleifer/distilbart-cnn-12-6")
  st.title("AI Text Summarizer")
st.write("Enter a long text below, and get a concise Summary!")
long_text = st.text_area("Enter text to Summarizer:", height = 200)
max_length = st.slider("Max Summary Length", min_value=50,
                       max_value=300, value=130)
min_length = st.slider("Min Summary Length" , min_value=20,
                       max_value=100, value=30)
if st.button("Summarize"):
  if long_tex.strip():
    with st.spinner("Generating summary..."):
      summary = summarizer(long_text,max_length,min_length=min_length, do_sample=False)
      st.subheader("Summary!")
      st.success(summary[0]8
  else
  st.warning("⚠️ Please enter some text to summarize.")
