import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime
import matplotlib.pyplot as plt
import gdown
import os


st.title("Fallecidos Covid-19")
st.subheader("In")
st.write("El covid-19 cambió todo y afectando a millones de personas. El 11 de marzo de 2020, la Organización Mundial de la Salud declaró el brote de COVID-19 como una pandemia, ya que se ha extendido simultáneamente a más de 100 países en todo el mundo. El 16 de marzo de 2020, el expresidente Martín Vizcarra declaró emergencia sanitaria en Perú y prohibió las reuniones públicas debido a la pandemia del Covid.")

option = st.selectbox("¿Como nos ponemos en contacto?", ('Edad', 'Sexo', 'Departamento'))

st.write("Su seleccion fue: ", option)

#Construccion del set/list de departamentos (Valores unicos sin NA)
set_departamentos = np.sort(df['DEPARTAMENTO'].dropna().unique())
#Seleccion del departamento
opcion_departamento = st.selectbox('Selecciona un departamento', set_departamentos)
df_departamentos = df[df['DEPARTAMENTO'] == opcion_departamento]
num_filas = len(df_departamentos.axes[0]) 

#Construccion del set/list de provincias (Valores unicos sin NA)
set_provincias = np.sort(df_departamentos['PROVINCIA'].dropna().unique())
#Seleccion de la provincia
opcion_provincia = st.selectbox('Selecciona una provincia', set_provincias)
df_provincias = df_departamentos[df_departamentos['PROVINCIA'] == opcion_provincia]
num_filas = len(df_provincias.axes[0]) 

#Construccion del set/list de distritos (Valores unicos sin NA)
set_distritos = np.sort(df_departamentos['DISTRITO'].dropna().unique())
#Seleccion de la distrito
opcion_distrito = st.selectbox('Selecciona un distrito', set_distritos)
df_distritos = df_departamentos[df_departamentos['DISTRITO'] == opcion_distrito]
num_filas = len(df_distritos.axes[0]) 

st.write('Numero de registros:', num_filas)

#Gráficas

#Gráfica de pie de METODODX
df_metododx = df_distritos.METODODX.value_counts()
df_metododx = pd.DataFrame(df_metododx)
df_metododx = df_metododx.reset_index()  
df_metododx.columns = ['METODODX', 'Total']

fig1, ax1 = plt.subplots()
ax1.pie(df_metododx['Total'], labels=df_metododx['METODODX'], autopct='%1.1f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.write('Distribución por METODODX:')
st.pyplot(fig1)

