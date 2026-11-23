import streamlit as st
import pandas as pd
from service import Service

class ListarServicosAgendadosUI():
    def main():
        st.header("Lista de Serviços Agendados")
        horarios = Service.listar_servicos_agendados()
        
