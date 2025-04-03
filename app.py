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
st.set_page_config(page_title="Simulador de Força de Fechamento", layout="centered")
st.title("🔩 Simulador de Força de Fechamento de Molde")

# Tabela de pressão
espessuras_ref = np.array([0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3,
                           1.4, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.5, 4.0, 4.5, 5.0])
betas = np.array([50, 75, 100, 150, 200, 250])
pressao_tabela = np.array([
    [270, 240, 220, 200, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180],
    [400, 375, 325, 300, 270, 240, 220, 200, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180],
    [480, 450, 400, 370, 340, 300, 290, 280, 250, 230, 210, 190, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180],
    [720, 670, 580, 530, 480, 440, 425, 400, 375, 360, 340, 320, 260, 220, 210, 180, 180, 180, 180, 180, 180, 180],
    [900, 850, 750, 720, 700, 630, 580, 520, 500, 450, 430, 410, 360, 320, 290, 260, 240, 220, 180, 180, 180, 180],
    [1050,1000, 900, 850, 800, 700, 660, 620, 560, 530, 500, 480, 420, 360, 330, 300, 275, 250, 225, 200, 180, 180]
])
interpolador_pressao = RegularGridInterpolator((betas, espessuras_ref), pressao_tabela, method='linear', bounds_error=False, fill_value=None)

# Fatores por material
fatores_materiais = {
    "PE": 1.00, "PP": 1.00, "PS": 1.00,
    "ABS": 1.35, "SAN": 1.35,
    "PA": 1.30, "SB": 1.30,
    "PMMA": 1.60, "PPO": 1.60,
    "CA": 1.40, "PC": 1.85, "PVC": 1.85
}

# Upload
st.subheader("1. Envie seu arquivo STL")
arquivo = st.file_uploader("Arquivo STL", type=['stl'])

if arquivo:
    mesh = trimesh.load(arquivo, file_type='stl')

    st.subheader("2. Selecione o material")
    material = st.selectbox("Material", list(fatores_materiais.keys()))

    st.subheader("3. Informe a espessura da parede (mm)")
    esp = st.number_input("Espessura (mm)", min_value=0.1, max_value=10.0, value=2.0, step=0.1)

    if st.button("Calcular"):
        fluxo = np.max(np.linalg.norm(mesh.vertices, axis=1))
        beta = fluxo / esp
        beta = np.clip(beta, betas.min(), betas.max())
        base = interpolador_pressao([[beta, esp]])[0]
        fator = fatores_materiais.get(material.upper(), 1.0)
        pressao = (base * fator) / 10.1972
        area_proj = mesh.area_faces[mesh.face_normals[:, 2] > 0.9].sum()
        forca_kgf = (area_proj * pressao) / 1000
        forca_ton = forca_kgf / 10

        st.success("Cálculo finalizado com sucesso!")
        st.write(f"📏 Espessura informada: **{esp:.2f} mm**")
        st.write(f"📐 Comprimento de fluxo estimado: **{fluxo:.2f} mm**")
        st.write(f"🧲 Área projetada estimada: **{area_proj:.2f} mm²**")
        st.write(f"🔥 Pressão de injeção estimada: **{pressao:.2f} MPa**")
        st.write(f"💪 Força de fechamento estimada: **{forca_ton:.2f} toneladas-força**")

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
