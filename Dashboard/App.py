import os
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image 
import datetime

data_file = "../Data/superstore.csv"

# data reading and data cleaning 

df = pd.read_csv(data_file,encoding='unicode_escape')

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])



st.set_page_config(layout="wide")
st.markdown('<style>div.bloack-container{padding-top:0.1rem;}</style>',unsafe_allow_html=True)


image = Image.open("../Data/superstore.png")


with st.sidebar:
    st.write("Here will filter")

box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
st.write(f"Last Updated : {box_date}")

col1,col2 = st.columns([0.1,0.9])

with col1:
    st.image(image,width=100)

html_title = """

<style>
.main-title {
font-weight:bold;
padding:5px;
birder-radius:6px;
}</style>
<center><h1 class="main-title"> Superstore Dashboard </center> 

"""
with col2:
    st.markdown(html_title,unsafe_allow_html=True)

col3,col4 = st.columns([0.5,0.5])


with col3:
    fig = px.bar(df,x="Ship Mode",y="Sales",labels={"Sales":"Total Sales ($)"},
                 title="Total Sales by Ship Mode",hover_data=['Sales'],template="gridon",height=500,text='Sales')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig,use_container_width=True)

_,view1, dwn1, view2, dwn2 = st.columns([0.15,0.20,0.20,0.20,0.20])

with view1:
    expander = st.expander("Sales by Ship Mode")
    data = df[["Ship Mode","Sales"]].groupby(by='Ship Mode')['Sales'].sum()
    expander.write(data)
with dwn1:
    st.download_button("Get Data",data=data.to_csv().encode('utf-8'),file_name='sales_by_ship_mode.csv',mime='text\csv')


with col4:
    fig = px.bar(df,x="Category",y="Sales",labels={"Sales":"Total Sales ($)"},
                 title="Total Sales by Category",hover_data=['Sales'],template="gridon",height=500,text='Sales')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig,use_container_width=True)


with view2:
    expander = st.expander("Sales by Ship Mode")
    data = df[["Category","Sales"]].groupby(by='Category')['Sales'].sum()
    expander.write(data)
with dwn2:
    st.download_button("Get Data",data=data.to_csv().encode('utf-8'),file_name='sales_by_category.csv',mime='text\csv')
