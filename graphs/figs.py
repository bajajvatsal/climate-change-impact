# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def avg_temp_scatter():
    df = pd.read_csv("data/temperatures.csv")
    fig = px.scatter(df, x="YEAR", y="ANNUAL", title="Average Temperature of India", color_discrete_sequence=px.colors.qualitative.Light24)
    px.line(df, x="YEAR", y="ANNUAL")
    return fig


def avg_t_go_chart():
    df = pd.read_csv("data/temperatures.csv")
    x = df.iloc[:,0]
    y = df.iloc[:,13]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y + 5, name="spline",
                            text=["tweak line smoothness<br>with 'smoothing' in line object"],
                            hoverinfo='text+name',
                            line_shape='spline'))
