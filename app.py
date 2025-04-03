import streamlit as st
import numpy as np
import trimesh
from scipy.interpolate import RegularGridInterpolator

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

    with st.form("formulario_cliente"):
        tipo_pessoa = st.selectbox("Tipo de Pessoa", ["Jurídica", "Física"])
        razao_social = st.text_input("Razão Social / Nome Completo")
        nome_fantasia = st.text_input("Nome Fantasia (opcional)")
        cpf_cnpj = st.text_input("CNPJ / CPF")
        ie = st.text_input("Inscrição Estadual")
        isento_ie = st.checkbox("Isento de IE")
        im = st.text_input("Inscrição Municipal (opcional)")
        cnae = st.text_input("CNAE (opcional)")
        regime_tributario = st.selectbox("Regime Tributário", ["Simples Nacional", "Lucro Presumido", "Lucro Real"])
        indicador_ie = st.selectbox("Indicador de IE", ["Contribuinte", "Isento", "Não contribuinte"])

        st.markdown("### Endereço")
        cep = st.text_input("CEP")
        logradouro = st.text_input("Logradouro")
        numero = st.text_input("Número")
        complemento = st.text_input("Complemento")
        bairro = st.text_input("Bairro")
        municipio = st.text_input("Município")
        uf = st.text_input("Estado (UF)")
        pais = st.text_input("País", value="Brasil")

        st.markdown("### Contato")
        responsavel = st.text_input("Nome do Responsável")
        cargo = st.text_input("Cargo / Função")
        telefone = st.text_input("Telefone Fixo")
        celular = st.text_input("Celular / WhatsApp")
        email = st.text_input("E-mail")
        website = st.text_input("Website (opcional)")

        st.markdown("### Preferências de Faturamento")
        forma_pagamento = st.selectbox("Forma de Pagamento Padrão", ["Boleto", "Transferência", "Cartão", "Pix"])
        indicador_presenca = st.selectbox("Presença do Comprador", ["Presencial", "Internet", "Telefone"])

        st.markdown("### Observações")
        observacoes = st.text_area("Notas internas ou observações adicionais")
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
