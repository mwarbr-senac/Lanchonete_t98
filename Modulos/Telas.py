#importando a classe Time do próprio Python
import time 
import os
from Modulos.Controle import Controle

class Telas:
    
    controle = Controle()
    
    def entradaSistema( self ):
        
        self.limpaConsole()

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
        self.limpaConsole()
        print( f"+--------------------------------------------------+" )
        print( f"|                                                  |" )
        print( f"|      ** Obrigado por usar o Sistema **           |" )
        print( f"|                                                  |" )
        print( f"+--------------------------------------------------+" )

        self.esperaLimpa()
    
    def mensagensSistema( self, mensagem ):
        self.limpaConsole()
        print( f"+--------------------------------------------------+" )
        print( f"|                                                  |" )
        print( f"   ** {mensagem} **             " )
        print( f"|                                                  |" )
        print( f"+--------------------------------------------------+" )
        self.esperaLimpa()
    
    def limpaConsole( self ):
        
        if os.name == "nt": # windows nt - Linux posix - Mac darwin 
            os.system( "cls" )
        else: 
            os.system( "clear" )
            
    def exibeMenu( self, usuario ):
        self.limpaConsole()
        
        while True:
            print( f"+--------------------------------------------------+" )
            print( f"|   ** Menu - Escolha uma Opção:                   |" )
            print( f"|   1 - Cadastrar                                  |" )
            print( f"|   2 - Listar Todos                               |" )
            print( f"|   3 - Apagar Usuário                             |" )
            print( f"|   0 - Sair                                       |" )
            print( f"+--------------------------------------------------+" )
        
            # convertemos para inteiro a string do input
            escolha = int(input("Digite a sua escolha:"))
            
            self.limpaConsole()
                        
            if escolha == 1:
                nome =  input("Informe o nome do funcionário:")
                user = input("Informe o usuário:")
                senha =  "1234"
                
                # vetor com os dados cadastrados
                novoUsuario = { 
                    "loginArmazenado" :  user , 
                    "senhaArmazenada" :  senha, 
                    "nomeUsuario" : nome 
                }
                
                self.controle.cadastraUsuario( novoUsuario )
                
            elif escolha == 2:
                self.controle.mostraUsuarios()
            
            elif escolha == 3:
                usuario = input("Informe o nome do usuário a ser apagado:")
                self.controle.apagaUsuario( usuario)
                
            else:
                self.saidaSistema()
                break
                