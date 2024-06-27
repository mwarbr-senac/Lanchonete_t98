from GravaDados import GravaDados

class Controle:
    
    grava = GravaDados()
    
    def cadastraUsuario( self, novoUsuario ):
        return self.grava.cadastraUsuario( novoUsuario )
        
    def mostraUsuarios( self ):
        
        dadosArmazenados = self.grava.ordenaBusca()
        
        print( "+--------------------------------------------------+" )
        print( "|  Usuários Cadastrados:" )
        print( "+--------------------------------------------------+" )
        
        # exibe os usuarios cadastrados através do laço de repetição for
        for i, usuarios in enumerate( dadosArmazenados ):
            print( f"|   {i + 1 } - {usuarios['loginArmazenado']} - {usuarios['nomeUsuario']}" )
        
        print( "+--------------------------------------------------+" )
    
    def apagaUsuario( self, login ):
       self.grava.apagaUsuario( login )