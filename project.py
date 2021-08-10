import pandas as pd
import plotly_express as px
df = pd.read_csv('project.csv')
graph = px.line(df,x='date',y='cases',color='country')
graph.show()

