import streamlit as st
import pathlib

st.set_page_config(page_title="Vangelico Practice", layout="wide")

html_file = pathlib.Path("vangelico_practice.html").read_text(encoding="utf-8")

# full width, higher height, scrolling enabled
st.components.v1.html(
    f"<div style='width:100%'>{html_file}</div>",
    height=1000,
    scrolling=True
)
