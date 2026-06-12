import streamlit as st


def apply_theme():
        css = """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
        :root{
            --bg-1: #071029; --bg-2:#0f1724; --accent:#00e6a8; --accent2:#7c3aed; --glass: rgba(255,255,255,0.04);
        }
        html, body, [class*='css'] > .block-container{
            background: radial-gradient(1200px 600px at 10% 10%, rgba(124,58,237,0.12), transparent 8%),
                                    radial-gradient(1000px 500px at 90% 90%, rgba(0,230,168,0.08), transparent 8%),
                                    linear-gradient(180deg, var(--bg-1), var(--bg-2));
            color: #e6eef8; font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
        }
        /* Glass card with subtle blur and neon edge */
        .glass-card{
            background: linear-gradient(135deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
            border-radius:14px; padding:18px; box-shadow: 0 8px 30px rgba(2,6,23,0.7);
            border: 1px solid rgba(124,58,237,0.12); backdrop-filter: blur(6px);
        }
        .glass-card:hover{ transform: translateY(-8px); transition: all 0.18s ease; box-shadow: 0 14px 40px rgba(2,6,23,0.85) }
        /* Buttons and inputs */
        .stButton>button, .stSelectbox>div>div, .stTextInput>div>input {
            border-radius:10px; background: linear-gradient(90deg, rgba(124,58,237,0.2), rgba(0,230,168,0.06));
            border: 1px solid rgba(255,255,255,0.04);
        }
        /* Hero header */
        .stApp header { display: none }
        .app-hero{ padding:28px; border-radius:14px; margin-bottom:16px; background: linear-gradient(90deg, rgba(124,58,237,0.12), rgba(0,230,168,0.06)); border:1px solid rgba(124,58,237,0.12) }
        .app-title{ font-weight:800; font-size:28px; margin:0; color: #f8fafc }
        .app-sub{ color:#c7d2fe; margin:4px 0 0 0 }
        /* small neon accent for score badges */
        .score-badge{ display:inline-block; padding:6px 10px; border-radius:999px; font-weight:600; color:#071029; background: linear-gradient(90deg,var(--accent),var(--accent2)); }
        /* small utilities */
        .muted{ color:#9aa4b2 }
        </style>
        """
    st.markdown(css, unsafe_allow_html=True)
