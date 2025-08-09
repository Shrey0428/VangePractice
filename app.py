import streamlit as st
import pathlib

st.set_page_config(page_title="Vangelico Practice", page_icon="🎮", layout="centered")

st.title("Vangelico Block Hack — Practice")
st.caption("Click groups of 2+ same color (no diagonals). After clears: gravity down, then columns shift left.")

html_path = pathlib.Path("vangelico_practice.html")

if html_path.exists():
    html_file = html_path.read_text(encoding="utf-8")
else:
    # Fallback: if the HTML file isn't found, show a helpful message
    st.error("`vangelico_practice.html` not found in the repo root. Please add it.")
    st.stop()

# Render the game
st.components.v1.html(html_file, height=820, scrolling=False)

with st.expander("Tips & Shortcuts"):
    st.markdown(
        """
        - **Undo** reverts the last clear.
        - **Timer mode** uses a stopwatch; add a hard countdown later if you want.
        - Board: **11×8**, **3 colors**, only orthogonal matches.
        """
    )
