import plotly.graph_objects as go
import numpy as np
import streamlit as st


def box_mesh(x, y, z, dx, dy, dz, color, name):
    # Create the 8 corners
    x0 = x - dx/2
    x1 = x + dx/2
    y0 = y - dy/2
    y1 = y + dy/2
    z0 = z - dz/2
    z1 = z + dz/2
    verts = np.array([
        [x0,y0,z0],[x1,y0,z0],[x1,y1,z0],[x0,y1,z0],
        [x0,y0,z1],[x1,y0,z1],[x1,y1,z1],[x0,y1,z1]
    ])
    # faces (triangles)
    I = [0,0,0,3,4,4,4,7,1,2,5,6]
    J = [1,3,4,2,5,7,0,4,2,3,6,7]
    K = [3,4,5,6,6,0,1,0,5,6,7,4]
    mesh = go.Mesh3d(
        x=verts[:,0], y=verts[:,1], z=verts[:,2],
        i=I, j=J, k=K,
        color=color, opacity=0.9, name=name, flatshading=True
    )
    return mesh


def build_dimensions_from_components(components: dict):
    # Heuristic sizes (mm converted to arbitrary units)
    case_w, case_h, case_d = 40, 30, 15
    mobo_w, mobo_h, mobo_d = 30, 20, 2
    gpu_len = components.get('gpu', {}).get('length_mm', 240) / 10
    gpu_w, gpu_h, gpu_d = gpu_len, 6, 2
    ram_w, ram_h, ram_d = 6, 3, 0.5
    storage_w, storage_h, storage_d = 8, 4, 0.5
    cooler_w, cooler_h, cooler_d = 10, 10, 6
    return {
        'case': (0,0,0, case_w, case_d, case_h),
        'motherboard': (0, -2, -1, mobo_w, mobo_d, mobo_h),
        'gpu': (5, 0, -3, gpu_w, gpu_d, gpu_h),
        'ram': (-5, 3, -1, ram_w, ram_d, ram_h),
        'storage': (10, 6, -2, storage_w, storage_d, storage_h),
        'cooler': (-2, -1, 3, cooler_w, cooler_d, cooler_h)
    }


def render_3d_build(build: dict, highlight: str = None):
    comps = build.get('components', {})
    dims = build_dimensions_from_components(comps)
    fig = go.Figure()

    colors = {
        'case':'#111827', 'motherboard':'#0ea5a4', 'gpu':'#ef4444', 'ram':'#84cc16', 'storage':'#f59e0b', 'cooler':'#6366f1'
    }

    for key, d in dims.items():
        x,y,z,dx,dy,dz = d
        color = colors.get(key,'#888')
        opacity = 1.0 if (highlight is None or highlight==key) else 0.25
        m = box_mesh(x,y,z,dx,dy,dz,color=color,name=key)
        m.opacity = opacity
        fig.add_trace(m)
        # add an invisible marker at the center for click interaction
        fig.add_trace(go.Scatter3d(x=[x], y=[y], z=[z], mode='markers', marker=dict(size=6, color=color), name=key, customdata=[key], hovertext=[key], hoverinfo='text'))

    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
            aspectmode='manual', aspectratio=dict(x=2, y=1, z=0.6)
        ),
        margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False
    )
    return fig
