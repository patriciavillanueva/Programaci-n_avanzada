import urllib.request
import streamlit as st
import pandas as pd
from PIL import Image
st.title('Fallecidos por COVID-19 - [Ministerio de Salud - MINSA]')

#CRITERIOS
image_INTRODUCCION = Image.open('INTRODUCCION.jpg')
st.image(image_INTRODUCCION)

st.markdown("""
	Esta app permite al usuario visualizar los datos de fallecidos por COVID-19
	* **Base de datos:** [MINAM-Ministerio de Salud del Perú (https://www.datosabiertos.gob.pe/dataset/fallecidos-por-covid-19-ministerio-de-salud-minsa).
	""")

#CRITERIOS
st.subheader("**CRITERIOS TECNICOS**")    
st.write("""A partir del 31.mayo.2021 se cambió el criterio de “Fallecidos por Covid-19” por “Muertes por Covid-19” y como resultado el dataset creció casi al triple en el número de registros. Esta nueva clasificación está definida por el cumplimiento de al menos uno de los siguientes siete criterios técnicos:""")
image_CRITERIOS = Image.open('CRITERIOS.jpg')
st.image(image_CRITERIOS)

#IMAGEN PORTADA
imagen_portada = Image.open('imagenportada.jpg')
st.image(imagen_portada)

#VIDEO DE YOUTUBE
st.subheader("**VIDEO INFORMATIVO DE LA PROBLEMATICA**")    
video_file = open('Coronavirus Covid-19_ Claves para entender la enfermedad y protegerse - Clínica Alemana.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.write("**Fuente**: Clínica Alemana. (2020). https://www.youtube.com/watch?v=vlzxSleRnmg")



