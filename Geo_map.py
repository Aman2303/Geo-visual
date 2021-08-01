# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 14:40:34 2021

@author: amsinha
"""

import json
import pandas as pd
import plotly.io as pio
pio.renderers.default='browser'
d1=open(r"C:\Users\amsinha\Downloads\Work Request\Work Request\results\orlando_averaged_2019-01-01.geojson")
data = json.load(d1)
d2=data["features"][0]
d3=pd.json_normalize(data, record_path =['features'])
#d3.to_excel(r"C:\Users\amsinha\Downloads\Work Request\Work Request\results\dataframe.xlsx")

base=pd.read_excel(r"C:\Users\amsinha\Downloads\Work Request\Work Request\results\dataframe.xlsx")
today = date.today()
import plotly.express as px
#df = px.data.election()
#geojson = px.data.election_geojson()
#print(geojson["features"][0])	
#candidates = df.winner.unique()
df = px.data.election()
geojson = px.data.election_geojson()

fig = px.choropleth_mapbox(base, geojson=data, locations="NeighName", color="avg_d_mbps", featureidkey="properties.NeighName",
                           center={"lat": 28.5383, "lon": -81.3792},
                           mapbox_style="carto-positron", zoom=9)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()





import plotly.figure_factory as ff
fig = ff.create_choropleth(base, geojson=data, locations="NeighName", values="avg_d_mbps",
                    featureidkey="properties.NeighName",
                          color_continuous_scale="Viridis",
                           scope='FL',
                           labels={'avg_d_mbps':'unemployment rate'}
                          )


fig = px.choropleth(base, geojson=data, locations="NeighName", color="avg_d_mbps",
                            featureidkey="properties.NeighName",
                           color_continuous_scale="Oranges",
                           scope="usa",
                           hover_name=base["NeighName"],
   #                        hover_data=base["avg_d_mbps"],
                        center = {"lat": 37.0902, "lon": -95.7129},
                           labels={'avg_d_mbps':'unemployment rate'}
                          )
fig.update_geos(
    visible=False, resolution=110, scope="usa",
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Blue",
)
fig.update_geos(fitbounds="locations")


fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
