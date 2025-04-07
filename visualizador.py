import streamlit as st
from st3d import st_3d_viewer
import os

def exibir_visualizador():
    st.subheader("🧊 Visualizador 3D - Arquivos STL")

    # Lista os arquivos STL disponíveis
    arquivos = [f for f in os.listdir("arquivos_3d") if f.endswith(".stl")]

    if not arquivos:
        st.warning("Nenhum arquivo STL encontrado na pasta 'arquivos_3d'.")
        return

    # Dropdown para o usuário escolher o arquivo
    selecionado = st.selectbox("Selecione um arquivo STL para visualizar:", arquivos)

    caminho = os.path.join("arquivos_3d", selecionado)

    # Visualização 3D
    st_3d_viewer(caminho)
