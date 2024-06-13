#importando a classe Time do próprio Python
import time 
import os

class Telas:
    
    def entradaSistema( self ):
        print( f"+--------------------------------------------------+" )
        print( f"|                                                  |" )
        print( f"|      ** Seja Bem Vindo ao Sistema **             |" )
        print( f"|                                                  |" )
        print( f"+--------------------------------------------------+" )
        
        self.esperaLimpa()
        
    def esperaLimpa( self, tempo = 3 ):
        # esperar - delay de Xsegundos
        time.sleep( tempo )

        # limpa a tela
        self.limpaConsole()
    
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
        
        if os.name == "nt": # windows nt - Linux posix - Mac darwin 
            os.system( "cls" )
        else: 
            os.system( "clear" )
            
        # if os.name == "nt": # windows nt - Linux posix - Mac darwin 
        #     os.system( "cls" )
        # elif os.name == "darwin": 
        #     os.system( "clear" )
        # else:
        #     os.system( "clear" )
        
        # tipoSistema = os.name
        # switch( tipoSistema ):
        #     case "nt":
        #         os.system("cls")            
        #         break: