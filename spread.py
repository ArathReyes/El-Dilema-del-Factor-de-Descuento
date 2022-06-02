# -*- coding: utf-8 -*-
"""
Created on Fri May 27 10:19:38 2022

@author: Arath Reyes
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import plotly.express as px

#import plotly.io as pio
#pio.renderers.default='browser' # browser, svg

import plotly.offline as pyo
pyo.init_notebook_mode()

# Download Data
path = "C:\\Users\\Arath Reyes\\Desktop\\Libros\\Quantitative Finance\\ted-spread-historical-chart.csv"
spread = pd.read_csv(path)
spread = spread.dropna()
spread["date"] = spread["date"].apply(lambda x:datetime(int(x[6:]), int(x[3:5]), int(x[:2])))
spread["Puntos Base"] = spread[" value"]*100
spread.rename(columns = {'date':'Fecha'}, inplace = True)

# Inline Plot
sns.set_style("darkgrid")
plt.figure(figsize = (16,8))
ax = sns.lineplot(data = spread[(spread["Fecha"]>datetime(2007,3,1)) & (spread["Fecha"]< datetime(2010,3,10))],\
                  y = "Puntos Base", x = "Fecha", color = "red")
ax.set_title("LIBOR-OIS Spread 2007-2010 ")
plt.show()

# Html Plot
fig = px.line(spread, x='Fecha', y='Puntos Base', title='LIBOR-OIS Spread')
fig.update_xaxes(rangeslider_visible=True)
fig.write_html('spread.html', auto_open=True)
#fig.show()