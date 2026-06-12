import plotly.graph_objects as go

def budget_pie(build: dict):
    labels = []
    values = []
    for k,v in build.get('components', {}).items():
        labels.append(k)
        values.append(v.get('price',0))
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.4)])
    fig.update_layout(margin=dict(l=0,r=0,t=0,b=0))
    return fig

def performance_bar(build: dict):
    comps = build.get('components',{})
    labels = ['cpu','gpu']
    vals = [comps.get('cpu',{}).get('performance_score',0), comps.get('gpu',{}).get('performance_score',0)]
    fig = go.Figure([go.Bar(x=labels, y=vals)])
    fig.update_layout(yaxis_title='Performance Score', margin=dict(l=0,r=0,t=0,b=0))
    return fig
