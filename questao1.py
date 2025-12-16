#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QUESTÃO 1 - Sistema de Planos de Saúde
Programa que calcula o valor mensal do plano baseado na idade do cliente.
"""

# EXIGÊNCIA DE CÓDIGO 1 de 6: Mensagem de boas-vindas com nome e sobrenome
print("Bem-vindo ao Sistema de Planos de Saúde!")
print("Desenvolvido por: [SEU NOME] [SEU SOBRENOME]")

# EXIGÊNCIA DE CÓDIGO 2 de 6: Input do valorBase e idade
valorBase = float(input("Digite o valor base do plano: R$ "))
idade = int(input("Digite a idade do cliente: "))

# EXIGÊNCIA DE CÓDIGO 3 de 6: Regras de valores conforme a idade
# EXIGÊNCIA DE CÓDIGO 5 de 6: Uso de if, elif e else
if idade >= 0 and idade < 19:
    # Se a idade for maior ou igual que 0 e menor que 19, o valor será de 100% do valor base
    porcentagem = 100 / 100
elif idade >= 19 and idade < 29:
    # Se a idade for maior ou igual que 19 e menor que 29, o valor será de 150% do valor base
    porcentagem = 150 / 100
elif idade >= 29 and idade < 39:
    # Se a idade for maior ou igual que 29 e menor que 39, o valor será de 225% do valor base
    porcentagem = 225 / 100
elif idade >= 39 and idade < 49:
    # Se a idade for maior ou igual que 39 e menor que 49, o valor será de 240% do valor base
    porcentagem = 240 / 100
elif idade >= 49 and idade < 59:
    # Se a idade for maior ou igual que 49 e menor que 59, o valor será de 350% do valor base
    porcentagem = 350 / 100
else:
    # Se a idade for maior ou igual que 59, o valor será de 600% do valor base
    porcentagem = 600 / 100

# EXIGÊNCIA DE CÓDIGO 4 de 6: Cálculo do valorMensal
valorMensal = valorBase * porcentagem

# Exibição do resultado
print(f"\nValor mensal do plano: R$ {valorMensal:.2f}")

