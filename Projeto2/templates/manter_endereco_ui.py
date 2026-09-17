import streamlit as st
import pandas as pd
import time
from service import Service

class ManterEnderecoUI:
    def main():
        st.header("Cadastro de Endereços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterEnderecoUI.listar()
        with tab2: ManterEnderecoUI.inserir()
        with tab3: ManterEnderecoUI.atualizar()
        with tab4: ManterEnderecoUI.excluir()
    def listar():
        enderecos = Service.endereco_listar()
        if len(enderecos) == 0: st.write("Nenhum endereço cadastrado")
        else:
            list_dic = []
            for obj in enderecos: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        nome = st.text_input("Informe o nome")
        endereco = st.text_input("Informe o endereço")
        id_cliente = st.text_input("Informe o id_cliente")
        if st.button("Inserir"):
            Service.endereco_inserir(nome, endereco, id_cliente)
            st.success("Endereço inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        enderecos = Service.endereco_listar()
        if len(enderecos) == 0: st.write("Nenhum endereco cadastrado")
        else:
            op = st.selectbox("Atualização de Endereços", enderecos)
            nome = st.text_input("Novo nome", op.get_nome())
            endereco = st.text_input("Novo endereço", op.get_endereco())
            id_cliente = st.text_input("Novo id_cliente", op.get_id_cliente())
            if st.button("Atualizar"):
                id = op.get_id()
                Service.endereco_atualizar(id, nome, endereco, id_cliente)
                st.success("Endereço atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    def excluir():
        enderecos = Service.endereco_listar()
        if len(enderecos) == 0: st.write("Nenhum endereço cadastrado")
        else:
            op = st.selectbox("Exclusão de Endereços", enderecos)
            if st.button("Excluir"):
                id = op.get_id()
                Service.endereco_excluir(id)
                st.success("Endereço excluído com sucesso")
                time.sleep(2)
                st.rerum()
