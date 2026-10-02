import streamlit as st
import pandas as pd
from service import Service
import time
from datetime import datetime

class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    def listar():
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios:
                cliente = Service.cliente_listar_id(obj.get_id_cliente())
                servico = Service.servico_listar_id(obj.get_id_servico())
                profissional = Service.servico_listar_id(obj.get_id_profissional())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_descricao()
                if profissional != None: profissional = profissional.get_nome()
                dic.append({"id" : obj.get_id(), "data" : obj.get_data(), "confirmado" : obj.get_confirmado(),
                            "cliente" : cliente, "servico" : servico, "profissional": profissional})
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        clientes = Service.cliente_listar()
        servicos = Service.servico_listar()
        profissionais = Service.profissional_listar()
        data = st.text_input("Informe a data e o horário do serviço", datetime.now().strftime("%d/%m/%Y %H:%M"))
        confirmado = st.checkbox("Confirmado")
        cliente = st.selectbox("Informe o cliente", clientes, index = None)
        servico = st.selectbox("Informe o serviço", servicos, index = None)
        profissional = st.selectbox("Informe p profissionsl", profissionais, index = None)
        if st.button("Inserir"):
            id_cliente = None
            id_servico = None
            id_profissional = None
            if cliente != None: id_cliente = cliente.get_id()
            if servico != None: id_servico = servico.get_id()
            if profissional != None: id_profissional = profissional.get_id()
            Service.horario_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico, id_profissional)
            st.success("Horário inserido com sucesso")
            time.sleep(2)