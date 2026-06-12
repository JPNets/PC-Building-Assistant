import streamlit as st
from utils.formatters import currency

def render_component_card(component: dict):
    st.markdown(f"**{component.get('name')}** — {component.get('brand', '')}")
    st.write(f"Price: {currency(component.get('price',0))}")
    specs = [f"{k}: {v}" for k,v in component.items() if k not in ['id','name','brand','price']]
    st.write(', '.join(specs))


def render_build_card(build: dict, idx: int = 0):
    st.subheader(f"Build #{idx+1}")
    st.write(f"Total: {currency(build.get('total_price',0))}")
    cols = st.columns(2)
    with cols[0]:
        for key, comp in build.get('components', {}).items():
            st.markdown(f"**{key.upper()}**")
            render_component_card(comp)
    with cols[1]:
        st.write("**Scores**")
        for k,v in build.get('scores',{}).items():
            st.write(f"{k}: {v}")
        st.write("**Compatibility**")
        for k,v in build.get('compatibility',{}).items():
            st.write(f"{k}: {v}")
