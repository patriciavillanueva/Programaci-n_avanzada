importar streamlit como st
importar pandas como pd
importar numpy como np
importar altair como alt
importar urllib.request
importar base64
st.sidebar.header("Entradas del usuario")
año_seleccionado=st.sidebar.selectbox('Edad', list(reversed(range(0,117))))
st.header("Conjunto de datos FALLECIDOS COVID")
