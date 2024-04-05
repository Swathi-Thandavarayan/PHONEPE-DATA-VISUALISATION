import streamlit as st
import mysql.connector
import matplotlib.pyplot as plt
import plotly
import pydeck as pdk
import plotly.express as px
import pandas as pd

config = {
    "user": "root",
    "password": "1234",
    "host": "127.0.0.1",
    "database": "phonepe_pulse"
}
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

#STREAMLIT

st.set_page_config(
    page_title="PHONEPE DATA VISUALISATION",
    layout="centered" # wide or centered
    )
with st.sidebar:
    st.title(" PHONEPE PULSE DATA VISUALISATION  AND EXPLORATION ")
    st.subheader("A  User-Friendly Tool Using Streamlit and Plotly")

st.title

clm1,clm2,clm3 = st.columns(3)
with clm1:
    aggtrans = '''SELECT * FROM  top_users_district'''
    cursor.execute(aggtrans)
    df = pd.DataFrame()
    results = cursor.fetchall()
    df = pd.DataFrame(results)
    
    

    if st.button("AGGREGATED"):
       st.write("hello")
        
     
        
        
with clm2:
    st.header("MAPS")
    aggtrans = '''SELECT * FROM  top_users_district'''
    cursor.execute(aggtrans)
    df = pd.DataFrame()
    results = cursor.fetchall()
    df = pd.DataFrame(results)
    #query = '''SELECT COLUMN_NAME FROM FROM top_users_district'''
    #cursor.execute(query)
    #results = cursor.fetchall()
    #st.write(results)
with clm3:
    st.header("TOP")

