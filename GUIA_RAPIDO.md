# 🚀 Guia Rápido - Como Executar os Programas

## ⚡ Início Rápido (3 passos)

### 1️⃣ Verificar se o Python está instalado

```bash
wsl python3 --version
```

**Se aparecer uma versão (ex: Python 3.10.12)**, você pode pular para o passo 3.

**Se aparecer erro**, instale o Python:

```bash
wsl sudo apt update
wsl sudo apt install python3 -y
```

### 2️⃣ Personalizar os arquivos

**IMPORTANTE:** Antes de executar, você DEVE editar:

1. **Todos os arquivos (questao1.py até questao5.py):**
   - Substitua `[SEU NOME] [SEU SOBRENOME]` pelo seu nome completo

2. **questao4.py:**
   - Substitua `id_global = 4297914` pelo seu número de RU

### 3️⃣ Executar os programas

```bash
# Navegue até a pasta do projeto
cd D:\workspace-private\rcp

# Execute qualquer questão
wsl python3 questao1.py
wsl python3 questao2.py
wsl python3 questao3.py
wsl python3 questao4.py
wsl python3 questao5.py
```

---

## 📋 Comandos Úteis

### Verificar instalação do Python
```bash
wsl python3 --version
```

### Ver onde o Python está instalado
```bash
wsl which python3
```

### Listar arquivos do projeto
```bash
wsl ls -la
```

### Navegar até a pasta do projeto (no WSL)
```bash
wsl cd /mnt/d/workspace-private/rcp
```

---

## 🎯 Execução Rápida de Cada Questão

### Questão 1 - Planos de Saúde
```bash
wsl python3 questao1.py
```
**Entrada esperada:** Valor base e idade

### Questão 2 - Pizzaria
```bash
wsl python3 questao2.py
```
**Entrada esperada:** Sabor (PS/PD), Tamanho (P/M/G), continuar pedindo?

### Questão 3 - Venda de Toras
```bash
wsl python3 questao3.py
```
**Entrada esperada:** Tipo de madeira, quantidade, transporte

### Questão 4 - Contatos
```bash
wsl python3 questao4.py
```
**Entrada esperada:** Menu com opções 1-4

### Questão 5 - BINGO
```bash
wsl python3 questao5.py
```
**Entrada esperada:** Menu com opções 1-4, quantidade de cartelas, sigla

---

## ⚠️ Problemas Comuns

### "python3: command not found"
```bash
wsl sudo apt install python3 -y
```

### "Permission denied"
```bash
chmod +x questao*.py
```

### Não encontra os arquivos
```bash
# Verifique se está na pasta correta
wsl pwd
# Deve mostrar: /mnt/d/workspace-private/rcp
```

---

## ✅ Checklist Antes de Entregar

- [ ] Substituí `[SEU NOME] [SEU SOBRENOME]` em todos os arquivos
- [ ] Substituí o número de RU no questao4.py
- [ ] Testei todas as 5 questões
- [ ] Verifiquei que os programas estão funcionando corretamente
- [ ] Capturei as saídas de console conforme exigido no PDF

---

**Para mais detalhes, consulte o README.md completo!**

