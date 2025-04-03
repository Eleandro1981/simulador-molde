# crm.py

import streamlit as st
import json
import os

CAMINHO_ARQUIVO = "clientes.json"

def salvar_cliente(cliente):
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "r") as f:
            dados = json.load(f)
    else:
        dados = []

    dados.append(cliente)

    with open(CAMINHO_ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

def carregar_clientes():
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "r") as f:
            return json.load(f)
    return []

def exibir_crm():
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

        submit = st.form_submit_button("Salvar Cliente")

    if submit:
        cliente = {
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
        salvar_cliente(cliente)
        st.success("✅ Cliente salvo com sucesso!")

    st.markdown("### 📋 Clientes Cadastrados")
    clientes = carregar_clientes()
    if clientes:
        for i, c in enumerate(clientes, 1):
            st.markdown(f"**{i}. {c['razao_social']}** – {c['cpf_cnpj']}")
    else:
        st.info("Nenhum cliente cadastrado ainda.")
