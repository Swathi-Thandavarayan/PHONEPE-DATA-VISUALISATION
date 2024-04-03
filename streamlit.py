import streamlit as st
import mysql.connector
import matplotlib.pyplot as plt
import plotly

config = {
    "user": "root",
    "password": "1234",
    "host": "127.0.0.1",
    "database": "phonepe_pulse"
}
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

#STREAMLIT
st.title(" PHONEPE PULSE DATA VISUALISATION  AND EXPLORATION ")
st.subheader("A  User-Friendly Tool Using Streamlit and Plotly")
st.write("welcome")
