
import streamlit as st
from motor import generar_proyecto

st.title("BI Generator (Test)")

necesidad = st.text_input("Describe tu necesidad")
archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

if st.button("Generar"):
    if archivo is not None:
        with open("input.xlsx", "wb") as f:
            f.write(archivo.getbuffer())

        generar_proyecto(necesidad, "input.xlsx")

        st.success("Proyecto generado en carpeta output_pbip")
    else:
        st.error("Sube un archivo primero")
