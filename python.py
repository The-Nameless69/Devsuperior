#--------------  Iniciando no Python   ------------------------------------------------------
# Comentários
"""
Usando o VScode, temos dois tipos de comentários, usando a Hashtag (#) ou usando três aspas simple (ou duplas) para abrir
e três aspas simples (ou duplas) para fechar o comentario. como neste exemplo aqui. O comentário mais usado é a Hashtag
pois o VScode realmente ignora ele e não ler. Já os das aspas simples (ou duplas) ele ler e guarda na memória e isto não
é bom. O comentário usado com aspas server para lembrar o Dev o que ele irá fazer. Já o comentáro com a Hashtag serve
para informar algo no seu código.
"""

#---------------  A Função Print  -------------------------------------------------------------
#A função print é utilizado para imprimir algo na tela. Ele pode ser um output ou um input. Exemplo:

print(123, 456)
print("Olá Mundo!")
print('Hello World!')

#Para números não é necessário aspas, pois não é uma "String". String significa Texto. Para digitar um texto na saida do print
# é necessário usar aspas, pode ser simples ou duplas. Como no exemplo acima.

#------------  Usando os Separadores de Argumentos  ------------------------------------------

print(12, 34, 56) #entre a vírgula irá existir um espaço em branco. Aí onde entrará o Separador.

print(12, 34, 56, sep="/") #Nos separadores fica a sua escolha de escolher qual caractere você quer para tal função.

#-----------  Mudando a Forma de Quebra de Linha  --------------------------------------------

print(1982, 1983, end='/')
print(1984, 1985, end='\n**') #O \n quebra a linha e adiciona os caracteres no inicio de outra linha.
print(1986, 1987)

# O end, faz com que não quebre a linha e adiciona um caractere escolhido para a separação da linha. Pode-se usar qualquer
# caractere no end também. Fica a seu critério. Lembre-se de deixar o código limpo e bonito.

#------------------------  Números do Tipo Int & Float  ---------------------------------------
# Int = Inteiro (Qualquer Número positivo ou negativo que não tenha ponto)
# Float = Ponto Flutuante (Número do Tipo Real)

print (123)  # Inteiro
print (-321) # Inteiro
print (0)    # Inteiro
print (12.3) # Float
print (-3.5) # Float
print (0.0)  # Float

#----------------------  Como Saber o Tipo de Função que Estou Trabalhando  --------------------

# Usando a classe Type iremos ver qual função estamos trabalhando. Vejmos exemplos abaixo:

print (type("Olá!"))  # Isto é uma "STR" que significa String = Texto.
print (type(1.1))     # Isto será um Float, que significa um Número com ponto Flutuante (Real)
print (type(123))     # Isto será um Int, classe número Inteiro.

# ATENÇÃO: TUDO EM PYTHON É UM OBJETO.

#--------------------------------  Tipo de Bool (Boolean)  -------------------------------------
# No tipo de dado Boolean só existe duas funções, True (Verdadeiro) ou False (Falso).

print(10 ==10) # Questionando o programa se de é igual a 10. Como é um Bool tem que me retornar True ou False.
print(10 == 11) #False
print(type(10 == 10)) # A classe de retorno será Bool.
















