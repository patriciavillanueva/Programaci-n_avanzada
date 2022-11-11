import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime


st.title("Proyecto de Programacion Avanzada 2022-2")
st.write("Hola **como** estas")

agendar = st.slider("Programe la asesoria:", value=(time(11,30), time(12,45)))
st.write("Esta agendado para: {}".format(agendar))

d = st.date_input("Fecha de cumpleaños", datetime.date(2019,7,6))

st.write("Tu cumple es:", d)

option = st.selectbox("¿Como nos ponemos en contacto?", ('Email', 'Telefono', 'Whatsapp'))

st.write("Su seleccion fue: ", option)

n = st.slider("n", 5, 100, step=1)

chart_data = pd.DataFrame(np.random.randn(n), columns=['data'])
st.line_chart(chart_data)
