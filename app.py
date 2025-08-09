import streamlit as st
import pathlib

st.set_page_config(page_title="Vangelico Practice", page_icon="🎮", layout="centered")

st.title("Vangelico Block Hack — Practice")
st.caption("Click groups of 2+ same color (no diagonals). After clears: gravity down, then columns shift left.")

html_path = pathlib.Path("vangelico_practice.html")
if not html_path.exists():
    st.error("`vangelico_practice.html` not found in the repo root. Please add it.")
    st.stop()

html_file = html_path.read_text(encoding="utf-8")

# Give the iframe more height and allow scrolling just in case
st.components.v1.html(html_file, height=1000, scrolling=True)
