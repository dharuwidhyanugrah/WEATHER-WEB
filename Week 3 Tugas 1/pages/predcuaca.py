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

    for n in pred['list']:
        temp = n['main']['temp']
        feels = n['main']['feels_like']
        humid = n['main']['humidity']
        wind = n['wind']['speed']
        iconPred = n['weather'][0]['icon']
        status = n['weather'][0]['description']
        time = convTime(n['dt'])

    return time, temp, feels, humid, wind, iconPred, status

def convTime(dt):
    normalDate = datetime.fromtimestamp(dt)
    return normalDate

def image():
    iconPred = ['list'][0]['weather'][0]['icon']
    st.image(f"https://openweathermap.org/img/wn/{iconPred}@2x.png")


st.title("Weather Prediction")

st.write(predWeather, image)