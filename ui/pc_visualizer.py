import streamlit as st
from PIL import Image, ImageDraw
from io import BytesIO


def render_pc_visual(build: dict):
    # Simple layered 2D visualization using PIL
    width, height = 600, 400
    img = Image.new('RGBA', (width, height), (20,20,30,255))
    draw = ImageDraw.Draw(img)

    # Draw case rectangle
    draw.rectangle((50,30,550,370), outline=(200,200,220), width=3)
    comps = build.get('components', {})
    # Draw motherboard
    draw.rectangle((120,60,480,260), outline=(100,150,200), width=2)
    draw.text((130,65), f"{comps.get('motherboard',{}).get('name','Motherboard')}", fill=(200,200,200))
    # Draw GPU
    draw.rectangle((130,150,420,200), outline=(180,100,120), width=2)
    draw.text((135,152), f"{comps.get('gpu',{}).get('name','GPU')}", fill=(220,220,220))
    # Draw RAM sticks
    draw.rectangle((300,80,330,140), outline=(120,200,120), width=2)
    draw.text((305,82), f"{comps.get('ram',{}).get('capacity_gb','RAM')}GB", fill=(220,220,220))

    buf = BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    st.image(buf)
