import os
from os import listdir
from os.path import isfile, join
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

with st.sidebar:
    opcion=st.selectbox(
        "Opción",
        ("DataSets","Fuente Original","Compilar","Entrenar","Guardar","Leer","Predecir","Matriz"))

if (opcion=="DataSets"):
    st.write("## Agente4D  Image to Image translation")
    st.write(opcion)
    col1, col2 = st.columns((2,2))
    with col1:
        st.write("## A")
    with col2:
        st.write("## B")

    imagenesA=[f for f in listdir('datasets/A') if not isfile(join(f))]
    for imagen in imagenesA:
        with col1:
            ruta=os.path.join('datasets/A/', imagen)
            img = Image.open(ruta)
            st.image(img, width=512)
        with col2:
            ruta=os.path.join('datasets/B/', imagen)
            try:
                img = Image.open(ruta)
                st.image(img, width=512)
            except IOError:
                st.write("Pendiente pos subir",ruta)
            
      
if (opcion=="Fuente Original"):
    st.write("## Agente4D  Image to Vector translation")
    st.write(opcion)
    col1, col2 = st.columns((2,2))
    with col1:
        st.write("Entrada")

    with col2:
        st.write("Salida")

    directorios=[f for f in listdir() if not isfile(join(f))]
    for directorio in directorios:
        if (directorio != ".git"):
            for archivo in listdir(directorio):
                nombre, extencion = os.path.splitext(archivo)
                if (extencion != ".htm" and extencion in [".gif", ".jpg", ".jpeg", ".bmp", ".png"]):
                    ruta=os.path.join(directorio, archivo)
                    img = Image.open(ruta)

                    col1, col2 = st.columns((2,2))
                    with col1:
                        st.image(img, width=512)

                    with col2:
                        nombrehtm=nombre+'.htm'
                        ruta=os.path.join(directorio, nombrehtm)
                        if os.path.isfile(ruta):
                            HtmlFile = open(ruta, 'r', encoding='utf-8')
                            html_string = HtmlFile.read() 
                            #st.markdown(html_string, unsafe_allow_html=True)
                            components.html(html_string, width=512, height=512)
                        else:
                            html_string = "Pendiente por subir" 
                            components.html(html_string, width=512, height=512)

if (opcion=="Compilar"):
    st.write(opcion)