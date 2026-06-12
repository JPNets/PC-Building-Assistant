import streamlit as st
from ui.sidebar import render_sidebar
from ui.theme import apply_theme
from ui.three_viewer import render_3d_build
from services.optimizer import optimize_builds
from services.ai_explainer import explain_build
from ui.build_cards import render_build_card
from ui.charts import budget_pie, performance_bar
from ui.pc_visualizer import render_pc_visual
from utils.file_io import save_build
import json

st.set_page_config(page_title='AI PC Builder', layout='wide', initial_sidebar_state='expanded')

st.header('AI-powered PC Builder Assistant')

ui = render_sidebar()
apply_theme()

page = st.selectbox('Page', ['Home','Build Generator','Compatibility Checker','Compare Builds','Saved Builds','Settings'])

if page == 'Home':
    st.subheader('Welcome')
    st.write('Use the sidebar to configure requirements and generate builds.')

if page == 'Build Generator':
    st.subheader('Generate Builds')
    if st.button('Generate Builds'):
        with st.spinner('Generating candidate builds...'):
            builds = optimize_builds(ui.dict())
        if not builds:
            st.error('No compatible builds found for given budget/filters.')
        else:
            for group in builds:
                st.markdown(f"### {group['type']}")
                for idx, b in enumerate(group['items']):
                    # create stable keys for Streamlit elements to avoid duplicates
                    safe_type = group['type'].replace(' ', '_')
                    col1, col2 = st.columns([2,1])
                    with col1:
                        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                        render_build_card(b, idx)
                        st.markdown('</div>', unsafe_allow_html=True)
                        st.markdown('**3D Visualization**')
                        comp_keys = list(b['components'].keys())
                        sel_key = f"highlight_{safe_type}_{idx}"
                        highlight = st.selectbox(f"Highlight component ({group['type']} #{idx+1})", ['None'] + comp_keys, key=sel_key)
                        render_3d_build(b, highlight=None if highlight == 'None' else highlight)
                    with col2:
                        st.plotly_chart(budget_pie(b), use_container_width=True, key=f"budget_{safe_type}_{idx}")
                        st.plotly_chart(performance_bar(b), use_container_width=True, key=f"perf_{safe_type}_{idx}")
                        explain_key = f"explain_{safe_type}_{idx}"
                        save_key = f"save_{safe_type}_{idx}"
                        if st.button(f"Explain build {group['type']} #{idx+1}", key=explain_key):
                            explanation = explain_build({
                                'name': f"{group['type']} #{idx+1}",
                                'components': {k: v for k,v in b['components'].items()},
                                'scores': b.get('scores', {})
                            })
                            st.info(explanation)
                        if st.button(f"Save build {group['type']} #{idx+1}", key=save_key):
                            path = save_build({
                                'type': group['type'],
                                'build': b
                            }, f"{group['type'].replace(' ','_')}_{idx+1}.json")
                            st.success(f"Saved to {path}")

if page == 'Compatibility Checker':
    st.subheader('Compatibility Checker')
    st.write('Select components from the database in code or load a saved build to check compatibility.')
    uploaded = st.file_uploader('Upload saved build JSON', type=['json'])
    if uploaded:
        data = json.load(uploaded)
        build = data.get('build') if isinstance(data, dict) else data
        st.write('Checking compatibility...')
        from services.compatibility import check_compatibility
        compat = check_compatibility(build.get('components', build))
        st.json(compat)

if page == 'Compare Builds':
    st.subheader('Compare Builds')
    st.write('Load two saved builds to compare.')
    b1 = st.file_uploader('Build A', type=['json'], key='a')
    b2 = st.file_uploader('Build B', type=['json'], key='b')
    if b1 and b2:
        data1 = json.load(b1)
        data2 = json.load(b2)
        st.write('Build A')
        render_build_card(data1.get('build') or data1, 0)
        st.write('Build B')
        render_build_card(data2.get('build') or data2, 0)

if page == 'Saved Builds':
    st.subheader('Saved Builds')
    import os
    saved = 'saved_builds'
    if not os.path.exists(saved):
        st.write('No saved builds yet.')
    else:
        files = [f for f in os.listdir(saved) if f.endswith('.json')]
        sel = st.selectbox('Select saved build', files if files else [])
        if sel:
            with open(os.path.join(saved, sel),'r',encoding='utf-8') as f:
                data = json.load(f)
            render_build_card(data.get('build') or data, 0)
            if st.button('Export JSON'):
                st.download_button('Download JSON', json.dumps(data, indent=2), file_name=sel)

if page == 'Settings':
    st.subheader('Settings')
    st.write('Manage API keys and preferences in `.env`.')
