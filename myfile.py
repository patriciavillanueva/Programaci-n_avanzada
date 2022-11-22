import urllib.request
import streamlit as st
import pandas as pd



st.title("Fallecidos por COVID-19 - [Ministerio de Salud - MINSA]")
st.markdown("**Proyecto de Programacion Avanzada 2022-2**")
st.write("--------------------------------------------------------------------------------")

from PIL import Image
intro=Image.open('INTRO.jpg')
st.image(intro)


pict = Image.open('COVI.jpg')
st.image(pict)

#*****************************
st.header("Dataset MINAM")
@st.experimental_memo
def download_data():
   url="http://server01.labs.org.pe:2005/fallecidos_covid.csv"
   filename="datos_horarios_contaminacion_lima.csv"
   urllib.request.urlretrieve(url,filename)
   df=pd.read_csv('data.csv', sep=';')
   return df
#-----------------------------------------------------------------------------
c=download_data()
st.write('**Dimensiones de la tabla:**') 
st.write('* Fila: ' + str(c.shape[0]))
st.write('* Columnas: ' + str(c.shape[1]))
st.dataframe(c)
#-----------------------------------------------------------------------------
st.subheader("Características del Dataset")
st.write(c.describe())
#----------------------------------------------------------------------------
#option = st.selectbox(
     #'Seleccione el tipo de gráfico',
     #('Gráfico circular de sexo', 'Gráfico de barras por SEXO ', 'Gráfico de barras por DEPARTAMENTOS', "Gráfico de dispersión por FECHA DE RESULTADOS"))
#url del archivo en formato raw
url = 'https://raw.githubusercontent.com/DayanaHV/Programaci-n_avanzada/main/fallecidos_covid%20(3)%20(1).csv'
datos = pd.read_csv(url,sep= ',')
st.line_chart(data=datos, x='DEPARTAMENTO', y='EDAD_DECLARADA')
#---------------------------------------------------------------------------------------


option = st.selectbox(
     'Seleccione el tipo de gráfico',
     ('Gráfico de barras por PROVINCIA','Gráfico de barras por DEPARTAMENTOS','Gráfico de barras por SEXO'))

if option == "Gráfico de barras por DEPARTAMENTOS":
    st.subheader("Gráfico de barras por DEPARTAMENTOS")
    L = c[['DEPARTAMENTO', 'CLASIFICACION_DEF']].groupby('DEPARTAMENTO').count()
    st.bar_chart(L)
    st.write('Tu seleccionaste:', option)
elif option == "Gráfico de barras por SEXO":
    st.subheader("Gráfico de barras por SEXO")
    L = c[['SEXO', 'DEPARTAMENTO']].groupby('SEXO').count()
    st.bar_chart(L)
    st.write('Tu seleccionaste:', option)
elif option == "Gráfico de barras por PROVINCIA":
    st.subheader("Gráfico de barras por PROVINCIA")
    L = c[['PROVINCIA', 'CLASIFICACION_DEF']].groupby('PROVINCIA').count()
    st.bar_chart(L)
    st.write('Tu seleccionaste:', option)

#cont_DISTRITO = DISTRITO.iloc[:,6:].set_index(index)
#st.dataframe(cont_DISTRITO)
#st.subheader("Gráficos interactivos")
#st.line_chart(cont_DISTRITO)

#elif option == "Gráfico de barras por SEXO ":
   # st.subheader("Gráfico de barras por SEXO ")
    #tipo2=c["SEXO"].value_counts().FEMENINO
    #tipo3=c["SEXO"].value_counts().MASCULINO
    #b = (
        #Bar()
        #.add_xaxis(["FEMENINO", "MASCULINO"])
        #.add_yaxis(
            #"Casos positivos por sexo", [int(tipo2),int(tipo3)]
        #)
        #.set_global_opts(
            #title_opts=opts.TitleOpts(
                #title=" "
            #),
            #toolbox_opts=opts.ToolboxOpts(),
        #)
    #)
    #st_pyecharts(b)



#st.sidebar.header("Entradas del usuario")
#selected_SEXO=st.sidebar.selectbox('SEXO', ('FEMENINO','MASCULINO'))
