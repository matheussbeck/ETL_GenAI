import streamlit as st
import contrato
from datetime import datetime

def main ():
    st.title("Sistema de CRM e Vendas da ZapFlow - FrontEnd Simples")
    email = st.text_input("Email do vendedor")
    data = st.date_input("Data da Venda")
    hora = st.time_input("Hora da Venda")
    valor = st.number_input("Valor da Venda")
    quantidade = st.number_input("Quantidade de Produtos")
    produto = st.selectbox("Produto Vendido", ['Zapflow com Gemini','Zapflow com ChatGPT','Zapflow com LLama 3.0'])
    
    if st.button("Salvar"):
        data_hora = datetime.combine(data,hora)
        st.write('**Dados da Venda')
        st.write(f'Email do vendedor: {email}')
        st.write(f'Data e Hora da Compra: {data_hora}')
        st.write(f'Valor da venda: {valor:.2f}')
        st.write(f'Quantidade de Produtos: {quantidade}')
        st.write(f'Produto vendido: {produto }')
    
if __name__ == "__main__":
    main()
    
