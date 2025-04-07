import streamlit as st
import pandas as pd
import os

def exibir_tabela_olhal():
    st.subheader("🧱 Tabela - Olhal de Içamento")

    # Exibe a imagem técnica
    st.image("arquivos_3d/Olhal.jpg", caption="Desenho técnico do Olhal", use_container_width=True)

    # Carrega a planilha
    df = pd.read_excel("arquivos_3d/Tabela Olhal.xlsx")

    # Remove linhas sem nome (geralmente a primeira, se estiver vazia)
    df = df.dropna(subset=["Nome"])

    st.markdown("**Clique para baixar os modelos 3D:**")

    for i, row in df.iterrows():
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 1, 2, 2])

        col1.write(row["Nome"])
        col2.write(row["Rosca"])
        col3.write(f'{row["Peso - Kg"]:.3f} kg')
        col4.write(f'{row["Carga -T"]:.0f} kgf')

        xt_name = f"olhal_{row['Nome'].lower()}.x_t"
        stp_name = f"olhal_{row['Nome'].lower()}.stp"

        xt_path = os.path.join("arquivos_3d", xt_name)
        stp_path = os.path.join("arquivos_3d", stp_name)

        if os.path.exists(xt_path):
            with open(xt_path, "rb") as f:
                col6.download_button(
                    label=".x_t",
                    data=f,
                    file_name=xt_name,
                    mime="application/octet-stream",
                    key=f"x_t_{i}"
                )
        else:
            col6.write("❌")

        if os.path.exists(stp_path):
            with open(stp_path, "rb") as f:
                col7.download_button(
                    label=".stp",
                    data=f,
                    file_name=stp_name,
                    mime="application/octet-stream",
                    key=f"stp_{i}"
                )
        else:
            col7.write("❌")
