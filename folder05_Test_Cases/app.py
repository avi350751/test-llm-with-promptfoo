import streamlit as st
from helper import analyze_json
import json


st.set_page_config(page_title="JSON Explorer and QA", page_icon="🧠", layout="wide")
st.title("JSON Explorer and QA")
st.markdown("--------------------------")
st.write("Upload a JSON file and ask LLM for insights")

# Initialize state to persist the loaded JSON across reruns
if "json_data" not in st.session_state:
    st.session_state.json_data = None
if "insights" not in st.session_state:
    st.session_state.insights = None


with st.sidebar:
    st.header("Upload JSON")
    uploaded_file = st.file_uploader("Upload your json file", type=["json", "txt"])
    st.markdown("-----------------------------")
    submit_btn = st.button("Submit for processing")

if submit_btn:
    if not uploaded_file:
        st.warning("Upload a JSON file first")
    else:
        try:
            st.session_state.json_data = json.load(uploaded_file)
            st.session_state.insights = None
            st.success("File Uploaded. ready to analyze...")
        except Exception as e:
            st.error(f"Error reading JSON: {e}")

# Show JSON preview if present
if st.session_state.json_data is not None:
    st.subheader("JSON Preview")
    st.json(st.session_state.json_data, expanded=False)


    if st.button("🔍 Generate Insights"):
        with st.spinner("Analyzing JSON...."):
            st.session_state.insights = analyze_json(st.session_state.json_data)
            st.subheader("🧠 Insights from LLM:")
    # Show insights if available
    if st.session_state.insights:
        #st.subheader("🧠 Insights")
        st.write(st.session_state.insights)
else:
    st.info("Upload a JSON file in the sidebar and click **Submit for processing**.")



    