#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Teste - Verifica se o ambiente Python está configurado corretamente
Execute este script antes de rodar as questões para garantir que tudo está OK.
"""

import sys

def verificar_python():
    """Verifica a versão do Python"""
    print("=" * 60)
    print("VERIFICAÇÃO DO AMBIENTE PYTHON")
    print("=" * 60)

    versao = sys.version_info
    print(f"✓ Python {versao.major}.{versao.minor}.{versao.micro} detectado")

    if versao.major < 3 or (versao.major == 3 and versao.minor < 6):
        print("⚠ ATENÇÃO: Python 3.6 ou superior é recomendado!")
        return False
    else:
        print("✓ Versão do Python compatível!")
        return True

def verificar_bibliotecas():
    """Verifica se as bibliotecas necessárias estão disponíveis"""
    print("\n" + "=" * 60)
    print("VERIFICAÇÃO DE BIBLIOTECAS")
    print("=" * 60)

    bibliotecas = {
        'random': 'Biblioteca padrão para números aleatórios',
        'copy': 'Biblioteca padrão para cópia de objetos'
    }

    todas_ok = True

    for lib, descricao in bibliotecas.items():
        try:
            __import__(lib)
            print(f"✓ {lib} - {descricao}")
        except ImportError:
            print(f"✗ {lib} - ERRO: Não encontrada!")
            todas_ok = False

    return todas_ok

def verificar_arquivos():
    """Verifica se os arquivos das questões existem"""
    print("\n" + "=" * 60)
    print("VERIFICAÇÃO DE ARQUIVOS")
    print("=" * 60)

    import os

    arquivos = [
        'questao1.py',
        'questao2.py',
        'questao3.py',
        'questao4.py',
        'questao5.py'
    ]

    todos_ok = True

    for arquivo in arquivos:
        if os.path.exists(arquivo):
            tamanho = os.path.getsize(arquivo)
            print(f"✓ {arquivo} encontrado ({tamanho} bytes)")
        else:
            print(f"✗ {arquivo} NÃO encontrado!")
            todos_ok = False

    return todos_ok

def verificar_personalizacao():
    """Verifica se os arquivos foram personalizados"""
    print("\n" + "=" * 60)
    print("VERIFICAÇÃO DE PERSONALIZAÇÃO")
    print("=" * 60)

    import os

    arquivos_para_verificar = [
        ('questao1.py', '[SEU NOME]'),
        ('questao2.py', '[SEU NOME]'),
        ('questao3.py', '[SEU NOME]'),
        ('questao4.py', '[SEU NOME]'),
        ('questao4.py', '4297914', 'RU')
    ]

    avisos = []

    for item in arquivos_para_verificar:
        arquivo = item[0]
        placeholder = item[1]
        tipo = item[2] if len(item) > 2 else 'nome'

        if os.path.exists(arquivo):
            with open(arquivo, 'r', encoding='utf-8') as f:
                conteudo = f.read()
                if placeholder in conteudo:
                    avisos.append(f"⚠ {arquivo}: Ainda contém placeholder '{placeholder}' ({tipo})")

    if avisos:
        for aviso in avisos:
            print(aviso)
        print("\n⚠ LEMBRE-SE: Você precisa personalizar nome e RU antes de entregar!")
        return False
    else:
        print("✓ Todos os arquivos parecem estar personalizados!")
        return True

def main():
    """Função principal"""
    print("\n" + "=" * 60)
    print("TESTE DE INSTALAÇÃO - RCP LPA MÓDULO A")
    print("=" * 60)
    print("\nEste script verifica se seu ambiente está pronto para executar")
    print("os programas das questões.\n")

    resultados = []

    # Verificar Python
    resultados.append(("Python", verificar_python()))

    # Verificar bibliotecas
    resultados.append(("Bibliotecas", verificar_bibliotecas()))

    # Verificar arquivos
    resultados.append(("Arquivos", verificar_arquivos()))

    # Verificar personalização
    resultados.append(("Personalização", verificar_personalizacao()))

    # Resumo final
    print("\n" + "=" * 60)
    print("RESUMO")
    print("=" * 60)

    todos_ok = True
    for nome, resultado in resultados:
        status = "✓ OK" if resultado else "✗ FALHOU"
        print(f"{nome}: {status}")
        if not resultado and nome != "Personalização":
            todos_ok = False

    print("\n" + "=" * 60)
    if todos_ok:
        print("✓ AMBIENTE PRONTO! Você pode executar os programas.")
        print("\nPara executar uma questão, use:")
        print("  wsl python3 questao1.py")
        print("  wsl python3 questao2.py")
        print("  etc...")
    else:
        print("⚠ ALGUNS PROBLEMAS ENCONTRADOS!")
        print("Consulte o README.md para soluções.")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()

