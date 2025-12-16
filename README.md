# RCP LPA Módulo A - Trabalho de Recuperação de Conceito

Este repositório contém as 5 questões do trabalho de Recuperação de Conceito (RCP) de Lógica de Programação e Algoritmos, desenvolvidas em Python.

## 📋 Índice

1. [Estrutura dos Arquivos](#estrutura-dos-arquivos)
2. [Pré-requisitos](#pré-requisitos)
3. [Instalação do Python](#instalação-do-python)
4. [Verificação da Instalação](#verificação-da-instalação)
5. [Personalização dos Programas](#personalização-dos-programas)
6. [Como Executar os Programas](#como-executar-os-programas)
7. [Descrição Detalhada das Questões](#descrição-detalhada-das-questões)
8. [Exemplos de Uso](#exemplos-de-uso)
9. [Solução de Problemas](#solução-de-problemas)

---

## 📁 Estrutura dos Arquivos

```
rcp/
├── questao1.py          # Sistema de Planos de Saúde
├── questao2.py          # Sistema de Pizzaria
├── questao3.py          # Sistema de Venda de Toras
├── questao4.py          # Sistema de Gerenciamento de Contatos
├── questao5.py          # Sistema de BINGO
├── README.md             # Este arquivo
└── RCP LPA Modulo A.pdf  # Documentação do trabalho
```

---

## 🔧 Pré-requisitos

Antes de executar os programas, você precisa ter:

- **Python 3.6 ou superior** instalado
- **WSL (Windows Subsystem for Linux)** - se estiver usando Windows
- **Terminal/Console** para executar os comandos

### Bibliotecas Necessárias

Os programas utilizam apenas bibliotecas padrão do Python:
- `random` - para geração de números aleatórios (Questão 5)
- `copy` - para cópia de dicionários (Questão 4)

**Não é necessário instalar bibliotecas externas!**

---

## 💻 Instalação do Python

### No Windows (usando WSL)

Se você está usando Windows e tem WSL instalado, o Python geralmente já vem pré-instalado. Para verificar:

```bash
wsl python3 --version
```

Se o Python não estiver instalado no WSL, execute:

```bash
wsl sudo apt update
wsl sudo apt install python3 python3-pip -y
```

### No Linux/Mac

O Python geralmente já vem instalado. Para verificar:

```bash
python3 --version
```

Se não estiver instalado:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

**macOS (usando Homebrew):**
```bash
brew install python3
```

### Instalação Direta no Windows (sem WSL)

1. Acesse: https://www.python.org/downloads/
2. Baixe a versão mais recente do Python 3.x
3. Durante a instalação, **marque a opção "Add Python to PATH"**
4. Complete a instalação

---

## ✅ Verificação da Instalação

### Teste Automático (Recomendado)

Execute o script de teste para verificar se tudo está configurado corretamente:

```bash
wsl python3 testar_instalacao.py
```

Este script verifica:
- ✓ Versão do Python
- ✓ Bibliotecas necessárias
- ✓ Existência dos arquivos
- ⚠️ Personalização (nome e RU)

### Verificar se o Python está instalado

**No WSL:**
```bash
wsl python3 --version
```

**No Linux/Mac:**
```bash
python3 --version
```

**No Windows (PowerShell/CMD):**
```bash
python --version
# ou
py --version
```

### Verificar onde o Python está instalado

**No WSL:**
```bash
wsl which python3
```

**No Linux/Mac:**
```bash
which python3
```

**No Windows:**
```bash
where python
```

### Exemplo de saída esperada:

```
Python 3.10.12
```

Se você ver uma mensagem de versão, o Python está instalado corretamente!

---

## ✏️ Personalização dos Programas

Antes de executar os programas, você **DEVE** personalizar as seguintes informações:

### 1. Questão 1, 2, 3, 4 e 5 - Nome e Sobrenome

Abra cada arquivo e substitua `[SEU NOME] [SEU SOBRENOME]` pelo seu nome completo.

**Exemplo:**
```python
# ANTES:
print("Desenvolvido por: [SEU NOME] [SEU SOBRENOME]")

# DEPOIS:
print("Desenvolvido por: João Silva")
```

**Arquivos a editar:**
- `questao1.py` - linha ~8
- `questao2.py` - linha ~8
- `questao3.py` - linha ~8
- `questao4.py` - linha ~8
- `questao5.py` - não tem mensagem de boas-vindas, mas precisa informar a sigla quando solicitado

### 2. Questão 4 - Número de RU

Abra o arquivo `questao4.py` e substitua o número de RU:

```python
# ANTES:
id_global = 4297914  # SUBSTITUIR PELO SEU RU

# DEPOIS:
id_global = 1234567  # Seu número de RU aqui
```

**Localização:** `questao4.py` - linha ~12

### 3. Questão 5 - Sigla

Na Questão 5, quando o programa solicitar, digite sua sigla (primeira letra do nome + primeira letra do sobrenome).

**Exemplo:** Se seu nome é "João Silva", sua sigla será "JS"

---

## 🚀 Como Executar os Programas

### Método 1: Usando WSL (Recomendado para Windows)

1. **Abra o PowerShell ou CMD no Windows**

2. **Navegue até a pasta do projeto:**
```bash
cd D:\workspace-private\rcp
```

3. **Execute os programas usando WSL:**
```bash
# Questão 1
wsl python3 questao1.py

# Questão 2
wsl python3 questao2.py

# Questão 3
wsl python3 questao3.py

# Questão 4
wsl python3 questao4.py

# Questão 5
wsl python3 questao5.py
```

### Método 2: Diretamente no WSL

1. **Abra o terminal do WSL:**
   - Pressione `Win + R`
   - Digite `wsl` e pressione Enter
   - Ou procure por "Ubuntu" no menu Iniciar

2. **Navegue até a pasta do projeto:**
```bash
cd /mnt/d/workspace-private/rcp
```

3. **Execute os programas:**
```bash
python3 questao1.py
python3 questao2.py
python3 questao3.py
python3 questao4.py
python3 questao5.py
```

### Método 3: No Linux/Mac

1. **Abra o Terminal**

2. **Navegue até a pasta do projeto:**
```bash
cd /caminho/para/o/projeto/rcp
```

3. **Execute os programas:**
```bash
python3 questao1.py
python3 questao2.py
python3 questao3.py
python3 questao4.py
python3 questao5.py
```

### Método 4: No Windows (sem WSL)

1. **Abra o PowerShell ou CMD**

2. **Navegue até a pasta do projeto:**
```bash
cd D:\workspace-private\rcp
```

3. **Execute os programas:**
```bash
python questao1.py
# ou
py questao1.py
```

**Nota:** Use `python` ou `py` dependendo de como o Python foi instalado no seu Windows.

---

## 📖 Descrição Detalhada das Questões

### Questão 1 - Sistema de Planos de Saúde

**Objetivo:** Calcular o valor mensal de um plano de saúde baseado na idade do cliente.

**Funcionalidades:**
- Solicita valor base do plano e idade do cliente
- Aplica percentuais diferentes conforme faixas etárias:
  - 0-18 anos: 100%
  - 19-28 anos: 150%
  - 29-38 anos: 225%
  - 39-48 anos: 240%
  - 49-58 anos: 350%
  - 59+ anos: 600%
- Exibe o valor mensal calculado

**Exemplo de uso:**
```
Digite o valor base do plano: R$ 100.00
Digite a idade do cliente: 45
Valor mensal do plano: R$ 240.00
```

---

### Questão 2 - Sistema de Pizzaria

**Objetivo:** Sistema de pedidos de pizzas com validação e acumulação de valores.

**Funcionalidades:**
- Menu de pizzas (Salgadas e Doces)
- Validação de sabor (PS/PD) e tamanho (P/M/G)
- Preços:
  - P: PS=R$30, PD=R$34
  - M: PS=R$45, PD=R$48
  - G: PS=R$60, PD=R$66
- Permite múltiplos pedidos
- Calcula valor total

**Exemplo de uso:**
```
Digite o sabor da pizza (PS para Salgada ou PD para Doce): PS
Digite o tamanho da pizza (P, M ou G): M
Pizza adicionada! Valor: R$ 45.00
Deseja pedir mais alguma coisa? (sim/não): sim
...
Valor total do pedido: R$ 111.00
```

---

### Questão 3 - Sistema de Venda de Toras

**Objetivo:** Sistema de vendas de toras de madeira com cálculo de descontos e transporte.

**Funcionalidades:**
- Tipos de madeira:
  - PIN: R$ 150,40/m³
  - PER: R$ 170,20/m³
  - MOG: R$ 190,90/m³
  - IPE: R$ 210,10/m³
  - IMB: R$ 220,70/m³
- Descontos por quantidade:
  - < 100 m³: 0%
  - 100-499 m³: 4%
  - 500-999 m³: 9%
  - 1000-2000 m³: 16%
  - > 2000 m³: não aceito
- Transporte:
  - Rodoviário: R$ 1.000,00
  - Ferroviário: R$ 2.000,00
  - Hidroviário: R$ 2.500,00

**Exemplo de uso:**
```
Digite o tipo de madeira (PIN/PER/MOG/IPE/IMB): PIN
Digite a quantidade de toras (em m³): 500
Digite a opção de transporte (1-Rodoviário, 2-Ferroviário, 3-Hidroviário): 1
TOTAL A PAGAR: R$ 69336.00
```

---

### Questão 4 - Sistema de Gerenciamento de Contatos

**Objetivo:** Sistema CRUD completo para gerenciamento de contatos comerciais.

**Funcionalidades:**
- Cadastrar contatos (ID, Nome, Atividade, Telefone)
- Consultar contatos:
  - Todos os contatos
  - Por ID
  - Por Atividade
- Remover contatos
- ID inicia com seu número de RU

**Exemplo de uso:**
```
1) Cadastrar Contato
2) Consultar Contato
3) Remover Contato
4) Encerrar Programa
Digite a opção desejada: 1
Digite o nome do contato: João Silva
Digite a atividade do contato: Estudante
Digite o telefone do contato: 1234567
Contato cadastrado com sucesso! ID: 4297914
```

---

### Questão 5 - Sistema de BINGO

**Objetivo:** Sistema completo de BINGO com geração de cartelas e verificação de ganhadores.

**Funcionalidades:**
- Gerar cartelas 5x5 com números aleatórios
- Definir regras:
  - Linha, Coluna ou Diagonal
  - Cartela Cheia
- Sortear números (1-75)
- Verificar ganhadores automaticamente
- Exibir cartela vencedora

**Exemplo de uso:**
```
1) Gerar Cartelas
2) Definir Regras
3) Começar Bingo!
4) Encerrar Programa
Digite a opção desejada: 1
Quantas cartelas devem ser geradas? 100
Digite sua sigla (2 letras): JS
100 cartelas geradas com sucesso!
```

---

## 💡 Exemplos de Uso

### Executando a Questão 1

```bash
# No WSL
wsl python3 questao1.py

# Saída esperada:
# Bem-vindo ao Sistema de Planos de Saúde!
# Desenvolvido por: [SEU NOME] [SEU SOBRENOME]
# Digite o valor base do plano: R$ 100.00
# Digite a idade do cliente: 45
# Valor mensal do plano: R$ 240.00
```

### Executando a Questão 2

```bash
wsl python3 questao2.py

# Interação esperada:
# 1. Digite o sabor (PS/PD)
# 2. Digite o tamanho (P/M/G)
# 3. Pergunta se deseja continuar
# 4. Exibe valor total
```

### Executando a Questão 3

```bash
wsl python3 questao3.py

# Interação esperada:
# 1. Escolha o tipo de madeira
# 2. Informe a quantidade (m³)
# 3. Escolha o transporte
# 4. Exibe o total a pagar
```

### Executando a Questão 4

```bash
wsl python3 questao4.py

# Interação esperada:
# 1. Menu principal com 4 opções
# 2. Cadastrar, consultar ou remover contatos
# 3. Consultas por ID, atividade ou todos
```

### Executando a Questão 5

```bash
wsl python3 questao5.py

# Interação esperada:
# 1. Gerar cartelas (informe quantidade e sigla)
# 2. Definir regras (1 ou 2)
# 3. Começar o Bingo (sorteios automáticos)
# 4. Exibe cartela vencedora quando houver ganhador
```

---

## 🔍 Solução de Problemas

### Problema: "python3: command not found"

**Solução:**
```bash
# No WSL
wsl sudo apt update
wsl sudo apt install python3 -y
```

### Problema: "Permission denied"

**Solução:**
```bash
# Dar permissão de execução aos arquivos
chmod +x questao1.py questao2.py questao3.py questao4.py questao5.py
```

### Problema: "No module named 'random'"

**Solução:**
Isso não deveria acontecer, pois `random` é biblioteca padrão. Verifique se está usando Python 3:
```bash
python3 --version
```

### Problema: Erro de codificação (acentos)

**Solução:**
Os arquivos já estão configurados com `# -*- coding: utf-8 -*-`. Se ainda houver problemas, certifique-se de que o terminal suporta UTF-8.

### Problema: Não consigo executar no Windows

**Solução:**
1. Verifique se o Python está no PATH:
   ```bash
   python --version
   ```
2. Se não funcionar, use o WSL (recomendado):
   ```bash
   wsl python3 questao1.py
   ```

### Problema: Erro ao executar no WSL

**Solução:**
1. Certifique-se de estar na pasta correta:
   ```bash
   wsl pwd
   ```
2. Liste os arquivos para verificar:
   ```bash
   wsl ls -la
   ```
3. Execute com caminho completo:
   ```bash
   wsl python3 /mnt/d/workspace-private/rcp/questao1.py
   ```

---

## 📝 Observações Importantes

1. ✅ Todos os códigos estão devidamente comentados conforme as exigências
2. ✅ Os programas seguem todas as especificações do documento RCP LPA Módulo A
3. ⚠️ **Lembre-se de substituir os placeholders (nome, RU, etc.) antes de entregar o trabalho**
4. ✅ Teste todos os programas antes de entregar para garantir que estão funcionando corretamente
5. ✅ Os programas foram testados e estão funcionando corretamente

---

## 🧪 Testes Recomendados

Para cada questão, siga os exemplos de saída de console especificados no documento PDF (`RCP LPA Modulo A.pdf`) para validar o funcionamento correto.

### Checklist de Testes:

- [ ] Questão 1: Testar com idade >= 29 anos
- [ ] Questão 2: Testar erro de sabor, erro de tamanho, múltiplos pedidos
- [ ] Questão 3: Testar erro de tipo, quantidade > 2000, valor não numérico
- [ ] Questão 4: Cadastrar seu contato (nome completo, atividade "Estudante", telefone = RU), cadastrar mais 2 contatos, consultar todos, consultar por ID, consultar por atividade, remover contato
- [ ] Questão 5: Gerar 100 cartelas, definir regra "Cartela Cheia", iniciar Bingo, depois definir regra "Linha/Coluna/Diagonal", iniciar Bingo novamente

---

## 📞 Suporte

Se encontrar problemas ao executar os programas:

1. Verifique se o Python está instalado corretamente
2. Verifique se está na pasta correta
3. Verifique se personalizou nome e RU nos arquivos
4. Consulte a seção "Solução de Problemas" acima

---

**Boa sorte com o trabalho! 🎓**
