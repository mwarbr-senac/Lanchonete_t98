from Modulos.Telas import Telas
from GravaDados import GravaDados

class Usuario:
  """ Documentação da Classe no Python
      Funções do usuário padrão da Lanchonete.
  """

  # propriedades da classe (variáveis)
  # cadeia - string - str - "texto 1234" "1234"
  loginInformado:str = None
  senhaInformada:str = None

  # Array - matriz ou vetor nomeado
  dadosUsuario = {
      "loginArmazenado" : "cliente",
      "senhaArmazenada" : "1234",
      "nomeUsuario" : "João dos Santos",
  }
  
  tela = Telas()

  # Método Construtor: executado ao instanciar a classe
  # self refere-se à instância da classe
  def __init__( self ):
    
    # chamando a tela de entrada que está no módulo Telas.py
    # entrada = Telas() # instância da classe Telas
    self.tela.entradaSistema()
    
    # chamando o método logar da classe
    self.logar()

  def logar( self ):
    
    self.loginInformado = input( "Informe o login ou 0 para sair: " )

    # opção para sair do programa
    if self.loginInformado == "0":
      self.tela.saidaSistema()
      return False
    
    else:
      self.senhaInformada = input( "Informe a senha: " )

    # Comparação - Condicionais - Se - if
    # senão - else - falso

    

    # buscaremos os valores armazenados no Json usando o GravaDados.py
    usuarioArmazenado = GravaDados()
    
    user = usuarioArmazenado.recuperaUsuario( self.loginInformado )      

    if self.loginInformado == user["loginArmazenado"] and self.senhaInformada == user["senhaArmazenada"]  :
      
      self.tela.mensagensSistema( "Login bem sucedido!" )
      
      # enviando o nome do usuário para a tela
      self.tela.exibeMenu( user["nomeUsuario"])
      
    else:

      self.tela.mensagensSistema( " Falha ao se conectar, tente novamente ")
      
      self.logar()

  def sair( self ):
    print( "Logout do sistema" )
    

# Uma classe convencional precisa ser Instanciada para que seus objetos possam ser usados.
# Instanciar uma classe é colocar uma cópia ( instância ) em uma variável ( objeto )
# operador de atribuição =
# atendente = Usuario()

# usando um dos métodos
# atendente.sair()
