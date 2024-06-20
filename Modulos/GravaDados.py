import builtins
import json

class GravaDados:
    
    usuariosCadastrados = {
        "loginArmazenado" : "cliente",
        "senhaArmazenada" : "1234",
        "nomeUsuario" : "João dos Santos",
    }
    
    # open( nomeArquivo, modoAbertura) é uma função do python3 que lê e escreve arquivos 
        # w - write - escrita
        # r - read - leitura
        # r+ - escrita/leitura    
    def salvaDados( self  ):
        
        with open( "Lanchonete_t98\\Modulos\\dados.txt", "w") as dados:
            
            # converter o vetor em JSON
            dadosJson = json.dumps( self.usuariosCadastrados )
            
            dados.write( dadosJson )
            
            dados.close()
        
        print("Dados Armazenados")
            
    def leDados( self ):
        # para ler usamos a classe builtins do Python3 
        with builtins.open( "Lanchonete_t98\\Modulos\\dados.txt", "r") as dados:
            
            print( f"No arquivo temos: \n" )
            
            # for é um laço de repetição
            # para cada linha do arquivo de texto 
            for linha in dados.readlines() :
                print( linha.rstrip() ) 
    
    def adicionaCadastro( self, novoUsuario ):
        
        # pegamos o json no arquivo de dados
        
        with builtins.open( "Lanchonete_t98\\Modulos\\dados.txt", "r") as dados:
                    
            # adicionando um novo item ao nosso vetor
        
            # salvar novamente o arquivo
        
        
    def exportaDados( self ):
        print("")
        
dados = GravaDados()
novoUsuario = {
            "loginArmazenado" : "cliente2",
            "senhaArmazenada" : "1234",
            "nomeUsuario" : "Maria da Silva",
        }
dados.adicionaCadastro(novoUsuario)
dados.salvaDados()
dados.leDados()