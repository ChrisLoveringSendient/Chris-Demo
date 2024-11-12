# Sprint review demo from 12/11/2024

import streamlit as st
import httpx

st.title("👨‍👩‍👧‍👦 Teams import")

api_key = st.text_input("SmartEducator API Key", type="password")
if not api_key:
    st.info("Please add your SmartEducator API key to continue.", icon="🗝️")
else:
    pressed = st.button("Import from teams", type="primary")
    if pressed:
        a = st.text("Importing...")
        httpx.post(
            "http://localhost:7071/api/experimental/ms-teams/import-all",
            headers={"Authorization": f"Bearer {api_key}"},
        )
        a.text("Imported successfully!")
