#$ pip install streamlit --upgrade
import streamlit as st
import urllib.request
import pandas as pd
import numpy as np
st.header("CATALOGO")
@st.experimental_memo

def download_data():
   url="http://server01.labs.org.pe:2005/fallecidos_covid.csv"
   filename="datos_horarios_contaminacion_lima.csv"
   urllib.request.urlretrieve(url,filename)
   df=pd.read_csv('datos_horarios_contaminacion_lima.csv')
   return df
c=download_data()
st.write('Dimensiones: ' + str(c.shape[0]) + ' filas y ' + str(c.shape[1]) + ' columnas')
st.dataframe(c)
st.subheader("Características del Dataset")
st.write(c.describe())
 

