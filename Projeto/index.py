from templates.manter_cliente_ui import ManterClienteUI
from templates.manter_servico_ui import ManterServicoUI
from templates.manter_horario_ui import ManterHorarioUI
from templates.manter_profissional_ui import ManterProfissionalUI
from templates.manter_atendimento_ui import ManterAtendimentoUI
from templates.abrir_conta_ui import AbrirContaUI
from templates.login_ui import LoginUI
from templates.perfil_cliente_ui import PerfilClienteUI
from templates.perfil_profissional_ui import PerfilProfissionalUI
from templates.perfil_admin_ui import PerfilAdminUI
from templates.agendar_servico_ui import AgendarServicoUI
from templates.abrir_minha_agenda_ui import AbrirMinhaAgendaUI
from templates.visualizar_meus_servicos_ui import VisualizarMeusServicosUI
from Projeto.templates.visualizar_minha_agenda_ui import VisualizarMinhaAgendaUI
from templates.confirmar_servico_ui import ConfirmarServicoUI
from templates.manter_endereco_ui import ManterEnderecoUI
from service import Service
import streamlit as st

class IndexUI:

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
    

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Meus Serviços"])
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "Agendar Serviço": AgendarServicoUI.main()
        if op == "Meus Serviços": VisualizarMeusServicosUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Abrir Agenda", "Minha Agenda", "Confirmar Servico"])
        if op == "Meus Dados": PerfilProfissionalUI.main()
        if op == "Abrir Agenda": AbrirMinhaAgendaUI.main()
        if op == "Minha Agenda": VisualizarMinhaAgendaUI.main()
        if op == "Confirmar Serviço": ConfirmarServicoUI.main()
        
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Clientes", "Serviços", "Horários", "Profissionais", "Atendimentos", "Endereços"])
        if op == "Meus Dados": PerfilAdminUI.main()
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Horários": ManterHorarioUI.main()
        if op == "Profissionais": ManterProfissionalUI.main()
        if op == "Atendimentos": ManterAtendimentoUI.main()
        if op == "Endereços" : ManterEnderecoUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            else:
                if st.session_state["usuario_tipo"] == "cliente": IndexUI.menu_cliente()
                else: IndexUI.menu_profissional()
            IndexUI.sair_do_sistema()
            
    def main():
        # verifica a existe o usuário admin
        Service.cliente_criar_admin()
        # monta o sidebar
        IndexUI.sidebar()

IndexUI.main()