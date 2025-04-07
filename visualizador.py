import streamlit as st
from streamlit_vtkjs import st_vtkjs
import os

def exibir_visualizador():
    st.subheader("🧊 Visualizador 3D - Arquivos STL")

    arquivos = [f for f in os.listdir("arquivos_3d") if f.endswith(".stl")]

    if not arquivos:
        st.warning("Nenhum arquivo STL encontrado.")
        return

    escolhido = st.selectbox("Selecione o arquivo STL:", arquivos)

    caminho = os.path.join("arquivos_3d", escolhido)
    
    with open(caminho, "rb") as f:
        st_vtkjs(file=f.read())
