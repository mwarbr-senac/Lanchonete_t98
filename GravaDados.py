import builtins
import json # JavaScript Object Notation


class GravaDados:
    
    # atributo/variável vazio (GLOBAL)
    usuariosJson = None
    
    def __init__(self):
        self.carregaJson()
    
    def carregaArquivo( self ):
        
        with builtins.open( "textos.txt", "r" ) as dados:
            for linha in dados:
                print( linha.rstrip() )
                
    def carregaJson( self ):
        
        with open( "usuarios.json", "r" ) as dados:
            
            # recuperando os dados do JSON
            dadosJson = json.load( dados )
            
            # retornamos os dados para que outra função utilize de forma direta
            self.usuariosJson = dadosJson
            
            # print( f" Usuário: { dadosJson[0]["loginArmazenado"] } e a senha { dadosJson[0]["senhaArmazenada"] } " )
            
    def cadastraUsuario( self, novoUsuario ):
        # pegamos os dados da variável global
        usuariosCadastrados = self.usuariosJson

        # salva o novo usuario no vetor
        usuariosCadastrados.append( novoUsuario )

        # abrir o arquivo Json e escreveros dados atualizados nele
        with open( "usuarios.json", "w" ) as dados:
            # coloca os dados em formato Json
            json.dump( usuariosCadastrados, dados, indent=4  )
            # fecha o arquivo
            dados.close()
            
            #tela = Telas()
            
            # exibir a tela da classe Telas()
            #tela.mensagensSistema( "Cadastro Realizado com sucesso!!" )

    def recuperaUsuario( self, buscar ):
        # busca o item do arquivo json escolhido
        # a programação executa apenas um item por vez, para processar mais itens usamos um laço de repetição - for
        for i, item in enumerate( self.usuariosJson  ):
            # vamos comparar o nome de usuário para o filtro
            if item["loginArmazenado"] == buscar:
                return item
            else:
                # se não achou nada retorna a mensagem
                print("Nenhum usuário encontrado!")
                break
            
    def apagaUsuario( self, login ):
        
        dadosArmazenados = self.usuariosJson
        
        for i, item in enumerate( dadosArmazenados ):
            if item["loginArmazenado"] == login:
                del dadosArmazenados[i]
                break
            
        with open( "usuarios.json", "w" ) as dados:
            
            json.dump( dadosArmazenados, dados )
            
            dados.close()
            
            print("Usuário apagado com sucesso!")
            
    def ordenaBusca( self, ordenarPor = "loginArmazenado", ordemReversa=False ):
        
        return sorted( self.usuariosJson, key=lambda item: item[ ordenarPor], reverse=ordemReversa )

# teste = Testes()

# escolhido = teste.recuperaUsuario( " cliente " )

# print( escolhido )

#  novoUsuario = {
#     "loginArmazenado" : "maycon",
#     "senhaArmazenada" : "1234",
#     "nomeUsuario" : "Maycon Guerra"
# }

#teste.cadastraUsuario( novoUsuario )