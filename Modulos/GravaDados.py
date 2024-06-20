import builtins

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
        
        with open( "Lanchonete\\Modulos\\dados.txt", "w") as dados:
            
            dados.write( self.usuariosCadastrados )
            
            dados.close()
        
        print("Dados Armazenados")
            
    def leDados( self ):
        # para ler usamos a classe builtins do Python3 
        with builtins.open( "Lanchonete\\Modulos\\dados.txt", "r") as dados:
            
            print( f"No arquivo temos: \n" )
            
            # for é um laço de repetição
            # para cada linha do arquivo de texto 
            for linha in dados.readlines() :
                print( linha.rstrip() ) 
        
        
    def exportaDados( self ):
        print("")
        
dados = GravaDados()
dados.salvaDados()
dados.leDados()