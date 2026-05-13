class Musica:
    def __init__(self, id, titulo, artista, album):
        self.__id = id
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album

    def get_id(self):
        return self.__id
    
    def get_titulo(self):
        return self.__titulo
    
    def get_artista(self):
        return self.__artista
    
    def get_album(self):
        return self.__album
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_artista(self, artista):
        self.__artista = artista

    def set_album(self, album):
        self.__album = album

    def __str__(self):
        return f"{self.__titulo} - {self.__artista} - {self.__album}"
    
    
class Playlist:
    def __init__(self, id, nome, descricao):
        self.__id = id
        self.__nome = nome 
        self.__descricao = descricao

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_descricao(self):
        return self.__descricao
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def __str__(self):
        return f"{self.__nome} - {self.__descricao}"
    

class PlaylistItem:
    def __init__(self, id, id_playlist, id_musica, sequencia):
        self.__id = id
        self.__id_playlist = id_playlist 
        self.__id_musica = id_musica
        self.__sequencia = sequencia

    def get_id(self):
        return self.__id
    
    def get_id_playlist(self):
        return self.__id_playlist
    
    def get_id_musica(self):
        return self.__id_musica
    
    def get_sequencia(self):
        return self.__sequencia
    
    def set_id_playlist(self, id_playlist):
        self.__id_playlist = id_playlist

    def set_id_musica(self, id_musica):
        self.__id_musica = id_musica

    def set_sequencia(self, sequencia):
        self.__sequencia = sequencia

    def __str__(self):
        return f"Item: {self.__id} - Playlist: {self.__id_playlist} - Música: {self.__id_musica} - Ordem: {self.__sequencia}"
    

class UI:
    playlist = []
    musicas = []
    itens = []

    @staticmethod
    def main():
        op = 0
        while op != 13:
            op = UI.menu()
            if op == 1: UI.inserir_playlist()
            if op == 2: UI.listar_playlist()
            if op == 3: UI.atualizar_playlist()
            if op == 4: UI.excluir_playlist()
            if op == 5: UI.inserir_musica()
            if op == 6: UI.listar_musicas()
            if op == 7: UI.atualizar_musica()
            if op == 8: UI.excluir_musica()
            if op == 9: UI.inserir_item()
            if op == 10: UI.listar_itens()
            if op == 11: UI.listar_musicas_playlist()
            if op == 12: UI.reordeenar_musica()
    
    @staticmethod
    def menu():
        print("1-Inserir Playlist 2-Listar Playlists 3-Atualizar Playlists 4-Excluir Playlist 5-Inserir Música 6-Listar Músicas 7-Atualizar Música 8-Excluir Música 9-Inserir Música na Playlist 10-Listar Itens da Playlist 11=Listar Músicas de uma Playlist 12-Alterar Ordem da Música 13-Sair")
        return int(input("Escolha uma opção: "))
    
    @staticmethod
    def inserir_playlist():
        id = int(input("ID: "))
        nome