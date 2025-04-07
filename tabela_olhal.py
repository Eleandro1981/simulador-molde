import streamlit as st
import pandas as pd

def exibir_tabela_olhal():
    st.subheader("🧱 Tabela - Olhal de Içamento")

    # Exemplo de tabela (substitua pelos dados reais e arquivos que você tiver)
    dados = [
        {"Parafuso": "M8", "D": "20", "d": "8", "Download .x_t": "olhal_m8.x_t", "Download .step": "olhal_m8.step"},
        {"Parafuso": "M10", "D": "25", "d": "10", "Download .x_t": "olhal_m10.x_t", "Download .step": "olhal_m10.step"},
        {"Parafuso": "M12", "D": "30", "d": "12", "Download .x_t": "olhal_m12.x_t", "Download .step": "olhal_m12.step"},
        # Adicione mais linhas conforme a tabela real
    ]

    df = pd.DataFrame(dados)

    st.markdown("**Clique para baixar o modelo 3D do componente:**")
    for i, row in df.iterrows():
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 2, 2])
        col1.write(row["Parafuso"])
        col2.write(row["D"])
        col3.write(row["d"])
        col4.download_button(
            label=".x_t",
            data=open(f"arquivos_3d/{row['Download .x_t']}", "rb"),
            file_name=row['Download .x_t'],
            mime="application/octet-stream",
            key=f"x_t_{i}"
        )
        col5.download_button(
            label=".step",
            data=open(f"arquivos_3d/{row['Download .step']}", "rb"),
            file_name=row['Download .step'],
            mime="application/octet-stream",
            key=f"step_{i}"
        )
