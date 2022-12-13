import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import os

st.title("EZ MMR")
st.write("## U NEED TO BE like a Shark!")
st.write("**Let Me mid BOBO**")
df_dota = pd.read_csv("./data/hero_stats.csv")


## LOAD DATA
# @st.cache(persist=True)
# def load_data():
# 	df = pd.read_csv("C://Users/Thirawut/Project/Streamlit01/data/hero_stats.csv")
# 	return df

# df_dota = load_data()

# st.write("Example : DotA Heroes")
# st.table(df_dota[:5])

num_shown = st.slider("Example : DotA Heroes", 0, 130, 5)
st.table(df_dota[:num_shown])

## EPS
fig = px.box(df_dota, x=["Health",	"Health Regen",	"Mana",	"Mana Regen",	"Armor",	"%Physical Damage Reduction",	"Movement Speed"], 
	hover_data=[" separated by space. * wildcards allowed"],
	title="Dota Heroes stats",
	width=700)

st.write(fig)