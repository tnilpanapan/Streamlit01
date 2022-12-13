import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import os

pd.set_option('display.width', 10000)


st.title("Zen Group - DashBoard")
st.write("ZEN journey has been driven by cooking spirit and unique tasting selection to fulfill \
	consumers’dynamic desires with epicurean and creative symmetry.")

## LOAD DATA
@st.cache(persist=True)
def load_data():
	df_zen = pd.read_csv("./data/zen_twitter.csv")
	df_set_food = pd.read_csv("./data/food_set.csv")
	
	return df_zen, df_set_food

df_zen, df_set_food = load_data()

## PART FOOD INDUSTRIAL
st.markdown("## Food Industry 🍣")
st.write(f"Food industry ratio: {64*100/794:.2f} % compared to all industry in SET")

## TOTAL INCOME
fig = px.bar(df_set_food, x="st_name", y="total_income", 
	hover_data=["net_profit", "eps", "total_income_ratio", "total_income_rank"],
	title="Compare total income in food industry",
	width=700)

st.write(fig)

## NET PROFIT
fig = px.bar(df_set_food, x="st_name", y="net_profit", 
	hover_data=["total_income", "eps", "total_income_ratio", "total_income_rank"],
	title="Compare net profit in food industry",
	width=700)

st.write(fig)

## EPS
fig = px.bar(df_set_food, x="st_name", y="eps", 
	hover_data=["total_income", "net_profit", "total_income_ratio", "total_income_rank"],
	title="Compare earning per shares in food industry",
	width=700)

st.write(fig)



## PART SHOW TEXT IN ZEN GROUP
st.markdown("## What people talk to us 🎉")
st.write("Please select restaurant name ..")
res_seclected = st.selectbox("restaurant brands", ["ZEN", "Musha by Zen", "On the Table", "AKA", "Sushi Cyu", "Tetsu", 
	"ตำมั่ว", "เฝอ", "เดอตำมั่ว", "ลาวญวน", "แจ่วฮ้อน", "เขียง"])

st.write("Number of shown data ..")
num_shown = st.slider("Number of shown data ..", 0, 130, 25)

zen_dict = df_zen.groupby("food_tag")["text"].apply(list)

def display_text(_res_seclected, _num_shown=25):
	return st.table(df_zen[df_zen["food_tag"] == _res_seclected][["food_tag", "text"]][:_num_shown])

if res_seclected in zen_dict:
	display_text(res_seclected, num_shown)