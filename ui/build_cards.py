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
            # clickable component name to focus in 3D view
            comp_key = f"comp_btn_{key}_{idx}"
            if st.button(f"{key.upper()}", key=comp_key):
                st.session_state['highlight_component'] = key
            render_component_card(comp)
    with cols[1]:
            st.markdown("**Scores**")
            scores = build.get('scores', {})
            # reference maxima for scaling bars (heuristic)
            max_ref = {'gaming': 15000, 'productivity': 15000, 'ai_ml': 15000, 'value': 2.0, 'efficiency': 60.0, 'upgradeability': 3.0}

            def score_context(name, val):
                if name == 'gaming':
                    if val > 12000: return ('Blazing — Excellent for high-FPS 1440p/4K', '#ef4444')
                    if val > 8000: return ('Strong — Great for 1440p high settings', '#f97316')
                    return ('Good — Solid 1080p performance', '#60a5fa')
                if name == 'productivity':
                    if val > 12000: return ('Workhorse — Heavy multitasking & compile speeds', '#7c3aed')
                    if val > 8000: return ('Capable — Good for content creation', '#a78bfa')
                    return ('Adequate — Light productivity workloads', '#60a5fa')
                if name == 'ai_ml':
                    if val > 12000: return ('GPU-bound AI — excellent for model training', '#ef4444')
                    if val > 8000: return ('Good for inference & small training jobs', '#f97316')
                    return ('Limited — better for inference or CPU tasks', '#60a5fa')
                if name == 'value':
                    if val > 1.2: return ('Exceptional value — great performance per dollar', '#10b981')
                    if val > 0.6: return ('Good value', '#84cc16')
                    return ('Paying for performance — lower value', '#f59e0b')
                if name == 'efficiency':
                    if val > 0.5: return ('Very efficient', '#10b981')
                    return ('Efficiency average', '#f59e0b')
                if name == 'upgradeability':
                    if val > 1.5: return ('Highly upgradable', '#7c3aed')
                    return ('Moderate upgrade paths', '#60a5fa')
                return ('', '#9ca3af')

            for k, v in scores.items():
                label, color = score_context(k, v)
                maxv = max_ref.get(k, max(v, 1))
                pct = min(100, int((v / maxv) * 100)) if maxv else 0
                bar = f"<div style='background:rgba(255,255,255,0.04); border-radius:8px; padding:4px; margin-bottom:6px;'>"
                bar += f"<div style='display:flex;justify-content:space-between;align-items:center'><strong style='text-transform:capitalize'>{k.replace('_',' ').title()}</strong> <span class='score-badge'>{v}</span></div>"
                bar += f"<div style='height:10px;border-radius:6px;background:rgba(255,255,255,0.03);margin-top:6px'><div style='width:{pct}%;height:100%;background:{color};border-radius:6px'></div></div>"
                bar += f"<div style='font-size:12px;color:#bcd0e6;margin-top:6px'>{label}</div></div>"
                st.markdown(bar, unsafe_allow_html=True)

            st.markdown("**Compatibility**")
            for k, v in build.get('compatibility', {}).items():
                emoji = '✅' if '✅' in v else ('⚠' if '⚠' in v else '❌')
                st.markdown(f"- **{k}**: {emoji} {v}")
