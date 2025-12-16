#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QUESTÃO 5 - Sistema de BINGO
Programa para gerar cartelas de bingo e verificar ganhadores.
"""

import random  # Biblioteca Random permitida

# EXIGÊNCIA DE CÓDIGO 1 de 6: Função gerar_cartela(sigla)
def gerar_cartela(sigla):
    """
    Função que gera uma cartela de bingo 5x5.
    Recebe a sigla (2 letras) como parâmetro.
    Retorna a matriz que representa a cartela.
    """
    # Gerar uma matriz (lista de listas) com 5 linhas e 5 colunas
    cartela = [[0 for _ in range(5)] for _ in range(5)]

    # Inserir a sigla no CENTRO da matriz (matriz[2][2])
    cartela[2][2] = sigla

    # Coluna 0: 5 valores inteiros aleatórios, não repetidos, entre 1 e 15
    valores_col0 = []
    while len(valores_col0) < 5:
        num = random.randint(1, 15)
        if num not in valores_col0:
            valores_col0.append(num)
    for i in range(5):
        cartela[i][0] = valores_col0[i]

    # Coluna 1: 5 valores inteiros aleatórios, não repetidos, entre 16 e 30
    valores_col1 = []
    while len(valores_col1) < 5:
        num = random.randint(16, 30)
        if num not in valores_col1:
            valores_col1.append(num)
    for i in range(5):
        cartela[i][1] = valores_col1[i]

    # Coluna 2: 4 valores inteiros aleatórios, não repetidos, entre 31 e 45
    # (lembre-se que no centro a sigla deve permanecer)
    valores_col2 = []
    while len(valores_col2) < 4:
        num = random.randint(31, 45)
        if num not in valores_col2:
            valores_col2.append(num)
    # Insere os valores nas posições 0, 1, 3, 4 (pulando o centro)
    cartela[0][2] = valores_col2[0]
    cartela[1][2] = valores_col2[1]
    cartela[3][2] = valores_col2[2]
    cartela[4][2] = valores_col2[3]

    # Coluna 3: 5 valores inteiros aleatórios, não repetidos, entre 46 e 60
    valores_col3 = []
    while len(valores_col3) < 5:
        num = random.randint(46, 60)
        if num not in valores_col3:
            valores_col3.append(num)
    for i in range(5):
        cartela[i][3] = valores_col3[i]

    # Coluna 4: 5 valores inteiros aleatórios, não repetidos, entre 61 e 75
    valores_col4 = []
    while len(valores_col4) < 5:
        num = random.randint(61, 75)
        if num not in valores_col4:
            valores_col4.append(num)
    for i in range(5):
        cartela[i][4] = valores_col4[i]

    return cartela

# EXIGÊNCIA DE CÓDIGO 2 de 6: Função imprimir_cartela(cartela)
def imprimir_cartela(cartela):
    """
    Função que imprime a cartela formatada.
    Recebe uma cartela (matriz) como parâmetro.
    """
    print("\n" + "="*50)
    for i in range(5):
        for j in range(5):
            valor = cartela[i][j]
            # Se for a sigla (string), imprime diretamente
            if isinstance(valor, str):
                print(f"[{valor:^3}]", end=" ")
            else:
                # Imprime valores menores que 10 com um ZERO na frente
                if valor < 10:
                    print(f"[0{valor}]", end=" ")
                else:
                    print(f"[{valor:2}]", end=" ")
        print()  # Nova linha
    print("="*50)

# EXIGÊNCIA DE CÓDIGO 3 de 6: Função sorteia_valor(sorteados)
def sorteia_valor(sorteados):
    """
    Função que sorteia um número entre 1 e 75 que não esteja na lista de sorteados.
    Recebe uma lista de valores já sorteados como parâmetro.
    Retorna o número sorteado ou -1 se a lista estiver cheia.
    """
    # Se a lista estiver cheia, retorna -1
    if len(sorteados) >= 75:
        return -1

    # Sorteia um número entre 1 e 75
    while True:
        num = random.randint(1, 75)
        # Se o número não estiver na lista, retorna ele
        if num not in sorteados:
            return num

# EXIGÊNCIA DE CÓDIGO 4 de 6: Função verifica_ganhador_cheia(cartelas, sorteados)
def verifica_ganhador_cheia(cartelas, sorteados):
    """
    Função que verifica se há uma cartela ganhadora na regra "Cartela Cheia".
    Recebe uma lista de cartelas e uma lista de números sorteados.
    Retorna a cartela ganhadora ou None se não houver ganhadores.
    """
    for cartela in cartelas:
        ganhou = True
        # Verifica se todos os números da cartela foram sorteados
        for i in range(5):
            for j in range(5):
                valor = cartela[i][j]
                # Se for a sigla (string), ignora
                if isinstance(valor, str):
                    continue
                # Se o número não foi sorteado, a cartela não ganhou
                if valor not in sorteados:
                    ganhou = False
                    break
            if not ganhou:
                break

        if ganhou:
            return cartela

    return None

# EXIGÊNCIA DE CÓDIGO 5 de 6: Função verifica_ganhador_LCD(cartelas, sorteados)
def verifica_ganhador_LCD(cartelas, sorteados):
    """
    Função que verifica se há uma cartela ganhadora na regra "Linha, Coluna ou Diagonal".
    Recebe uma lista de cartelas e uma lista de números sorteados.
    Retorna a cartela ganhadora ou None se não houver ganhadores.
    """
    for cartela in cartelas:
        # Verifica linhas
        for i in range(5):
            linha_completa = True
            for j in range(5):
                valor = cartela[i][j]
                if isinstance(valor, str):
                    continue
                if valor not in sorteados:
                    linha_completa = False
                    break
            if linha_completa:
                return cartela

        # Verifica colunas
        for j in range(5):
            coluna_completa = True
            for i in range(5):
                valor = cartela[i][j]
                if isinstance(valor, str):
                    continue
                if valor not in sorteados:
                    coluna_completa = False
                    break
            if coluna_completa:
                return cartela

        # Verifica diagonal principal (de cima-esquerda para baixo-direita)
        diagonal_principal = True
        for i in range(5):
            valor = cartela[i][i]
            if isinstance(valor, str):
                continue
            if valor not in sorteados:
                diagonal_principal = False
                break
        if diagonal_principal:
            return cartela

        # Verifica diagonal secundária (de cima-direita para baixo-esquerda)
        diagonal_secundaria = True
        for i in range(5):
            valor = cartela[i][4-i]
            if isinstance(valor, str):
                continue
            if valor not in sorteados:
                diagonal_secundaria = False
                break
        if diagonal_secundaria:
            return cartela

    return None

# EXIGÊNCIA DE CÓDIGO 6 de 6: Menu principal
if __name__ == "__main__":
    cartelas = []  # Lista para armazenar as cartelas
    regra = 1  # Regra padrão: 1 - Linha, Coluna, Diagonal

    while True:
        print("\n" + "="*50)
        print("SISTEMA DE BINGO")
        print("="*50)
        print("1) Gerar Cartelas")
        print("2) Definir Regras")
        print("3) Começar Bingo!")
        print("4) Encerrar Programa")
        print("="*50)

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            # Gerar Cartelas - apagar cartelas anteriores e perguntar quantidade
            cartelas = []  # Apaga cartelas anteriores
            try:
                qtd = int(input("\nQuantas cartelas devem ser geradas? "))
                # Pede a sigla (primeira letra do nome e primeira letra do sobrenome)
                sigla = input("Digite sua sigla (2 letras - primeira do nome e primeira do sobrenome): ").upper()
                if len(sigla) != 2:
                    sigla = "XX"  # Padrão se não tiver 2 letras

                # Gera as cartelas
                for i in range(qtd):
                    cartela = gerar_cartela(sigla)
                    cartelas.append(cartela)

                print(f"\n{qtd} cartelas geradas com sucesso!")
            except ValueError:
                print("\nQuantidade inválida. Digite um número.")

        elif opcao == "2":
            # Definir Regras - perguntar a regra desejada
            print("\n" + "="*50)
            print("DEFINIR REGRAS")
            print("="*50)
            print("1 - Linha, Coluna, Diagonal (padrão)")
            print("2 - Cartela Cheia")
            print("="*50)

            try:
                regra_input = int(input("Digite a regra desejada: "))
                if regra_input == 1 or regra_input == 2:
                    regra = regra_input
                    print(f"\nRegra definida: {'Linha, Coluna, Diagonal' if regra == 1 else 'Cartela Cheia'}")
                else:
                    regra = 1  # Padrão se valor incorreto
                    print("\nValor incorreto. Modo padrão ativado (Linha, Coluna, Diagonal).")
            except ValueError:
                regra = 1  # Padrão se não for número
                print("\nValor incorreto. Modo padrão ativado (Linha, Coluna, Diagonal).")

        elif opcao == "3":
            # Começar Bingo!
            if len(cartelas) == 0:
                print("\nErro: Nenhuma cartela foi gerada. Gere cartelas primeiro!")
                continue

            sorteados = []  # Lista de números sorteados

            print("\n" + "="*50)
            print("BINGO INICIADO!")
            print("="*50)

            if regra == 2:
                # Regra: Cartela Cheia
                while True:
                    num_sorteado = sorteia_valor(sorteados)
                    if num_sorteado == -1:
                        print("\nTodos os números foram sorteados!")
                        break

                    sorteados.append(num_sorteado)
                    print(f"Número sorteado: {num_sorteado:2} | Total sorteados: {len(sorteados)}")

                    ganhador = verifica_ganhador_cheia(cartelas, sorteados)
                    if ganhador is not None:
                        print("\n" + "="*50)
                        print("BINGO! CARTELA CHEIA!")
                        print("="*50)
                        imprimir_cartela(ganhador)
                        print(f"\nQuantidade de números sorteados: {len(sorteados)}")
                        print("="*50)
                        break
            else:
                # Regra: Linha, Coluna ou Diagonal (padrão)
                while True:
                    num_sorteado = sorteia_valor(sorteados)
                    if num_sorteado == -1:
                        print("\nTodos os números foram sorteados!")
                        break

                    sorteados.append(num_sorteado)
                    print(f"Número sorteado: {num_sorteado:2} | Total sorteados: {len(sorteados)}")

                    ganhador = verifica_ganhador_LCD(cartelas, sorteados)
                    if ganhador is not None:
                        print("\n" + "="*50)
                        print("BINGO! LINHA, COLUNA OU DIAGONAL!")
                        print("="*50)
                        imprimir_cartela(ganhador)
                        print("="*50)
                        break

        elif opcao == "4":
            # Encerrar Programa
            print("\nPrograma encerrado. Obrigado!")
            break

        else:
            # Opção inválida
            print("\nOpção inválida")

