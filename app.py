import streamlit as st

# Configuração da página
st.set_page_config(page_title="App de Moldes", layout="wide")

# Título principal
st.title("🛠️ Plataforma de Projetos de Moldes")

# Menu lateral
menu = st.sidebar.radio("Navegar entre os módulos:", [
    "Simulador de Injeção",
    "CRM - Cadastro de Clientes",
    "Orçamento de Moldes",
    "Checklist de Projeto",
    "Tabelas de Componentes",
    "Configurações"
])

# Exibe o conteúdo da seção escolhida
if menu == "Simulador de Injeção":
    st.subheader("🧠 Simulador de Injeção")
    st.write("Aqui entra o código do simulador de força de fechamento...")

elif menu == "CRM - Cadastro de Clientes":
    st.subheader("👥 Cadastro de Clientes")
    st.write("Aqui você poderá cadastrar e consultar seus clientes.")
    # Em breve vamos adicionar o formulário aqui

elif menu == "Orçamento de Moldes":
    st.subheader("📦 Orçamento de Moldes")
    st.write("Em breve: cálculo de custos, margens e geração de proposta.")

elif menu == "Checklist de Projeto":
    st.subheader("✅ Checklist de Projeto")
    st.write("Em breve: verificação de itens essenciais antes da fabricação.")

elif menu == "Tabelas de Components":
    st.subheader("🧱 Tabelas de Componentes")
    st.write("Em breve: consulta a componentes com visualização 3D.")

elif menu == "Configurações":
    st.subheader("⚙️ Configurações")
    st.write("Ajustes gerais do sistema, preferências e dados da empresa.")
