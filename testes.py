import builtins
import json # JavaScript Object Notation

class Testes:
    
    def carregaArquivo( self ):
        
        with builtins.open( "C:\\Users\\maycon.aguerra\\Desktop\\Dev\\Lanchonete_t98\\textos.txt", "r" ) as dados:
            for linha in dados:
                print( linha.rstrip() )
                
    def carregaJson( self ):
        
        with open( "C:\\Users\\maycon.aguerra\\Desktop\\Dev\\Lanchonete_t98\\usuarios.json", "r" ) as dados:
            
            # recuperando os dados do JSON
            dadosJson = json.load( dados )
            
            print( f" Usuário: { dadosJson[0]["loginArmazenado"] } e a senha { dadosJson[0]["senhaArmazenada"] } " )
            
teste = Testes()
teste.carregaJson()