# crm.py

import streamlit as st
import json
import os

CAMINHO_ARQUIVO = "clientes.json"

# Carregar dados
def carregar_clientes():
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "r") as f:
            return json.load(f)
    return []

# Salvar todos os dados
def salvar_clientes(lista):
    with open(CAMINHO_ARQUIVO, "w") as f:
        json.dump(lista, f, indent=4)

def exibir_crm():
    st.subheader("👥 Cadastro de Clientes")

    clientes = carregar_clientes()

    # 🔍 Campo de busca
    busca = st.text_input("🔍 Buscar cliente por nome ou CPF/CNPJ")

    if busca:
        clientes = [c for c in clientes if busca.lower() in c["razao_social"].lower() or busca.lower() in c["cpf_cnpj"].lower()]

    # Verifica se estamos editando
    cliente_index = st.session_state.get("editar_index", None)
    cliente_edicao = clientes[cliente_index] if cliente_index is not None and cliente_index < len(clientes) else {}

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
        cargo = st.text_input("Cargo / Função", value=cliente_edicao.get("cargo", ""))
        telefone = st.text_input("Telefone Fixo", value=cliente_edicao.get("telefone", ""))
        celular = st.text_input("Celular / WhatsApp", value=cliente_edicao.get("celular", ""))
        email = st.text_input("E-mail", value=cliente_edicao.get("email", ""))
        website = st.text_input("Website (opcional)", value=cliente_edicao.get("website", ""))

        st.markdown("### Preferências de Faturamento")
        forma_pagamento = st.selectbox("Forma de Pagamento Padrão", ["Boleto", "Transferência", "Cartão", "Pix"],
                                       index=["Boleto", "Transferência", "Cartão", "Pix"].index(cliente_edicao.get("forma_pagamento", "Boleto")))
        indicador_presenca = st.selectbox("Presença do Comprador", ["Presencial", "Internet", "Telefone"],
                                          index=["Presencial", "Internet", "Telefone"].index(cliente_edicao.get("indicador_presenca", "Presencial")))

        st.markdown("### Observações")
        observacoes = st.text_area("Notas internas ou observações adicionais", value=cliente_edicao.get("observacoes", ""))

        if cliente_index is not None:
            submit = st.form_submit_button("Salvar Alterações")
        else:
            submit = st.form_submit_button("Salvar Novo Cliente")

    if submit:
        cliente_novo = {
            "tipo_pessoa": tipo_pessoa,
            "razao_social": razao_social,
            "nome_fantasia": nome_fantasia,
            "cpf_cnpj": cpf_cnpj,
            "ie": ie,
            "isento_ie": isento_ie,
            "im": im,
            "cnae": cnae,
            "regime_tributario": regime_tributario,
            "indicador_ie": indicador_ie,
            "cep": cep,
            "logradouro": logradouro,
            "numero": numero,
            "complemento": complemento,
            "bairro": bairro,
            "municipio": municipio,
            "uf": uf,
            "pais": pais,
            "responsavel": responsavel,
            "cargo": cargo,
            "telefone": telefone,
            "celular": celular,
            "email": email,
            "website": website,
            "forma_pagamento": forma_pagamento,
            "indicador_presenca": indicador_presenca,
            "observacoes": observacoes
        }

        todos = carregar_clientes()
        if cliente_index is not None:
            todos[cliente_index] = cliente_novo
            st.session_state.editar_index = None
            st.success("✅ Cliente editado com sucesso!")
        else:
            todos.append(cliente_novo)
            st.success("✅ Novo cliente salvo com sucesso!")

        salvar_clientes(todos)

    st.markdown("### 📋 Clientes Cadastrados")

    if not clientes:
        st.info("Nenhum cliente encontrado.")
    else:
        for i, c in enumerate(clientes):
            col1, col2, col3 = st.columns([6, 1, 1])
            with col1:
                st.markdown(f"**{i+1}. {c['razao_social']}** – {c['cpf_cnpj']}")
            with col2:
                if st.button("✏️ Editar", key=f"edit_{i}"):
                    st.session_state.editar_index = i
                    st.experimental_rerun()
            with col3:
                if st.button("🗑️ Excluir", key=f"delete_{i}"):
                    todos = carregar_clientes()
                    if i < len(todos):
                        nome = todos[i]["razao_social"]
                        todos.pop(i)
                        salvar_clientes(todos)
                        st.success(f"❌ Cliente '{nome}' excluído com sucesso!")
                        st.experimental_rerun()
