import streamlit as st
import pandas as pd
import os

def exibir_tabela_olhal():
    st.subheader("🧱 Tabela - Olhal de Içamento")

    dados = [
        {"Parafuso": "M8", "D": "20", "d": "8", "Download .x_t": "olhal_m8.x_t", "Download .step": "olhal_m8.step"},
        {"Parafuso": "M10", "D": "25", "d": "10", "Download .x_t": "olhal_m10.x_t", "Download .step": "olhal_m10.step"},
        {"Parafuso": "M12", "D": "30", "d": "12", "Download .x_t": "olhal_m12.x_t", "Download .step": "olhal_m12.step"}
    ]

    df = pd.DataFrame(dados)

    st.markdown("**Clique para baixar o modelo 3D do componente:**")

    for i, row in df.iterrows():
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 2, 2])
        col1.write(row["Parafuso"])
        col2.write(row["D"])
        col3.write(row["d"])

        xt_path = os.path.join("arquivos_3d", row["Download .x_t"])
        step_path = os.path.join("arquivos_3d", row["Download .step"])

        if os.path.exists(xt_path):
            with open(xt_path, "rb") as f:
                col4.download_button(
                    label=".x_t",
                    data=f,
                    file_name=row["Download .x_t"],
                    mime="application/octet-stream",
                    key=f"x_t_{i}"
                )
        else:
            col4.write("❌")

        if os.path.exists(step_path):
            with open(step_path, "rb") as f:
                col5.download_button(
                    label=".step",
                    data=f,
                    file_name=row["Download .step"],
                    mime="application/octet-stream",
                    key=f"step_{i}"
                )
        else:
            col5.write("❌")
