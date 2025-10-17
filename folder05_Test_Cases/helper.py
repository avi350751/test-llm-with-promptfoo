import json
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini",api_key=os.getenv("OPENAI_API_KEY"), temperature=0.3)

def analyze_json(json_data):

    preview = json.dumps(json_data)

    prompt = f"""
    You are a data analyst AI. Analyze the following JSON data and provide structured insights.
    Required sections:
    - Key patterns
    - Outliers or anomalies
    - Summary statistics if numerical
    - Relationships between fields
    - Any notable findings or recommendations

    Respond as Markdown with clear bullet points and short paragraphs.

    JSON data: {preview}"""

    messages = [
        SystemMessage(content="You are an expert data analyst specializing in structured JSON insights."),
        HumanMessage(content=prompt),
    ]
    response = llm.invoke(messages)
    return response.content
    