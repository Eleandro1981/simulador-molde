import streamlit as st
import json
import os

CAMINHO_ARQUIVO = "clientes.json"

# Carregar todos os clientes
def carregar_clientes():
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "r") as f:
            return json.load(f)
    return []

# Salvar todos os clientes
def salvar_clientes(lista):
    with open(CAMINHO_ARQUIVO, "w") as f:
        json.dump(lista, f, indent=4)

# Exibir formulário e lista
def exibir_crm():
    st.subheader("👥 Cadastro de Clientes")

    # Todos os clientes
    todos = carregar_clientes()

    # 🔍 Campo de busca
    busca = st.text_input("🔍 Buscar cliente por nome ou CPF/CNPJ")

    # Identificador do cliente sendo editado
    cliente_index = st.session_state.get("editar_index", None)

    # Filtrar clientes se tiver busca
    if busca:
        clientes_filtrados = [
            (i, c) for i, c in enumerate(todos)
            if busca.lower() in c["razao_social"].lower() or busca.lower() in c["cpf_cnpj"].lower()
        ]
    else:
        clientes_filtrados = list(enumerate(todos))

    # Dados do cliente em edição
    cliente_edicao = todos[cliente_index] if cliente_index is not None and cliente_index < len(todos) else {}

    # Formulário
    with st.form("formulario_cliente"):
        tipo_pessoa = st.selectbox("Tipo de Pessoa", ["Jurídica", "Física"], index=0 if cliente_edicao.get("tipo_pessoa") == "Jurídica" else 1 if cliente_edicao else 0)
        razao_social = st.text_input("Razão Social / Nome Completo", value=cliente_edicao.get("razao_social", ""))
        nome_fantasia = st.text_input("Nome Fantasia (opcional)", value=cliente_edicao.get("nome_fantasia", ""))
        cpf_cnpj = st.text_input("CNPJ / CPF", value=cliente_edicao.get("cpf_cnpj", ""))
        ie = st.text_input("Inscrição Estadual", value=cliente_edicao.get("ie", ""))
        isento_ie = st.checkbox("Isento de IE", value=cliente_edicao.get("isento_ie", False))
        im = st.text_input("Inscrição Municipal (opcional)", value=cliente_edicao.get("im", ""))
        cnae = st.text_input("CNAE (opcional)", value=cliente_edicao.get("cnae", ""))
        regime_tributario = st.selectbox("Regime Tributário", ["Simples Nacional", "Lucro Presumido", "Lucro Real"],
                                         index=["Simples Nacional", "Lucro Presumido", "Lucro Real"].index(cliente_edicao.get("regime_tributario", "Simples Nacional")))
        indicador_ie = st.selectbox("Indicador de IE", ["Contribuinte", "Isento", "Não contribuinte"],
                                    index=["Contribuinte", "Isento", "Não contribuinte"].index(cliente_edicao.get("indicador_ie", "Contribuinte")))

        st.markdown("### Endereço")
        cep = st.text_input("CEP", value=cliente_edicao.get("cep", ""))
        logradouro = st.text_input("Logradouro", value=cliente_edicao.get("logradouro", ""))
        numero = st.text_input("Número", value=cliente_edicao.get("numero", ""))
        complemento = st.text_input("Complemento", value=cliente_edicao.get("complemento", ""))
        bairro = st.text_input("Bairro", value=cliente_edicao.get("bairro", ""))
        municipio = st.text_input("Município", value=cliente_edicao.get("municipio", ""))
        uf = st.text_input("Estado (UF)", value=cliente_edicao.get("uf", ""))
        pais = st.text_input("País", value=cliente_edicao.get("pais", "Brasil"))

        st.markdown("### Contato")
        responsavel = st.text_input("Nome do Responsável", value=cliente_edicao.get("responsavel", ""))
        cargo = st.text_input("Cargo / Função", value=cliente_edicao.get("cargo", "
