import streamlit as st


def apply_theme():
    css = """
    <style>
    /* Dark background */
    .reportview-container, .main .block-container{background-color:#0f1720; color:#e6eef8}
    /* Glass cards */
    .glass-card{background:rgba(255,255,255,0.03); border-radius:12px; padding:16px; box-shadow:0 8px 20px rgba(2,6,23,0.6); border:1px solid rgba(255,255,255,0.03);}
    /* Rounded selectbox and buttons */
    .stButton>button, .stSelectbox>div>div{border-radius:10px}
    /* Headings */
    h1, h2, h3 { font-family: 'Inter', sans-serif; color:#f1f5f9 }
    /* Hover effect for cards */
    .glass-card:hover{transform:translateY(-6px); transition:all 0.18s ease}
    /* Streamlit markdown containers tweak */
    .stMarkdown{color:#cbd5e1}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
