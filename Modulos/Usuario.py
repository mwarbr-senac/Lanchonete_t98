from Modulos.Telas import Telas
class Usuario:
  """ Documentação da Classe no Python
      Funções do usuário padrão da Lanchonete.
  """

  # propriedades da classe (variáveis)
  # cadeia - string - str - "texto 1234" "1234"
  loginInformado:str = "cliente"
  senhaInformada:str = "1234"

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

  def logar ( self ):

    self.loginInformado = input( "Informe o login: " )
    self.senhaInformada = input( "Informe a senha: " )

    # Comparação - Condicionais - Se - if
    # senão - else - falso

    if self.loginInformado == self.dadosUsuario["loginArmazenado"] and self.senhaInformada == self.dadosUsuario["senhaArmazenada"]  :
      
      self.tela.mensagensSistema( "Login bem sucedido!" )
      
      self.tela.exibeMenu()
      
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
