#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import urllib.request
import base64

st.sidebar.header("Entradas del usuario")
año_seleccionado=st.sidebar.selectbox('Edad', list(reversed(range(0,117))))

st.header("Conjunto de datos FALLECIDOS COVID")
@st.experimental_memo
def download_data():
   url="https://www.datosabiertos.gob.pe/sites/default/files/Catalogo1960_2021.csv"
   filename="Catalogo1960_2021.xlsx"
   urllib.request.urlretrieve(url,filename)
   df=pd.read_csv("Catalogo1960_2021.xlsx")
   return df
c=download_data()
st.write('Dimensiones: ' + str(c.shape[0]) + ' filas y ' + str(c.shape[1]) + ' columnas')
st.dataframe(c)
st.subheader("Características del Dataset")
st.write(c.describe())

unique_sexo=["FEMENINO","MASCULINO"]
selected_sexo=st.sidebar.multiselect('Sexo', unique_sexo, unique_sexo)

unique_depa=["AMAZONAS","ANCASH","APURIMAC","AREQUIPA","AYACUCHO","CAJAMARCA","CALLAO","CUSCO","HUANCAVELICA","HUANUCO","ICA","JUNÍN","LA LIBERTAD","LAMBAYEQUE","LIMA","LORETO","MADRE DE DIOS","MOQUEGUA","PASCO","PIURA","PUNO","SAN MARTÍN","TACNA","TUMBES","UCAYALI"]
selected_depa=st.sidebar.multiselect('Departamento', unique_depa, unique_depa)
