from graphs import figs
import streamlit.components.v1 as components
# import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Climate Change Impact on Food", layout="wide")
st.title('Climate Change Impact on Food')

crops = st.multiselect("Select a Crop", ['Anise, badian, coriander, cumin, caraway, fennel and juniper berries, raw',
                                         'Apples', 'Apricots', 'Areca nuts', 'Bananas', 'Barley',
                                         'Beans, dry', 'Beer of barley, malted', 'Cabbages',
                                         'Cantaloupes and other melons', 'Carrots and turnips',
                                         'Cashew nuts, in shell', 'Cassava, fresh', 'Castor oil seeds',
                                         'Cauliflowers and broccoli', 'Cherries', 'Chick peas, dry',
                                         'Chillies and peppers, dry (Capsicum spp., Pimenta spp.), raw',
                                         'Chillies and peppers, green (Capsicum spp. and Pimenta spp.)',
                                         'Cocoa beans', 'Coconut oil', 'Coconuts, in shell',
                                         'Coffee, green', 'Coir, raw', 'Cotton lint, ginned', 'Cotton seed',
                                         'Cottonseed oil', 'Cucumbers and gherkins',
                                         'Eggplants (aubergines)', 'Figs', 'Ginger, raw', 'Grapes',
                                         'Green garlic', 'Groundnut oil', 'Groundnuts, excluding shelled',
                                         'Jute, raw or retted',
                                         'Kenaf, and other textile bast fibres, raw or retted',
                                         'Lemons and limes', 'Lentils, dry', 'Lettuce and chicory',
                                         'Linseed', 'Maize (corn)', 'Mangoes, guavas and mangosteens',
                                         'Margarine and shortening', 'Millet', 'Molasses',
                                         'Mushrooms and truffles', 'Natural rubber in primary forms',
                                         'Nutmeg, mace, cardamoms, raw', 'Oil of linseed', 'Oil of maize',
                                         'Oil of sesame seed', 'Okra',
                                         'Onions and shallots, dry (excluding dehydrated)', 'Oranges',
                                         'Other beans, green',
                                         'Other berries and fruits of the genus vaccinium n.e.c.',
                                         'Other citrus fruit, n.e.c.', 'Other fruits, n.e.c.',
                                         'Other oil seeds, n.e.c.', 'Other pulses n.e.c.',
                                         'Other stimulant, spice and aromatic crops, n.e.c.',
                                         'Other stone fruits', 'Other tropical fruits, n.e.c.',
                                         'Other vegetables, fresh n.e.c.', 'Papayas',
                                         'Peaches and nectarines', 'Pears', 'Peas, dry', 'Peas, green',
                                         'Pepper (Piper spp.), raw', 'Pigeon peas, dry', 'Pineapples',
                                         'Plums and sloes', 'Pomelos and grapefruits', 'Poppy seed',
                                         'Potatoes', 'Pumpkins, squash and gourds', 'Rape or colza seed',
                                         'Rapeseed or canola oil, crude',
                                         'Raw cane or beet sugar (centrifugal only)', 'Rice',
                                         'Rice, paddy (rice milled equivalent)', 'Safflower seed',
                                         'Safflower-seed oil, crude', 'Seed cotton, unginned',
                                         'Sesame seed', 'Sorghum', 'Soya bean oil', 'Soya beans',
                                         'Sugar cane', 'Sunflower seed', 'Sunflower-seed oil, crude',
                                         'Sweet potatoes', 'Tea leaves', 'Tomatoes',
                                         'True hemp, raw or retted', 'Unmanufactured tobacco',
                                         'Walnuts, in shell', 'Watermelons', 'Wheat'])
options = st.multiselect("Select a Type of Analysis", ["Area harvested", "Production", "Yield"])
crops_q = ','.join(i for i in crops)
options_q = ','.join(i for i in options)
query = f'Item=="{crops_q}" & Element=="{options_q}" '

print(query)
fig6 = figs.query_crop(query)
st.plotly_chart(fig6)


temp_l = ["In values", "Standard Deviation"]

st.write("Temprature")
fig11 = figs.temp()
st.plotly_chart(fig11)

st.write("Emissions Visualization")
fig2 = figs.global_ghg_em_1()
st.plotly_chart(fig2)

fig3 = figs.global_ghg_em_2()
st.plotly_chart(fig3)

sector_wise = [""]
fig4 = figs.slide_yeilds_bar_graph()
st.plotly_chart(fig4)
