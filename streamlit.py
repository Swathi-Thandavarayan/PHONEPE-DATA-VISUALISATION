import streamlit as st
import mysql.connector
import matplotlib.pyplot as plt
import plotly
import pydeck as pdk
import plotly.express as px
import pandas as pd
import datetime
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
    layout="centered") # wide or centered

with st.sidebar:
    st.title(":violet[PHONEPE PULSE DATA] VISUALISATION  AND EXPLORATION ")
    st.subheader("A  User-Friendly Tool Using Streamlit and Plotly")
    st.write("""This project will be a live geo visualization dashboard that displays information
          and insights from the :violet[Phonepe] pulse Github repository of
          :rainbow[The Indian digital payments] """)
    st.markdown("""The concept of this project is to build an understanding, 
            insights and visualization on how digital payments 
            have evolved over the years in  :rainbow[INDIA].""")

st.title(" :grey[DATA VISUALISATION] - :rainbow[DIGITAL INDIA]")


selected_date = st.date_input("Select a date")

# Display selected date
st.write("Selected Date:", selected_date)

clm1,clm2,clm3 = st.columns(3)
with clm1:
    with st.container(border=True):
        st.markdown("### AGGREGATED ")
        st.write("Aggregated values of various payment categories")
        #st.radio
        
        if st.button("Aggregated Transaction"):
            st.markdown('''Transaction data broken down by type of payment''')
        aggtrans = '''SELECT * FROM  top_users_district'''
        cursor.execute(aggtrans)
        df = pd.DataFrame()
        results = cursor.fetchall()
        df = pd.DataFrame(results)
        #st.dataframe(df)
    
    

    #if st.button("AGGREGATED"):
    #   st.write("hello")
        
     
        
        
with clm2:
    with st.container(border=True):
        st.markdown("### MAPS ")
        st.write("Total values at the State and District levels.")
    #st.header("MAPS")
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
    with st.container(border=True):
        st.markdown("### TOP ")
        st.write("Totals of top States / Districts /Pin Codes")
    #st.header("TOP")


centered_button_style = """
    display: flex;
    justify-content: center;
"""

# Render Streamlit app
st.write("""
    <div style="{}">
        <button>PHONEPE</button>
    </div>
""".format(centered_button_style), unsafe_allow_html=True)
