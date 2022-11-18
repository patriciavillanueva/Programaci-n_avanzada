import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime


st.title("Fallecidos Covid-19")
st.subheader("Introducción")
st.write("El covid-19 cambió todo y afectando a millones de personas. El 11 de marzo de 2020, la Organización Mundial de la Salud declaró el brote de COVID-19 como una pandemia, ya que se ha extendido simultáneamente a más de 100 países en todo el mundo. El 16 de marzo de 2020, el expresidente Martín Vizcarra declaró emergencia sanitaria en Perú y prohibió las reuniones públicas debido a la pandemia del Covid.")

agendar = st.slider("Programe la asesoria:", value=(time(11,30), time(12,45)))
st.write("Esta agendado para: {}".format(agendar))

d = st.date_input("Fecha de cumpleaños", datetime.date(2019,7,6))

st.write("Tu cumple es:", d)

option = st.selectbox("¿Como nos ponemos en contacto?", ('Email', 'Telefono', 'Whatsapp'))

st.write("Su seleccion fue: ", option)

n = st.slider("n", 5, 100, step=1)

chart_data = pd.DataFrame(np.random.randn(n), columns=['data'])
st.line_chart(chart_data)
