import streamlit as st
import json
import os

CAMINHO_ARQUIVO = "clientes.json"

def carregar_clientes():
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_clientes(lista):
    with open(CAMINHO_ARQUIVO, "w") as f:
        json.dump(lista, f, indent=4)

def exibir_crm():
    st.subheader("👥 Cadastro de Clientes")

    if "forcar_rerun" not in st.session_state:
        st.session_state["forcar_rerun"] = False
    if st.session_state["forcar_rerun"]:
        st.session_state["forcar_rerun"] = False
        st.experimental_rerun()

    if "editar_index" not in st.session_state:
        st.session_state.editar_index = None
    if "mostrar_busca" not in st.session_state:
        st.session_state.mostrar_busca = False

    todos = carregar_clientes()
    cliente_index = st.session_state.editar_index
    cliente_atual = todos[cliente_index] if cliente_index is not None and cliente_index < len(todos) else {}

    # Painel de botões
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        if st.button("🆕 Novo"):
            st.session_state.editar_index = None
            st.session_state["forcar_rerun"] = True
    with col2:
        if st.button("🔍 Pesquisar"):
            st.session_state.mostrar_busca = not st.session_state.mostrar_busca
    with col3:
        if st.button("◀️ Anterior") and cliente_index not in [None, 0]:
            st.session_state.editar_index -= 1
            st.experimental_rerun()
    with col4:
        if st.button("▶️ Próximo") and cliente_index is not None and cliente_index + 1 < len(todos):
            st.session_state.editar_index += 1
            st.experimental_rerun()
    with col5:
        if st.button("🗑️ Excluir") and cliente_index is not None:
            nome = todos[cliente_index]["razao_social"]
            todos.pop(cliente_index)
            salvar_clientes(todos)
            st.success(f"❌ Cliente '{nome}' excluído com sucesso!")
            st.session_state.editar_index = None
            st.session_state["forcar_rerun"] = True
    with col6:
        st.button("📄 Relatório (em breve)")

    # Campo de busca
    if st.session_state.mostrar_busca:
        busca = st.text_input("Digite um nome ou CPF/CNPJ para buscar")
        if busca:
            resultados = [
                (i, c) for i, c in enumerate(todos)
                if busca.lower() in c["razao_social"].lower() or busca.lower() in c["cpf_cnpj"].lower()
            ]
            for i, c in resultados:
                st.markdown(f"**{c['razao_social']}** – {c['cpf_cnpj']}")
                if st.button("Selecionar", key=f"sel_{i}"):
                    st.session_state.editar_index = i
                    st.session_state["forcar_rerun"] = True
        else:
            st.info("Digite algo para buscar.")
        st.markdown("---")

    # Formulário
    with st.form("formulario_cliente"):
        tipo_pessoa = st.selectbox("Tipo de Pessoa", ["Jurídica", "Física"], index=0 if cliente_atual.get("tipo_pessoa") == "Jurídica" else 1)
        razao_social = st.text_input("Razão Social / Nome Completo", value=cliente_atual.get("razao_social", ""))
        nome_fantasia = st.text_input("Nome Fantasia", value=cliente_atual.get("nome_fantasia", ""))
        cpf_cnpj = st.text_input("CNPJ / CPF", value=cliente_atual.get("cpf_cnpj", ""))
        ie = st.text_input("Inscrição Estadual", value=cliente_atual.get("ie", ""))
        isento_ie = st.checkbox("Isento de IE", value=cliente_atual.get("isento_ie", False))
        im = st.text_input("Inscrição Municipal", value=cliente_atual.get("im", ""))
        cnae = st.text_input("CNAE", value=cliente_atual.get("cnae", ""))
        regime_tributario = st.selectbox("Regime Tributário", ["Simples Nacional", "Lucro Presumido", "Lucro Real"],
                                         index=["Simples Nacional", "Lucro Presumido", "Lucro Real"].index(cliente_atual.get("regime_tributario", "Simples Nacional")))
        indicador_ie = st.selectbox("Indicador de IE", ["Contribuinte", "Isento", "Não contribuinte"],
                                    index=["Contribuinte", "Isento", "Não contribuinte"].index(cliente_atual.get("indicador_ie", "Contribuinte")))

        st.markdown("### Endereço")
        cep = st.text_input("CEP", value=cliente_atual.get("cep", ""))
        logradouro = st.text_input("Logradouro", value=cliente_atual.get("logradouro", "
