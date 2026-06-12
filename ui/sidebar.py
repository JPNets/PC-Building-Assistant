import streamlit as st
from models.user_input import UserInput


def render_sidebar():
    st.sidebar.title('PC Builder')
    budget = st.sidebar.number_input('Budget (USD)', min_value=200, value=1200)
    country = st.sidebar.selectbox('Country', ['US', 'UK', 'DE', 'FR', 'IN'], index=0)
    use_case = st.sidebar.selectbox('Main Use Case', ['Gaming', 'Programming', 'AI/ML', 'Content Creation', 'Streaming', 'Office'], index=0)
    resolution = st.sidebar.selectbox('Resolution', ['1080p', '1440p', '4K'], index=0)
    target_fps = st.sidebar.slider('Target FPS', min_value=30, max_value=240, value=60)
    preferred_cpu = st.sidebar.text_input('Preferred CPU model (optional)')
    preferred_gpu = st.sidebar.text_input('Preferred GPU model (optional)')
    form_factor = st.sidebar.selectbox('Form factor', ['ATX', 'Micro-ATX', 'Mini-ITX'], index=0)
    ram = st.sidebar.selectbox('RAM (GB)', [8,16,32,64], index=1)
    storage = st.sidebar.selectbox('Storage (GB)', [256,512,1000,2000], index=2)
    rgb = st.sidebar.checkbox('RGB preferred')
    noise = st.sidebar.checkbox('Noise sensitive')
    upgrade_priority = st.sidebar.slider('Upgradeability priority', 1, 5, 3)
    efficiency_priority = st.sidebar.slider('Power efficiency priority', 1, 5, 3)

    ui = UserInput(
        budget=budget,
        country=country,
        use_case=use_case.lower(),
        resolution=resolution,
        target_fps=target_fps,
        preferred_cpu=preferred_cpu or None,
        preferred_gpu=preferred_gpu or None,
        form_factor=form_factor,
        ram_gb=ram,
        storage_gb=storage,
        rgb=rgb,
        noise_sensitive=noise,
        upgrade_priority=upgrade_priority,
        power_efficiency_priority=efficiency_priority
    )
    return ui
