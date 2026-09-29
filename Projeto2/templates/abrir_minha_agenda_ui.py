import streamlit as st
from service import Service

class AbrirMinhaAgendaUI:
    def main():
        st.header("Abrir Minha Agenda")
        data = st.text_input("Infrome a data do formato dd/mm/aaaa")
        hora_inicio = st.text_input("Informe o horário inicial no formato HH:MM")
        hora_fim = st.text_input("Informe o horário final no formato HH:MM")
        intervalo = st.text_input("Informe o intervalo entre os horários (min)")
        if st.button("Abrir Agenda"):
            Service.horario_abrir_agenda(data, hora_inicio, hora_fim, int(intervalo), id_profissional)
            
                