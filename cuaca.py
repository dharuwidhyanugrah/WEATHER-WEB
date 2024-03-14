import streamlit as st
import requests

API_KEY ="b74b14e5a74aa003391444764d3c0561"

def searchCity(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    weather = requests.get(url)
    weather = weather.json()

    description = weather['weather'][0]['description']
    ico = weather['weather'][0]['icon']
    temp = weather['main']['temp']
    pressure = weather['main']['pressure']
    humidity = weather['main']['humidity']
    windspeed = weather['wind']['speed']
    lat = weather['coord']['lat']
    lon = weather['coord']['lon']

    return description, ico, temp, pressure, humidity, windspeed, lat, lon 

st.title('Weather App')

city = st.text_input("Search City...")
if st.button("Search"):
    description, ico, temp, pressure, humidity, windspeed, lat, lon = searchCity(city)

    c1, c2, c3, c4, c5, c6 = st.columns(6)

    with c1:
        st.subheader('Weather')
        st.write(description)

    with c2:
        st.subheader('Icon')
        st.image(f"https://openweathermap.org/img/wn/{ico}@2x.png")

    with c3:
        st.subheader("Temp")
        st.write(f"{temp}&deg;C")

    with c4:
        st.subheader("Pressure")
        st.write(pressure)

    with c5:
        st.subheader("Speed")
        st.write(windspeed)

    with c6:
        st.subheader("Humidity")
        st.write(humidity)