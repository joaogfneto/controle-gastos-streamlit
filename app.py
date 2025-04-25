import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Controle de Gastos", layout="centered")
st.title("📊 Controle de Gastos Pessoais")

# Inicializa o DataFrame
if 'gastos' not in st.session_state:
    st.session_state.gastos = pd.DataFrame(columns=["Data", "Categoria", "Valor", "Forma de Pagamento", "Descrição"])

# Formulário para adicionar nova despesa
with st.form("formulario"):
    data = st.date_input("Data", value=date.today())
    categoria = st.selectbox("Categoria", ["Alimentação", "Transporte", "Lazer", "Saúde", "Outros"])
    valor = st.number_input("Valor (R$)", min_value=0.0, step=0.01)
    pagamento = st.selectbox("Forma de Pagamento", ["Dinheiro", "Crédito", "Débito", "Pix", "Outro"])
    descricao = st.text_input("Descrição")
    enviar = st.form_submit_button("Adicionar Gasto")

    if enviar:
        novo = pd.DataFrame([[data, categoria, valor, pagamento, descricao]],
                            columns=["Data", "Categoria", "Valor", "Forma de Pagamento", "Descrição"])
        st.session_state.gastos = pd.concat([st.session_state.gastos, novo], ignore_index=True)
        st.success("Gasto adicionado com sucesso!")

# Exibir gastos
st.subheader("📅 Histórico de Gastos")
st.dataframe(st.session_state.gastos)

# Total
total = st.session_state.gastos["Valor"].sum()
st.subheader(f"💰 Total gasto: R$ {total:.2f}")
