
'''#Atividades Aula 2

#Classificador de Temperatura#

temperatura = int(input('Digite a temperatura '))
if temperatura < 15:
    print('frio')
if temperatura >= 15 and temperatura <= 25:
    print('Agradável')
if temperatura > 25:
    print('Calor!')'''

'''#Verificador de Login#

user1 = input('Digite o usuário ')
senha = input('Digite a senha ')
user_correto = 'aluno' #Lembrar de colocar aspas para o sistema ler a variável corretamente
senha_correta = 'senac123'
if user1 == user_correto and senha == senha_correta:
    print('Acesso liberado')
else:
    print('Acesso negado!')'''

'''#Calculadora de Desconto#

produto = float(input('Digite o valor do produto '))
if produto > 200:
    print('Seu desconto é de 10%')
    print(f'O valor final com desconto é {produto * 0.9:.2f}')
    # .2f -> limitador de casa decimal / f-string para ativar colchetes / formula entre colchetes
elif produto >= 100 and produto <= 200:
    print('Seu desconto é de 5%')
    print(f' Valor final com desconto {produto * 0.95:.2f}')
else:
    print('Você não possui desconto')'''

'''#Exercício Par ou Ímpar
numero = int(input('Digite o número para consulta '))
if numero < 0:
    print('negativo')
else:
    print('postivo')
if numero % 2 == 0:
    print('número par')
else:
    print('numero ímpar')'''

"""#Atividades Aula 1 e 4

#Cadasto de Aluno#

nome = (input('digite o nome '))
idade = int(input('digite a idade '))
nota1 = int(input('digite a primeira nota '))
nota2 = int(input('digite a segunda nota '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'Nome|{nome} | Idade: {idade} | Média: {media} | Situação: Aprovado')
elif media <= 5:
    print(f'Nome|{nome} | Idade: {idade} | Média: {media} | Situação: Recuperação')
else:
    print(f'Nome|{nome} | Idade: {idade} | Média: {media} | Situação: Reprovado')"""



'''#simulador de Caixa de Supermercado
arroz = 24.90
peso_arroz = 5
feijao = 8.5
peso_feijao = 1
macarrao = 4.30
peso_macarrao = 0.5
molho = 3.7
peso_molho = 0.2
oleo = 8.9
peso_oleo = 1
cha = 2.5
total = 0.0
peso_total = 0.0

resposta = input('Deseja comprar arroz? ')
if resposta == 'sim':
    quantidade = int(input('Quantos pacotes? '))
    total += arroz * quantidade
    print('adicionado ao carrinho')
    print(f'Total da compra {total :.2f}')
elif resposta == 'não' or resposta == 'nao':
    print('ok')
else:
    print('Resposta inválida')

resposta = input('Deseja comprar feijão? ')
if resposta =='sim':
    quantidade = int(input('Quantos pacotes? '))
    total += (feijao * quantidade)
    print('adicionado ao carrinho')
    print(f'Total da compra {total :.2f}')
elif resposta == 'não' or resposta == 'nao':
    print('ok')
else:
    print('Resposta inválida')

resposta = input('Deseja comprar Macarrão? ')
if resposta =='sim':
    quantidade = int(input('Quantos pacotes? '))
    total += (macarrao * quantidade)
    print('adicionado ao carrinho')
    print(f'Total da compra {total :.2f}')
elif resposta == 'não' or resposta == 'nao':
    print('ok')
else:
    print('Resposta inválida')

resposta = input('Deseja comprar Molho? ')
if resposta =='sim':
    quantidade = int(input('Quantos pacotes? '))
    total += (molho * quantidade)
    print('adicionado ao carrinho')
    print(f'Total da compra {total :.2f}')
elif resposta == 'não' or resposta == 'nao':
    print('ok')
else:
    print('Resposta inválida')

resposta = input('Deseja comprar Óleo de Soja? ')
if resposta == 'sim':
    quantidade = int(input('Quantos pacotes? '))
    total += (oleo * quantidade)
    print('adicionado ao carrinho')
    print(f'Total da compra {total :.2f}')
elif resposta == 'não' or resposta == 'nao':
    print('ok')
else:
    print('Resposta inválida')'''


#Simulador de Supermercado utilizando Match/Case

"""arroz = 24.90
feijao = 8.5
macarrao = 4.30
molho = 3.7
oleo = 8.9
total = 0.0

resposta = input('Azul ou Verde? ')
match resposta:
    case 'Azul':
        print('Parabéns')
    case 'Verde':
        print('OPA!')"""
    
'''nome = input('Digite o seu nome  ')
n1 = int(input('Digite o numero desejado  '))
n2 = 102
if n1 == n2:
    print(f'parabéns {nome}, hoje é o seu dia de sorte!')
else:
    print('Tente outra vez')'''

'''#Atividades Aula 2
#Classificador de Temperatura
temperatura = int(input('Digite a temperatura '))
if temperatura < 15:
    print('frio')
if temperatura >= 15 and temperatura <= 25:
    print('Agradável')
if temperatura > 25:
    print('Calor!')'''

'''#Verificador de Login
user1 = input('Digite o usuário ')
senha = input('Digite a senha ')
user_correto = 'aluno' #Lembrar de colocar aspas para o sistema ler a variável corretamente
senha_correta = 'senac123'
if user1 == user_correto and senha == senha_correta:
    print('Acesso liberado')
else:
    print('Acesso negado!')'''

'''#Calculadora de Desconto
produto = float(input('Digite o valor do produto '))
if produto > 200:
    print('Seu desconto é de 10%')
    print(f'O valor final com desconto é {produto * 0.9:.2f}')
    # .2f -> limitador de casa decimal / f-string para ativar colchetes / formula entre colchetes
elif produto >= 100 and produto <= 200:
    print('Seu desconto é de 5%')
    print(f' Valor final com desconto {produto * 0.95:.2f}')
else:
    print('Você não possui desconto')'''
    
"""continuar = "sim"
while continuar == "sim":
    produto = input("Digite o nome do produto: ")
    preco = float(input(f"Digite o preço de {produto}: R$ "))
    quantidade = int(input(f"Quantos pacotes de {produto}? "))

"""

'''#Atividades Aula 2

#Classificador de Temperatura#

temperatura = int(input('Digite a temperatura '))
if temperatura < 15:
    print('frio')
if temperatura >= 15 and temperatura <= 25:
    print('Agradável')
if temperatura > 25:
    print('Calor!')'''

'''#Verificador de Login#

user1 = input('Digite o usuário ')
senha = input('Digite a senha ')
user_correto = 'aluno' #Lembrar de colocar aspas para o sistema ler a variável corretamente
senha_correta = 'senac123'
if user1 == user_correto and senha == senha_correta:
    print('Acesso liberado')
else:
    print('Acesso negado!')'''

'''#Calculadora de Desconto#

produto = float(input('Digite o valor do produto '))
if produto > 200:
    print('Seu desconto é de 10%')
    print(f'O valor final com desconto é {produto * 0.9:.2f}')
    # .2f -> limitador de casa decimal / f-string para ativar colchetes / formula entre colchetes
elif produto >= 100 and produto <= 200:
    print('Seu desconto é de 5%')
    print(f' Valor final com desconto {produto * 0.95:.2f}')
else:
    print('Você não possui desconto')'''

'''#Exercício Par ou Ímpar
numero = int(input('Digite o número para consulta '))
if numero < 0:
    print('negativo')
else:
    print('postivo')
if numero % 2 == 0:
    print('número par')
else:
    print('numero ímpar')'''

"""#Atividades Aula 1 e 4

#Cadasto de Aluno#

nome = (input('digite o nome '))
idade = int(input('digite a idade '))
nota1 = int(input('digite a primeira nota '))
nota2 = int(input('digite a segunda nota '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'Nome|{nome} | Idade: {idade} | Média: {media} | Situação: Aprovado')
elif media <= 5:
    print(f'Nome|{nome} | Idade: {idade} | Média: {media} | Situação: Recuperação')
else:
    print(f'Nome|{nome} | Idade: {idade} | Média: {media} | Situação: Reprovado')"""



'''#simulador de Caixa de Supermercado
arroz = 24.90
peso_arroz = 5
feijao = 8.5
peso_feijao = 1
macarrao = 4.30
peso_macarrao = 0.5
molho = 3.7
peso_molho = 0.2
oleo = 8.9
peso_oleo = 1
cha = 2.5
total = 0.0
peso_total = 0.0

resposta = input('Deseja comprar arroz? ')
if resposta == 'sim':
    quantidade = int(input('Quantos pacotes? '))
    total += arroz * quantidade
    print('adicionado ao carrinho')
    print(f'Total da compra {total :.2f}')
elif resposta == 'não' or resposta == 'nao':
    print('ok')
else:
    print('Resposta inválida')

resposta = input('Deseja comprar feijão? ')
if resposta =='sim':
    quantidade = int(input('Quantos pacotes? '))
    total += (feijao * quantidade)
    print('adicionado ao carrinho')
    print(f'Total da compra {total :.2f}')
elif resposta == 'não' or resposta == 'nao':
    print('ok')
else:
    print('Resposta inválida')

resposta = input('Deseja comprar Macarrão? ')
if resposta =='sim':
    quantidade = int(input('Quantos pacotes? '))
    total += (macarrao * quantidade)
    print('adicionado ao carrinho')
    print(f'Total da compra {total :.2f}')
elif resposta == 'não' or resposta == 'nao':
    print('ok')
else:
    print('Resposta inválida')

resposta = input('Deseja comprar Molho? ')
if resposta =='sim':
    quantidade = int(input('Quantos pacotes? '))
    total += (molho * quantidade)
    print('adicionado ao carrinho')
    print(f'Total da compra {total :.2f}')
elif resposta == 'não' or resposta == 'nao':
    print('ok')
else:
    print('Resposta inválida')

resposta = input('Deseja comprar Óleo de Soja? ')
if resposta == 'sim':
    quantidade = int(input('Quantos pacotes? '))
    total += (oleo * quantidade)
    print('adicionado ao carrinho')
    print(f'Total da compra {total :.2f}')
elif resposta == 'não' or resposta == 'nao':
    print('ok')
else:
    print('Resposta inválida')'''


#Simulador de Supermercado utilizando Match/Case

"""arroz = 24.90
feijao = 8.5
macarrao = 4.30
molho = 3.7
oleo = 8.9
total = 0.0

resposta = input('Azul ou Verde? ')
match resposta:
    case 'Azul':
        print('Parabéns')
    case 'Verde':
        print('OPA!')"""

'''nome = input('Digite o seu nome  ')
n1 = int(input('Digite o numero desejado  '))
n2 = 102
if n1 == n2:
    print(f'parabéns {nome}, hoje é o seu dia de sorte!')
else:
    print('Tente outra vez')'''

'''#Atividades Aula 2
#Classificador de Temperatura
temperatura = int(input('Digite a temperatura '))
if temperatura < 15:
    print('frio')
if temperatura >= 15 and temperatura <= 25:
    print('Agradável')
if temperatura > 25:
    print('Calor!')'''

'''#Verificador de Login
user1 = input('Digite o usuário ')
senha = input('Digite a senha ')
user_correto = 'aluno' #Lembrar de colocar aspas para o sistema ler a variável corretamente
senha_correta = 'senac123'
if user1 == user_correto and senha == senha_correta:
    print('Acesso liberado')
else:
    print('Acesso negado!')'''

'''#Calculadora de Desconto
produto = float(input('Digite o valor do produto '))
if produto > 200:
    print('Seu desconto é de 10%')
    print(f'O valor final com desconto é {produto * 0.9:.2f}')
    # .2f -> limitador de casa decimal / f-string para ativar colchetes / formula entre colchetes
elif produto >= 100 and produto <= 200:
    print('Seu desconto é de 5%')
    print(f' Valor final com desconto {produto * 0.95:.2f}')
else:
    print('Você não possui desconto')'''
    
"""continuar = "sim"
while continuar == "sim":
    produto = input("Digite o nome do produto: ")
    preco = float(input(f"Digite o preço de {produto}: R$ "))
    quantidade = int(input(f"Quantos pacotes de {produto}? "))

"""

'''#Atividades Aula 2

#Classificador de Temperatura#

temperatura = int(input('Digite a temperatura '))
if temperatura < 15:
    print('frio')
if temperatura >= 15 and temperatura <= 25:
    print('Agradável')
if temperatura > 25:
    print('Calor!')'''

'''#Verificador de Login#

user1 = input('Digite o usuário ')
senha = input('Digite a senha ')
user_correto = 'aluno' #Lembrar de colocar aspas para o sistema ler a variável corretamente
senha_correta = 'senac123'
if user1 == user_correto and senha == senha_correta:
    print('Acesso liberado')
else:
    print('Acesso negado!')'''

'''#Calculadora de Desconto#

produto = float(input('Digite o valor do produto '))
if produto > 200:
    print('Seu desconto é de 10%')
    print(f'O valor final com desconto é {produto * 0.9:.2f}')
    # .2f -> limitador de casa decimal / f-string para ativar colchetes / formula entre colchetes
elif produto >= 100 and produto <= 200:
    print('Seu desconto é de 5%')
    print(f' Valor final com desconto {produto * 0.95:.2f}')
else:
    print('Você não possui desconto')'''

'''#Exercício Par ou Ímpar
numero = int(input('Digite o número para consulta '))
if numero < 0:
    print('negativo')
else:
    print('postivo')
if numero % 2 == 0:
    print('número par')
else:
    print('numero ímpar')'''

"""#Atividades Aula 1 e 4

#Cadasto de Aluno#

nome = (input('digite o nome '))
idade = int(input('digite a idade '))
nota1 = int(input('digite a primeira nota '))
nota2 = int(input('digite a segunda nota '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'Nome|{nome} | Idade: {idade} | Média: {media} | Situação: Aprovado')
elif media <= 5:
    print(f'Nome|{nome} | Idade: {idade} | Média: {media} | Situação: Recuperação')
else:
    print(f'Nome|{nome} | Idade: {idade} | Média: {media} | Situação: Reprovado')"""



'''#simulador de Caixa de Supermercado
arroz = 24.90
peso_arroz = 5
feijao = 8.5
peso_feijao = 1
macarrao = 4.30
peso_macarrao = 0.5
molho = 3.7
peso_molho = 0.2
oleo = 8.9
peso_oleo = 1
cha = 2.5
total = 0.0
peso_total = 0.0

resposta = input('Deseja comprar arroz? ')
if resposta == 'sim':
    quantidade = int(input('Quantos pacotes? '))
    total += arroz * quantidade
    print('adicionado ao carrinho')
    print(f'Total da compra {total :.2f}')
elif resposta == 'não' or resposta == 'nao':
    print('ok')
else:
    print('Resposta inválida')

resposta = input('Deseja comprar feijão? ')
if resposta =='sim':
    quantidade = int(input('Quantos pacotes? '))
    total += (feijao * quantidade)
    print('adicionado ao carrinho')
    print(f'Total da compra {total :.2f}')
elif resposta == 'não' or resposta == 'nao':
    print('ok')
else:
    print('Resposta inválida')

resposta = input('Deseja comprar Macarrão? ')
if resposta =='sim':
    quantidade = int(input('Quantos pacotes? '))
    total += (macarrao * quantidade)
    print('adicionado ao carrinho')
    print(f'Total da compra {total :.2f}')
elif resposta == 'não' or resposta == 'nao':
    print('ok')
else:
    print('Resposta inválida')

resposta = input('Deseja comprar Molho? ')
if resposta =='sim':
    quantidade = int(input('Quantos pacotes? '))
    total += (molho * quantidade)
    print('adicionado ao carrinho')
    print(f'Total da compra {total :.2f}')
elif resposta == 'não' or resposta == 'nao':
    print('ok')
else:
    print('Resposta inválida')

resposta = input('Deseja comprar Óleo de Soja? ')
if resposta == 'sim':
    quantidade = int(input('Quantos pacotes? '))
    total += (oleo * quantidade)
    print('adicionado ao carrinho')
    print(f'Total da compra {total :.2f}')
elif resposta == 'não' or resposta == 'nao':
    print('ok')
else:
    print('Resposta inválida')'''


#Simulador de Supermercado utilizando Match/Case

print ('Gohan')

print ('vivo')

print ('Gohan')

print ('vivo')
print ('Gohan')

print ('vivo')
print ('Gohan')

print ('vivo')
print ('Gohan')

print ('vivo')

