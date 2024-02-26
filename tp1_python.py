import random

def calculadora_numeros():
    print('Calculadora de Números\n')
    numero_1 = int(input('Escreva o primeiro número: '))
    numero_2 = int(input('Escreva o segundo número: '))

    soma = numero_1 + numero_2
    subtracao = numero_1 - numero_2
    multiplicacao = numero_1 * numero_2
    divisao = numero_1 / numero_2
    divisao_inteira = numero_1 // numero_2

    print(f'Soma: {soma}')
    print(f'Subtração: {subtracao}')
    print(f'Multiplicação: {multiplicacao}')
    print(f'Divisão : {divisao}')
    print(f'Divisão inteira: {divisao_inteira}')

def calculadora_horario():
    minutos_input = int(input('Escreva um horário em minutos: '))

    if minutos_input % 60 == 0:
        horas = minutos_input / 60
        print(f'{horas} hora(s)')
    else:
        horas = minutos_input // 60
        minutos = minutos_input - (horas * 60)
        print(f'{horas} hora(s) e {minutos} minuto(s)')

    print('Escreva um horário: ')
    horas_input = int(input('Horas: '))
    minutos_input = int(input('Minutos: '))

    conversao_minutos = (horas_input * 60) + minutos_input
    print(f'{conversao_minutos} minuto(s)')

def combinador_nomes():
    print('Escreva 2 nomes:')
    primeiro_nome = input('Primeiro nome: ')
    segundo_nome = input('Segundo nome: ')

    nome_novo = primeiro_nome + segundo_nome
    print(nome_novo[::-1])

def escolher_operacao():
    print('Escreva dois números depois escolha qual operação você deseja fazer: ')
    numero_1 = int(input('Escreva o primeiro número: '))
    numero_2 = int(input('Escreva o segundo número: '))

    print('0 - Soma')
    print('1 - Subtração')
    print('2 - Multiplicação')
    print('3 - Divisão')

    usuario_input = int(input('Qual operação você deseja fazer: '))
    if usuario_input == 0:
        print(numero_1 + numero_2)
    elif usuario_input == 1:
        print(numero_1 - numero_2)
    elif usuario_input == 2:
        print(numero_1 * numero_2)
    elif usuario_input == 3:
        print(numero_1 / numero_2)
    else:
        print('Escolha inválida')

def saudacoes():
   primeiro_nome = input('Escreva seu primeiro nome: ')
   segundo_nome = input('Escreva seu segundo nome: ')
   print(f'Saudações {primeiro_nome} {segundo_nome}')

def numero_secreto():
    numero_secreto = random.randint(0, 10)
    numero_usuario = int(input('Escreva um número entre 0 e 10: '))

    if numero_usuario == numero_secreto:
        print('Você acertou o número secreto!')
    elif numero_usuario < numero_secreto:
        print('Você errou! muito baixo')
    elif numero_usuario > numero_secreto:
        print('Você errou! muito alto')
    print(f'Número secreto: {numero_secreto}')

def calculadora_IMC():
    peso = int(input('Escreva seu peso em kgs: '))
    altura = float(input('Escreva sua altura em metros: '))

    imc = peso / (altura ** 2)
    print(f'IMC: {round(imc,2)}')

    if imc < 18.5:
        print('Abaixo do peso')
    elif imc >= 18.5 and imc <= 24.9:
        print('Peso normal')
    elif imc >= 25 and imc <= 29.9:
        print('Sobrepeso')
    elif imc >= 30 and imc <= 34.9:
        print('Obesidade 1')
    else:
        print('Obesidade 2 e 3')

def verificador_de_idade():
    idade_usuario = int(input('Escreva sua idade: '))
    if idade_usuario >= 18:
        print('Você é maior de idade!')
    else:
        print('Você não é maior de idade!')

def programa_de_desconto():
    valor_produto = int(input('Escreva qual o valor do produto para o programa calcular seu desconto: '))
    if valor_produto < 100:
        print('Nenhum desconto aplicado!')
    elif valor_produto >= 100 and valor_produto < 200:
        print('Desconto de 10% aplicado')

def contador_de_historia():
    locais = ['Bosque Encantado','Floresta Mal-Assombrada','Parque de diversões','Cidade SubMarina']
    pessoas = ['Augusto','Joao','Maria','Pablo']
    acoes = ["explorar uma caverna", "construir um foguete", "aprender magia", "viajar no tempo"]
    finais = ['Feliz','Triste']

    local = random.choice(locais)
    pessoa = random.choice(pessoas)
    acao = random.choice(acoes)
    final = random.choice(finais)
    print(f'{pessoa} estava passeando num(a) {local} e decidiu {acao}, o que definitivamente foi um final {final}')

def lancamento_de_dados():
    quantidade_de_dados = int(input('Quantos dados você deseja jogar? '))
    for i in range(quantidade_de_dados):
        print(f'Dado {i + 1} => {random.randint(1,6)}')

def classificador_palavra():
    
    palavra_input = input('Escreva uma palavra: ')
    if len(palavra_input) < 5:
        print('Esta palavra é curta')
    else:
        print('Esta palavra é longa')

def verificador_palindromo():

    palavra_input = input('Escreva uma palavra: ')
    letras = []
    for char in palavra_input:
        letras.append(char)
    
    letras_ao_contrario = []
    for item in reversed(letras):
        letras_ao_contrario.append(item)
    
    if letras_ao_contrario == letras:
        print('Esta palavra é um palindromo')
    else:
        print('Esta palavra não é um palindromo')

def votacao():
    print(' 0 - Banana')
    print(' 1 - Carro')
    print(' 2 - Cavalo')
    votos_banana = 0
    votos_carro = 0
    votos_cavalo = 0

    voto_input = int(input('Escolha uma das opções para votar'))
    if voto_input == 0:
        votos_banana += 1
        print('Voto computado com sucesso')
    elif voto_input == 1:
        votos_carro += 1
        print('Voto computado com sucesso')
    elif voto_input == 2:
        votos_cavalo += 1
        print('Voto computado com sucesso')
    else:
        print('Opção Inválida')

    print(f'Votos: banana {votos_banana}, Carro {votos_carro}, Cavalo {votos_cavalo}')

def escolhas():
    print('Bem vindo ao jogo das escolhas')
    print('Você está caminhanho por uma floresta e se depara com dois caminhos')
    escolha = input('Você deseja ir para esquerda ou para direita: ').lower()
    premios = []
    if escolha == 'esquerda':
        print('Você foi para esquerda e encontrou uma caverna')
        escolha = input('entrar ou dar meia volta: ').lower()
        if escolha == 'entrar': 
            print('você encontrou um baú de tesouros...')
            premios.append('Báu do tesouro')
            escolha = input('você deseja continuar ou sair: ').lower()
            if escolha == 'continuar':
                print('Você encontrou um urso faminto...')
                print('Sua jornada acaba aqui.')
            elif escolha == 'sair':
                print('Você saiu da caverna e entrou no caminho da direita da floresta.')
                print('Você continua andando e se depara com uma ponte sobre um rio')
                escolha = input('Atravessar ou dar meia-volta: ').lower()
                if escolha == 'meia volta':
                    print('você se deparou com vários lobos famintos...')
                    print('Sua jornada acaba aqui')
                elif escolha == 'atravessar':
                    ponte_quebrada = random.randint(0,1)
                    if ponte_quebrada == 0:
                        print('A ponte caiu e você se afogou no rio')
                        print('Sua jornada acaba aqui')
                    else:
                        print('Você encontrou uma vila de fazendeiros')
                        print('Sua jornada acaba aqui')
                        print('Seus prêmios: ')
                        for item in premios:
                            print(item)
        elif escolha == 'meia volta':
            print('Você continua andando e se depara com uma ponte sobre um rio')
            escolha = input('Atravessar ou dar meia-volta: ').lower()
            if escolha == 'meia volta':
                print('você se deparou com vários lobos famintos...')
                print('Sua jornada acaba aqui')
            elif escolha == 'atravessar':
                ponte_quebrada = random.randint(0,1)
                if ponte_quebrada == 0:
                    print('A ponte caiu e você se afogou no rio')
                    print('Sua jornada acaba aqui')
                else:
                    print('Você encontrou uma vila de fazendeiros')
                    print('Sua jornada acaba aqui')
                    print('Seus prêmios: ')
                    for item in premios:
                        print(item)
            else:
                print('Escolha inválida')             
        else:
            print('Escolha inválida')        
    elif escolha == 'direita':
        print('Você continua andando e se depara com uma ponte sobre um rio')
        escolha = input('Atravessar ou dar meia-volta: ').lower()
        if escolha == 'meia volta':
            print('você se deparou com vários lobos famintos...')
            print('Sua jornada acaba aqui')
        elif escolha == 'atravessar':
            ponte_quebrada = random.randint(0,1)
            if ponte_quebrada == 0:
                print('A ponte caiu e você se afogou no rio')
                print('Sua jornada acaba aqui')
            else:
                print('Você encontrou uma vila de fazendeiros')
                print('Sua jornada acaba aqui')
                print('Seus prêmios: ')
                for item in premios:
                     print(item)
        else:
            print('Escolha inválida')             
    else:
        print('Escolha inválida')                               

                




calculadora_numeros()
calculadora_horario()
combinador_nomes()
escolher_operacao()
saudacoes()
numero_secreto()
calculadora_IMC()
verificador_de_idade()
programa_de_desconto()
contador_de_historia()
lancamento_de_dados()    
classificador_palavra()
verificador_palindromo()
votacao()
escolhas()