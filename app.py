from pathlib import Path
import json

import streamlit as st
import streamlit.components.v1 as components

from src.storyboard import generate_storyboard
from src.html_generator import generate_interactive_html


st.set_page_config(page_title="AI Course Builder", page_icon="🧠", layout="wide")

SAMPLE_PATH = Path("data/sample_source.md")
sample_text = SAMPLE_PATH.read_text(encoding="utf-8") if SAMPLE_PATH.exists() else ""

st.title("AI Course Builder")
st.caption("Portfolio MVP: source material → structured storyboard → interactive HTML learning experience")

with st.sidebar:
    st.header("Project goals")
    st.write(
        "Demonstrate an AI-enabled instructional-design workflow with human review, "
        "structured outputs, and interactive learning generation."
    )
    st.info("This MVP uses deterministic mock generation and does not require an API key.")

audience = st.text_input("Target audience", value="Adult learners")
source_text = st.text_area(
    "Source material",
    value=sample_text,
    height=260,
    help="Paste raw content that an instructional designer would normally review and structure.",
)

if st.button("Generate storyboard", type="primary"):
    st.session_state.storyboard = generate_storyboard(source_text, audience).to_dict()

storyboard = st.session_state.get("storyboard")

if storyboard:
    left, right = st.columns([1, 1])

    with left:
        st.subheader("1. Structured storyboard")
        st.markdown(f"### {storyboard['course_title']}")
        st.write(f"**Audience:** {storyboard['audience']}")

        st.write("**Learning objectives**")
        for objective in storyboard["learning_objectives"]:
            st.write(f"- {objective}")

        for idx, section in enumerate(storyboard["sections"], start=1):
            with st.expander(f"{idx}. {section['title']}", expanded=True):
                st.write(section["purpose"])
                st.write("**Key points**")
                for point in section["key_points"]:
                    st.write(f"- {point}")
                st.write(f"**Interaction:** {section['interaction']}")

        st.download_button(
            "Download storyboard JSON",
            data=json.dumps(storyboard, indent=2),
            file_name="storyboard.json",
            mime="application/json",
        )

    with right:
        st.subheader("2. Interactive learning preview")
        html_output = generate_interactive_html(storyboard)
        components.html(html_output, height=720, scrolling=True)

        st.download_button(
            "Download interactive HTML",
            data=html_output,
            file_name="learning_interaction.html",
            mime="text/html",
        )
else:
    st.write("Use the sample source or paste your own content, then click **Generate storyboard**.")
