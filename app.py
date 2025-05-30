import streamlit as st
import numpy as np
import pandas as pd
import requests
import json



'''
# TaxiFareModel front
### version 000.0000001
'''
label = "change me.."

pickup_date = st.text_input('Pickup date', value="2014-07-06")
pickup_time = st.text_input('Pickup time', value="18:00")

pickup_longitude = st.text_input('Pickup Longitude', value="73.950655")
pickup_latitude = st.text_input('Pickup Latitude', value="40.783282")

dropoff_longitude = st.text_input('Dropoff Longitude', value="-73.984365")
dropoff_latitude = st.text_input('Dropoff Latitude', value="40.76980")

passenger_count = st.text_input('Passenger Count', value="2")



#calling the API
apiurl = 'https://taxifare.lewagon.ai//predict?'
calling = f'{apiurl}pickup_datetime={pickup_date}%20{pickup_time}&pickup_longitude={pickup_longitude}&pickup_latitude={pickup_latitude}&dropoff_longitude={dropoff_longitude}&dropoff_latitude={dropoff_latitude}&passenger_count={passenger_count}'

def call_api(params):
    print('waiting.....')
    results = requests.get(params).json()
    out =  f'Here is the predicted fare: {results["fare"]}'
    return out

if st.button("Predict"):
    #st.write(calling)
    st.write(call_api(calling))
else:
    st.write("Waiting for user input")
