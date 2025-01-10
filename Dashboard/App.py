import os
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from PIL import Image 
import datetime

data_file = "../Data/superstore.csv"

# data reading and data cleaning 

df = pd.read_csv(data_file,encoding='unicode_escape')

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Year'] = pd.DatetimeIndex(df['Order Date']).year
df['Month'] = pd.DatetimeIndex(df['Order Date']).month

## Adding Year-Month column in dataframe
df['Year-Month'] = df['Year'].astype(str) +'-'+  df['Month'].astype(str)

filters =[]

st.set_page_config(layout="wide")
st.markdown('<style>div.bloack-container{padding-top:0.1rem;}</style>',unsafe_allow_html=True)


image = Image.open("../Data/superstore.png")


with st.sidebar:
    st.write("## Filter")
    options = st.multiselect(
        "Select Year",
        [2014,2015,2016,2017]      
    )
    filters = [int(i) for i in options]
    #st.write(options)



if len(filters) > 0:
    tempDF = pd.DataFrame(columns=df.columns)
    for i in range(0,len(filters),1):
        tempDF = pd.concat([tempDF,df[df['Year'] == filters[i]]],ignore_index=True)
    df = tempDF


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


# Sales By Ship Mode

with view1:
    expander = st.expander("Sales by Ship Mode")
    data = df[["Ship Mode","Sales"]].groupby(by='Ship Mode')['Sales'].sum()
    expander.write(data)
with dwn1:
    st.download_button("Get Data",data=data.to_csv().encode('utf-8'),file_name='sales_by_ship_mode.csv',mime='text\csv')

# Sales by Category

with col4:
    fig = px.bar(df,x="Category",y="Sales",labels={"Sales":"Total Sales ($)"},
                 title="Total Sales by Category",hover_data=['Sales'],template="gridon",height=500,text='Sales')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig,use_container_width=True)


with view2:
    expander = st.expander("Sales by Category")
    data = df[["Category","Sales"]].groupby(by='Category')['Sales'].sum()
    expander.write(data)
with dwn2:
    st.download_button("Get Data",data=data.to_csv().encode('utf-8'),file_name='sales_by_category.csv',mime='text\csv')



col5,col6 = st.columns([0.5,0.5])
_,view3, dwn3 , view4 , dwn4 = st.columns([0.15,0.20,0.20,0.20,0.20])


# Sales by region : 
with col5:
    fig = px.bar(df,x="Region",y="Sales",labels={"Sales":"Total Sales ($)"},
                 title="Total Sales by Region",hover_data=['Sales'],template="gridon",height=500,text='Sales')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig,use_container_width=True)
with view3:
    expander = st.expander('Sales by Region')
    data = df[["Region","Sales"]].groupby(by='Region')["Sales"].sum()
    expander.write(data)

with dwn3:
    st.download_button("Get Data",data=data.to_csv().encode('utf-8'),file_name="Sales_by_Region.csv",mime='text\csv')


with col6:
    data = df[['Region','Profit']].groupby(by=['Region']).sum()['Profit'].round(2)
    data = data.reset_index()
    fig = px.bar(data,x="Region",y="Profit",labels={"Sales":"Total Profit ($)"},
                 title="Total Sales by Region",hover_data=['Profit'],template="gridon",height=500,text='Profit')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig,use_container_width=True)


with view4:
    expander = st.expander('Profit by Region')
    data = df[["Region","Profit"]].groupby(by='Region')["Profit"].sum()
    expander.write(data)

with dwn4:
    st.download_button("Get Data",data=data.to_csv().encode('utf-8'),file_name="Profit_by_Region.csv",mime='text\csv')



_,col7 = st.columns([0.1,0.9])



with col7:
    data = df[['Year-Month','Sales']].groupby(by=['Year-Month']).sum()['Sales'].round(2)
    data = data.reset_index()
    fig = px.bar(data,x="Year-Month",y='Sales',labels={"Sales":"Total Sales ($)"},
                 title="Yearly Sales",hover_data=['Sales'],template="gridon",height=500,text="Sales")
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig,use_container_width=True)

_,view5, dwn5,_= st.columns([0.30,0.20,0.20,0.30])

with view5:
    expander = st.expander("Sales by Year Month")
    data = df[['Year-Month','Sales']].groupby(by=['Year-Month']).sum()['Sales'].round(2)
    data = data.reset_index()
    expander.write(data)
with dwn5:
    st.download_button("Get Data",data=data.to_csv().encode('utf-8'),file_name='sales_by_Year_Month.csv',mime='text\csv')



