import urllib.request
import streamlit as st
import pandas as pd
from PIL import Image
st.title('Fallecidos por COVID-19 - [Ministerio de Salud - MINSA]')

#CRITERIOS
imageCRITERIOS = Image.open('CRITERIOS.jpg')
st.image(imageCRITERIOS)

#IMAGEN PORTADA
imagenportada = Image.open('imagenportada.jpg')
st.image(imagenportada)

#VIDEO DE YOUTUBE
st.subheader("**el covicho**")    
video_file = open('Coronavirus Covid-19_ Claves para entender la enfermedad y protegerse - Clínica Alemana.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.write("**Fuente**: Clínica Alemana. (2020). https://www.youtube.com/watch?v=vlzxSleRnmg")



