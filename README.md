# PHONEPE-DATA-VISUALISATION
Extract data from the Phonepe pulse Github repository to process it and obtain  valuble insights and information for visulaisation.

from git import Repo 
import pandas as pd
import json
import os
import mysql.connector
import plotly.express as px
import streamlit as st

config = {
    "user": "root",
    "password": "1234",
    "host": "127.0.0.1",
    "database": "phonepe_pulse"
}
connection = mysql.connector.connect(**config)
cursor = connection.cursor()


def agg_trans():
#This is to direct the path to get the data as states

    path = 'D:/GUVI/PHONEPE/pulse/data/aggregated/transaction/country/india/state/'

    Agg_state_list=os.listdir(path)
    #print(Agg_state_list)

    clm={'State':[], 'Year':[],'Quarter':[],'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]}

    for i in Agg_state_list:
        p_i=path + i +'/'
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+'/'
            Agg_yr_list= os.listdir(p_j) #file_list = os.listdir(directory_path)

            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                D=json.load(Data)
                for z in D['data']['transactionData']:
                    Name=z['name']
                    count=z['paymentInstruments'][0]['count']
                    amount=z['paymentInstruments'][0]['amount']
                    clm['Transacion_type'].append(Name)
                    clm['Transacion_count'].append(count)
                    clm['Transacion_amount'].append(amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quarter'].append(int(k.strip('.json')))
    #Succesfully created a dataframe
    Agg_Trans=pd.DataFrame(clm)
    Agg_Trans['State'] = Agg_Trans['State'].str.replace('andaman-&-nicobar-islands', 'Andaman & Nicobar-islands')
    Agg_Trans['State'] = Agg_Trans['State'].str.replace('-',' ')
    Agg_Trans['State'] = Agg_Trans['State'].str.title()
    Agg_Trans['State'] = Agg_Trans['State'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu', 'Dadra & Nagar-Haveli & Daman & Diu')
    #print(Agg_Trans)
    



    create_table = '''CREATE TABLE IF NOT EXISTS agg_transaction(STATE VARCHAR(250),
                                                YEAR VARCHAR(250),
                                                QUARTER INT,
                                                TRANSACTION_TYPE VARCHAR(250),
                                                TRANSACTION_COUNT VARCHAR(250),
                                                TRANSACTION_AMOUNT VARCHAR(250))'''

    cursor.execute(create_table)
    connection.commit()


    for index, row in Agg_Trans.iterrows():
        insert_query = '''INSERT INTO agg_transaction(STATE ,
                                    YEAR ,
                                    QUARTER ,
                                    TRANSACTION_TYPE,
                                    TRANSACTION_COUNT,
                                    TRANSACTION_AMOUNT) 
                                    values(%s,%s,%s,%s,%s,%s) '''
        vale_agg_transaction = (row['State'],
                                row['Year'],
                                row ['Quarter'], 
                                row['Transacion_type'], 
                                row['Transacion_count'],
                                row['Transacion_amount'])
        
        cursor.execute(insert_query,vale_agg_transaction)
        connection.commit()
    return Agg_Trans


df = agg_trans()
print(df)

import streamlit as st
st.title("PHONEPE DATA VISUALISATION")
