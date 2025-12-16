#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QUESTÃO 4 - Sistema de Gerenciamento de Contatos Comerciais
Programa para cadastrar, consultar e remover contatos usando lista de dicionários.
"""

# EXIGÊNCIA DE CÓDIGO 1 de 8: Mensagem de boas-vindas
print("Bem-vindo ao Sistema de Gerenciamento de Contatos Comerciais!")
print("Desenvolvido por: [SEU NOME] [SEU SOBRENOME]")

# EXIGÊNCIA DE CÓDIGO 2 de 8: Lista lista_contatos e variável id_global com valor inicial igual ao RU
lista_contatos = []  # EXIGÊNCIA DE CÓDIGO 7 de 8: Lista de dicionários
id_global = 4297914  # SUBSTITUIR PELO SEU RU

# EXIGÊNCIA DE CÓDIGO 3 de 8: Função cadastrar_contato(id)
def cadastrar_contato(id):
    """
    Função que cadastra um novo contato.
    Recebe o id como parâmetro e armazena os dados em um dicionário dentro da lista.
    """
    # Pergunta nome, atividade e telefone do contato
    nome = input("Digite o nome do contato: ")
    atividade = input("Digite a atividade do contato: ")
    telefone = input("Digite o telefone do contato: ")

    # Armazena os dados em um dicionário
    contato = {
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }

    # Copia o dicionário para dentro da lista_contatos (utilizando copy)
    import copy
    lista_contatos.append(copy.copy(contato))

    print(f"Contato cadastrado com sucesso! ID: {id}")

# EXIGÊNCIA DE CÓDIGO 4 de 8: Função consultar_contatos()
def consultar_contatos():
    """
    Função que consulta contatos de diferentes formas.
    Não recebe parâmetros.
    """
    while True:
        print("\n" + "="*50)
        print("MENU DE CONSULTA")
        print("="*50)
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Atividade")
        print("4. Retornar ao menu")
        print("="*50)

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            # Consultar Todos - apresentar todos os contatos
            if len(lista_contatos) == 0:
                print("\nNenhum contato cadastrado.")
            else:
                print("\n" + "="*50)
                print("TODOS OS CONTATOS")
                print("="*50)
                for contato in lista_contatos:
                    print(f"ID: {contato['id']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}")
                    print("-" * 50)

        elif opcao == "2":
            # Consultar por Id - solicitar id e apresentar o contato específico
            try:
                id_busca = int(input("\nDigite o ID do contato: "))
                encontrado = False
                for contato in lista_contatos:
                    if contato['id'] == id_busca:
                        print("\n" + "="*50)
                        print("CONTATO ENCONTRADO")
                        print("="*50)
                        print(f"ID: {contato['id']}")
                        print(f"Nome: {contato['nome']}")
                        print(f"Atividade: {contato['atividade']}")
                        print(f"Telefone: {contato['telefone']}")
                        print("="*50)
                        encontrado = True
                        break
                if not encontrado:
                    print("\nContato não encontrado.")
            except ValueError:
                print("\nID inválido. Digite um número.")

        elif opcao == "3":
            # Consultar por Atividade - solicitar atividade e apresentar contatos
            atividade_busca = input("\nDigite a atividade: ")
            encontrados = []
            for contato in lista_contatos:
                if contato['atividade'].lower() == atividade_busca.lower():
                    encontrados.append(contato)

            if len(encontrados) == 0:
                print("\nNenhum contato encontrado com essa atividade.")
            else:
                print("\n" + "="*50)
                print(f"CONTATOS COM ATIVIDADE: {atividade_busca}")
                print("="*50)
                for contato in encontrados:
                    print(f"ID: {contato['id']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}")
                    print("-" * 50)

        elif opcao == "4":
            # Retornar ao menu principal
            return

        else:
            # Opção inválida - repetir a pergunta
            print("\nOpção inválida")

# EXIGÊNCIA DE CÓDIGO 5 de 8: Função remover_contato()
def remover_contato():
    """
    Função que remove um contato da lista pelo ID.
    Não recebe parâmetros.
    """
    while True:
        try:
            id_remover = int(input("\nDigite o ID do contato a ser removido: "))

            # Procura o contato na lista
            encontrado = False
            for i, contato in enumerate(lista_contatos):
                if contato['id'] == id_remover:
                    lista_contatos.pop(i)
                    print(f"Contato com ID {id_remover} removido com sucesso!")
                    encontrado = True
                    break

            if not encontrado:
                print("Id inválido")
                # Repete a pergunta se o id não for encontrado
            else:
                break  # Sai do loop se o contato foi removido

        except ValueError:
            print("Id inválido. Digite um número.")

# EXIGÊNCIA DE CÓDIGO 6 de 8: Estrutura de menu no código principal (main)
if __name__ == "__main__":
    while True:
        print("\n" + "="*50)
        print("MENU PRINCIPAL")
        print("="*50)
        print("1) Cadastrar Contato")
        print("2) Consultar Contato")
        print("3) Remover Contato")
        print("4) Encerrar Programa")
        print("="*50)

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            # Cadastrar Contato - chamar função e incrementar id_global
            cadastrar_contato(id_global)
            id_global += 1

        elif opcao == "2":
            # Consultar Contato - chamar função consultar_contatos
            consultar_contatos()

        elif opcao == "3":
            # Remover Contato - chamar função remover_contato
            remover_contato()

        elif opcao == "4":
            # Encerrar Programa - sair do menu
            print("\nPrograma encerrado. Obrigado!")
            break

        else:
            # Opção inválida - repetir a pergunta
            print("\nOpção inválida")

