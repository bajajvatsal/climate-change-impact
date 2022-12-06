# import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def temprature_graph(query):
    df = pd.read_csv("data/official data/temprature.csv")
    data = df.query(query)
    fig = px.histogram(data, x='Year', y='Value')
    return fig


def temp():
    df = pd.read_csv("data/temperatures.csv")
    # data = df.query(query)
    fig = px.scatter(df, x='YEAR', y='ANNUAL')
    return fig


def avg_temp_scatter():
    df = pd.read_csv("data/temperatures.csv")
    fig = px.scatter(df, x="YEAR", y="ANNUAL", title="Average Temperature of India", color_discrete_sequence=px.colors.qualitative.Light24)
    px.line(df, x="YEAR", y="ANNUAL")
    return fig


def avg_t_go_chart():
    df = pd.read_csv("data/temperatures.csv")
    x = df.iloc[:, 0]
    y = df.iloc[:, 13]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y + 5, name="spline",
                             text=["tweak line smoothness<br>with 'smoothing' in line object"],
                             hoverinfo='text+name',
                             line_shape='spline'))


def global_ghg_em_1():
    df = pd.read_csv("data/global-ghg-emissions_fig-1.csv")
    fig = px.bar(df, x="Year", y=["Carbon dioxide", "Methane", "Nitrous oxide", "HFCs & PFCs & SF6"],
                 title="Change in CO2 and other gases over the Years", color_discrete_sequence=px.colors.qualitative.Light24)
    return fig


def global_ghg_em_2():
    df = pd.read_csv("data/global-ghg-emissions_fig-2.csv")
    fig = px.bar(df, x="Year", y=["Energy", "International transport", "Agriculture", "Industrial processes", "Waste",
                 "Land-use change and forestry"], title="Global Greenhouse Gas Emissions by Sector", color_discrete_sequence=px.colors.qualitative.Light24)
    return fig


def slide_yeilds_bar_graph():
    plt.rcParams['figure.figsize'] = 8, 5
    plt.style.use("fivethirtyeight")
    pd.options.plotting.backend = "plotly"

    data1 = pd.read_csv("data/crop type datas/datafile (1).csv")
    data2 = pd.read_csv("data/crop type datas/datafile (2).csv")
    data3 = pd.read_csv("data/crop type datas/datafile (3).csv")
    data0 = pd.read_csv("data/crop type datas/datafile.csv")
    production = pd.read_csv("data/crop type datas/produce.csv")
    df = data0.copy()

    crops = []
    production = []
    for i in range(df.shape[0]):
        for _ in range(8):
            crops.append(df['Crop'][i])
        production = production + df.loc[i][1:].tolist()

    years = df.drop('Crop', axis=1).columns.tolist() * 13

    df = pd.DataFrame({'Crop': crops, 'Year': years, 'Production': production})
    df = df.dropna().reset_index(drop=True)

    fig = px.bar(df, x='Crop', y="Production", animation_frame="Year",
                 animation_group="Crop", color="Crop", hover_name="Crop", range_y=[80, 150])
    fig.update_layout(title="Production rate of Crops per year")
    return fig


def stacked_country_ch():
    df = pd.read_csv("data/global-ghg-emissions_fig-3.csv")
    fig = px.area(df, x="Region", y=['1998', ' 1999', ' 2000', ' 2001', ' 2002', ' 2003', ' 2004', ' 2005', ' 2006', ' 2007', ' 2008', ' 2009',
                  ' 2010', ' 2011', ' 2012', ' 2013', ' 2014', ' 2015', ' 2016', ' 2017', ' 2018', ' 2019', '2020'], color="Region", line_group="Region")
    # fig = px.bar(df, x="Region", y=["Energy", "International transport", "Agriculture", "Industrial processes", "Waste", "Land-use change and forestry"],
    #  title="Global Greenhouse Gas Emissions by Sector, 1990–2010", color_discrete_sequence=px.colors.qualitative.Light24)
    return fig


def query_crop(query):
    df = pd.read_csv("data/FAOSTAT_data_en_12-1-2022.csv")
    data = df.query(query)
    fig = px.line(data, x='Year', y='Value')
    return fig
