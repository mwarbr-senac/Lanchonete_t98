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
            
    def exibeMenu( self ):
        print( f"+--------------------------------------------------+" )
        print( f"|                            Bem Vindo { usuario } |" )
        print( f"|   ** Menu - Escolha uma Opção:                   |" )
        print( f"|   1 - Cadastrar                                  |" )
        print( f"|   2 - Listar                                     |" )
        print( f"+--------------------------------------------------+" )