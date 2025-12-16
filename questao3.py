#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QUESTÃO 3 - Sistema de Venda de Toras
Programa para venda de toras de madeira com cálculo de desconto e transporte.
"""

# EXIGÊNCIA DE CÓDIGO 1 de 7: Mensagem de boas-vindas
print("Bem-vindo ao Sistema de Venda de Toras!")
print("Desenvolvido por: [SEU NOME] [SEU SOBRENOME]")

# EXIGÊNCIA DE CÓDIGO 2 de 7: Função escolha_tipo() sem parâmetros
def escolha_tipo():
    """
    Função que pergunta o tipo de madeira e retorna o valor correspondente.
    Repete a pergunta se a opção for inválida.
    """
    while True:
        tipo = input("\nDigite o tipo de madeira (PIN/PER/MOG/IPE/IMB): ").upper()

        if tipo == "PIN":
            return 150.40  # Tora de Pinho: R$ 150,40
        elif tipo == "PER":
            return 170.20  # Tora de Peroba: R$ 170,20
        elif tipo == "MOG":
            return 190.90  # Tora de Mogno: R$ 190,90
        elif tipo == "IPE":
            return 210.10  # Tora de Ipê: R$ 210,10
        elif tipo == "IMB":
            return 220.70  # Tora de Imbuia: R$ 220,70
        else:
            print("Tipo de madeira inválido. Tente novamente.")

# EXIGÊNCIA DE CÓDIGO 3 de 7: Função qtd_toras() sem parâmetros
def qtd_toras():
    """
    Função que pergunta a quantidade de toras e retorna a quantidade e o desconto.
    Repete a pergunta se o valor for acima de 2000 ou não numérico.
    """
    while True:
        try:  # EXIGÊNCIA DE CÓDIGO 6 de 7: Uso de try/except
            qtd = float(input("\nDigite a quantidade de toras (em m³): "))

            # Verifica se a quantidade é maior que 2000
            if qtd > 2000:
                print("Quantidade acima do permitido (máximo 2000 m³). Tente novamente.")
                continue

            # Calcula o desconto baseado na quantidade
            if qtd < 100:
                desconto = 0 / 100  # 0% de desconto
            elif qtd >= 100 and qtd < 500:
                desconto = 4 / 100  # 4% de desconto
            elif qtd >= 500 and qtd < 1000:
                desconto = 9 / 100  # 9% de desconto
            elif qtd >= 1000 and qtd <= 2000:
                desconto = 16 / 100  # 16% de desconto

            return qtd, desconto

        except ValueError:  # EXIGÊNCIA DE CÓDIGO 6 de 7: Tratamento de erro para não numérico
            print("Valor inválido. Digite um número. Tente novamente.")

# EXIGÊNCIA DE CÓDIGO 4 de 7: Função transporte() sem parâmetros
def transporte():
    """
    Função que pergunta pelo serviço adicional de transporte e retorna o valor.
    Repete a pergunta se a opção for inválida.
    """
    while True:
        opcao = input("\nDigite a opção de transporte (1-Rodoviário, 2-Ferroviário, 3-Hidroviário): ")

        if opcao == "1":
            return 1000.0  # Transporte rodoviário: R$ 1000,00
        elif opcao == "2":
            return 2000.0  # Transporte ferroviário: R$ 2000,00
        elif opcao == "3":
            return 2500.0  # Transporte hidroviário: R$ 2500,00
        else:
            print("Opção de transporte inválida. Tente novamente.")

# Código principal (main)
if __name__ == "__main__":
    # Chama as funções para obter os valores
    tipoMadeira = escolha_tipo()
    qtdToras, desconto = qtd_toras()
    valorTransporte = transporte()

    # EXIGÊNCIA DE CÓDIGO 5 de 7: Cálculo do total no código principal (main)
    total = ((tipoMadeira * qtdToras) * (1 - desconto)) + valorTransporte

    # Exibe o resultado
    print(f"\n{'='*50}")
    print("RESUMO DO PEDIDO")
    print(f"{'='*50}")
    print(f"Tipo de madeira: R$ {tipoMadeira:.2f} por m³")
    print(f"Quantidade: {qtdToras:.2f} m³")
    print(f"Desconto: {desconto * 100:.0f}%")
    print(f"Transporte: R$ {valorTransporte:.2f}")
    print(f"{'='*50}")
    print(f"TOTAL A PAGAR: R$ {total:.2f}")
    print(f"{'='*50}")

