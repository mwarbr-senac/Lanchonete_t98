class Telas:
    
    def entradaSistema( self ):
        print( f"+--------------------------------------------------+" )
        print( f"|                                                  |" )
        print( f"|      ** Seja Bem Vindo ao Sistema **             |" )
        print( f"|                                                  |" )
        print( f"+--------------------------------------------------+" )
        
        self.esperaLimpa()
        
    def esperaLimpa( self, tempo ):
        # esperar Xsegundos
        time.sleep( tempo )
        
        # limpa a tela
    
    def saidaSistema( self ):
        print( f"+--------------------------------------------------+" )
        print( f"|                                                  |" )
        print( f"|      ** Obrigado por usar o Sistema **           |" )
        print( f"|                                                  |" )
        print( f"+--------------------------------------------------+" )
    
    def mensagensSistema( self, mensagem ):
        print( f"+--------------------------------------------------+" )
        print( f"|                                                  |" )
        print( f"   ** {mensagem} **             " )
        print( f"|                                                  |" )
        print( f"+--------------------------------------------------+" )
    
    def limpaConsole( self ):
        print("")  