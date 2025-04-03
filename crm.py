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

    if st.session_state.get("forcar_rerun"):
        st.session_state.forcar_rerun = False
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
            st.session_state.forcar_rerun = True
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
            st.experimental_rerun()
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
                    st.experimental_rerun()
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
        logradouro = st.text_input("Logradouro", value=cliente_atual.get("logradouro", ""))
        numero = st.text_input("Número", value=cliente_atual.get("numero", ""))
        complemento = st.text_input("Complemento", value=cliente_atual.get("complemento", ""))
        bairro = st.text_input("Bairro", value=cliente_atual.get("bairro", ""))
        municipio = st.text_input("Município", value=cliente_atual.get("municipio", ""))
        uf = st.text_input("Estado", value=cliente_atual.get("uf", ""))
        pais = st.text_input("País", value=cliente_atual.get("pais", "Brasil"))

        st.markdown("### Contato")
        responsavel = st.text_input("Nome do Responsável", value=cliente_atual.get("responsavel", ""))
        cargo = st.text_input("Cargo", value=cliente_atual.get("cargo", ""))
        telefone = st.text_input("Telefone", value=cliente_atual.get("telefone", ""))
        celular = st.text_input("Celular / WhatsApp", value=cliente_atual.get("celular", ""))
        email = st.text_input("Email", value=cliente_atual.get("email", ""))
        website = st.text_input("Website", value=cliente_atual.get("website", ""))

        st.markdown("### Preferências")
        forma_pagamento = st.selectbox("Forma de Pagamento", ["Boleto", "Transferência", "Cartão", "Pix"],
                                       index=["Boleto", "Transferência", "Cartão", "Pix"].index(cliente_atual.get("forma_pagamento", "Boleto")))
        indicador_presenca = st.selectbox("Presença do Comprador", ["Presencial", "Internet", "Telefone"],
                                          index=["Presencial", "Internet", "Telefone"].index(cliente_atual.get("indicador_presenca", "Presencial")))

        observacoes = st.text_area("Observações", value=cliente_atual.get("observacoes", ""))

        salvar = st.form_submit_button("Salvar")

    if salvar:
        novo = {
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

        if cliente_index is not None and cliente_index < len(todos):
            todos[cliente_index] = novo
            mensagem = "✅ Cliente atualizado com sucesso!"
        else:
            todos.append(novo)
            mensagem = "✅ Novo cliente cadastrado com sucesso!"

        salvar_clientes(todos)
        st.success(mensagem)
        st.session_state.forcar_rerun = True
