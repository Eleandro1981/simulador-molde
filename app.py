import streamlit as st
from simulador_inj import exibir_simulador_inj
from crm_cadastro_cliente import exibir_crm_cadastro_cliente

st.set_page_config(page_title="App de Moldes", layout="wide")
st.title("🛠️ Plataforma de Projetos de Moldes")

menu = st.sidebar.radio("Navegar entre os módulos:", [
    "Simulador de Injeção",
    "CRM - Cadastro de Clientes",
    "Orçamento de Moldes",
    "Checklist de Projeto",
    "Tabelas de Componentes",
    "Configurações"
])

if menu == "Simulador de Injeção":
    exibir_simulador_inj()

elif menu == "CRM - Cadastro de Clientes":
    exibir_crm_cadastro_cliente()

elif menu == "Orçamento de Moldes":
    st.subheader("📦 Orçamento de Moldes")
    st.write("Em breve: cálculo de custos, margens e geração de proposta.")

elif menu == "Checklist de Projeto":
    st.subheader("✅ Checklist de Projeto")
    st.write("Em breve: verificação de itens essenciais antes da fabricação.")

elif menu == "Tabelas de Componentes":
    st.subheader("🧱 Tabelas de Componentes")
    st.write("Em breve: consulta a componentes com visualização 3D.")

elif menu == "Configurações":
    st.subheader("⚙️ Configurações")
    st.write("Ajustes gerais do sistema, preferências e dados da empresa.")

