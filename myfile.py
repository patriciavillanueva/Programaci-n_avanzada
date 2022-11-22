import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime


st.title("Fallecidos Covid-19")
st.subheader("In")
st.write("El covid-19 cambió todo y afectando a millones de personas. El 11 de marzo de 2020, la Organización Mundial de la Salud declaró el brote de COVID-19 como una pandemia, ya que se ha extendido simultáneamente a más de 100 países en todo el mundo. El 16 de marzo de 2020, el expresidente Martín Vizcarra declaró emergencia sanitaria en Perú y prohibió las reuniones públicas debido a la pandemia del Covid.")

option = st.selectbox("¿Como nos ponemos en contacto?", ('Edad', 'Sexo', 'Departamento'))

st.write("Su seleccion fue: ", option)


