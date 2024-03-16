import streamlit as st
import requests
from datetime import datetime
import main

#import variabel
new_city = main.city

API_Key ="4ef3ea40ea6ecb1293858d825436531d"

def predWeather(new_city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={new_city}&appid={API_Key}"

    pred = requests.get(url)
    pred = pred.json()

    temp = pred['list'][0]['main']['temp']
    feels = pred['list'][0]['main']['feels_like']
    humid = pred['list'][0]['main']['humidity']
    wind = pred['list']['wind']['speed']
    status = pred['list'][0]['weather'][0]['description']
    time = convTime(pred['list']['dt'])

    return time, temp, feels, humid, wind, status

def convTime(dt):
    normalDate = datetime.fromtimestamp(dt)
    return normalDate

def image():
    iconPred = ['list'][0]['weather'][0]['icon']
    st.image(f"https://openweathermap.org/img/wn/{iconPred}@2x.png")


st.title("Weather Prediction")

time, temp, feels, humid, wind, status = predWeather(new_city)

st.header(new_city)

col1, col2, col3 = st.columns(2)
with col1:
    st.subheader(status)
with col2:
    st.subheader(time)

st.image(image)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label = "Temperature", value = (f"{temp}&deg;F"), help = (feels))
with col2:
    st.metric(label = "Wind", value = (wind))
with col3:
    st.metric(label = "Humidity", value = (humid))
