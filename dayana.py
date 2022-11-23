#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.sidebar.header("Entradas del usuario")
año_seleccionado=st.sidebar.selectbox('Edad', list(reversed(range(0,117))))

st.header("Conjunto de datos FALLECIDOS COVID")
@st.experimental_memo
def download_data():
   url="https://raw.githubusercontent.com/DayanaHV/Programaci-n_avanzada/main/fallecidos_covid.csv"
   df=pd.read_csv("fallecidos_covid.csv")
   return df
c=download_data()
st.write('Dimensiones: ' + str(c.shape[0]) + ' filas y ' + str(c.shape[1]) + ' columnas')
st.dataframe(c)
st.subheader("Características del Dataset")
st.write(c.describe())

def load_data(year):
	df = download_data()
	df=df.astype({'EDAD_DECLARADA':'str'})
	grouped = df.groupby(df.EDAD_DECLARADA)
	df_EDAD = grouped.get_group(EDAD)
	return df_EDAD

data_by_EDAD=load_data(str(selected_EDAD))

sorted_unique_depa=sorted(data_by_EDAD.DEPARTAMENTO.unique())

selected_depa=st.sidebar.multiselect('Departamento',sorted_unique_depa,sorted_unique_depa)

unique_sexo=["FEMENINO","MASCULINO"]
selected_sexo=st.sidebar.multiselect('SEXO', unique_sexo, unique_sexo)

df_selected=data_by_EDAD[(data_by_EDAD.DEPARTAMENTO.isin(selected_depa))]

def remove_columns(dataset, cols):
	return dataset.drop(cols, axis=1)

cols=np.setdiff1d(unique_sexo, selected_sexo)

st.subheader('Mostrar data de departamento(s) y sexo(s) seleccionado(s)')
data=remove_columns(df_selected, cols)
st.write('Dimensiones: ' + str(data.shape[0]) + ' filas y ' + str(data.shape[1]) + ' columnas')
st.dataframe(data)
