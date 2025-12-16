#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QUESTÃO 2 - Sistema de Pizzaria
Programa para vendas de pizzas doces e salgadas com diferentes tamanhos.
"""

# EXIGÊNCIA DE CÓDIGO 1 de 8: Mensagem de boas-vindas e menu
print("Bem-vindo à Pizzaria!")
print("Desenvolvido por: [SEU NOME] [SEU SOBRENOME]")
print("\n" + "="*50)
print("MENU DE PIZZAS")
print("="*50)
print("Tamanho P: Pizza Salgada (PS) - R$ 30,00 | Pizza Doce (PD) - R$ 34,00")
print("Tamanho M: Pizza Salgada (PS) - R$ 45,00 | Pizza Doce (PD) - R$ 48,00")
print("Tamanho G: Pizza Salgada (PS) - R$ 60,00 | Pizza Doce (PD) - R$ 66,00")
print("="*50)

# EXIGÊNCIA DE CÓDIGO 5 de 8: Acumulador para somar os valores dos pedidos
valorTotal = 0.0

# EXIGÊNCIA DE CÓDIGO 7 de 8: Uso de while, break e continue
while True:
    # EXIGÊNCIA DE CÓDIGO 2 de 8: Input do sabor com validação
    sabor = input("\nDigite o sabor da pizza (PS para Salgada ou PD para Doce): ").upper()

    if sabor != "PS" and sabor != "PD":
        print("Sabor inválido. Tente novamente")
        continue  # EXIGÊNCIA DE CÓDIGO 7 de 8: Uso de continue

    # EXIGÊNCIA DE CÓDIGO 3 de 8: Input do tamanho com validação
    tamanho = input("Digite o tamanho da pizza (P, M ou G): ").upper()

    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print("Tamanho inválido. Tente novamente")
        continue  # EXIGÊNCIA DE CÓDIGO 7 de 8: Uso de continue

    # EXIGÊNCIA DE CÓDIGO 4 de 8: If, elif e/ou else aninhados com todas as combinações
    if sabor == "PS":  # Pizza Salgada
        if tamanho == "P":
            valor = 30.0
        elif tamanho == "M":
            valor = 45.0
        else:  # tamanho == "G"
            valor = 60.0
    else:  # sabor == "PD" - Pizza Doce
        if tamanho == "P":
            valor = 34.0
        elif tamanho == "M":
            valor = 48.0
        else:  # tamanho == "G"
            valor = 66.0

    # Adiciona o valor ao acumulador
    valorTotal += valor
    print(f"Pizza adicionada! Valor: R$ {valor:.2f}")

    # EXIGÊNCIA DE CÓDIGO 6 de 8: Pergunta se deseja pedir mais alguma coisa
    continuar = input("\nDeseja pedir mais alguma coisa? (sim/não): ").lower()

    if continuar != "sim":
        break  # EXIGÊNCIA DE CÓDIGO 7 de 8: Uso de break

# Exibe o valor total do pedido
print(f"\nValor total do pedido: R$ {valorTotal:.2f}")
print("Obrigado pela preferência!")

