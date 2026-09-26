# Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento 🏭

Este projeto é um protótipo desenvolvido em Python para simular a automação do controle de qualidade e armazenamento em uma linha de montagem industrial. O sistema inspeciona dados de peças fabricadas, filtra itens fora do padrão e organiza os itens aprovados em caixas virtuais de capacidade limitada.

## ⚙️ Funcionalidades

- **Controle de Qualidade Automático:** Avalia instantaneamente o peso, cor e comprimento das peças.
- **Logística de Armazenamento:** Agrupa peças aprovadas em lotes de 10 unidades. A caixa é "fechada" automaticamente quando a capacidade é atingida.
- **Gestão de Dados:** Permite cadastrar, listar, remover peças e visualizar caixas já finalizadas.
- **Relatórios:** Gera um consolidado rápido da operação com detalhamento dos motivos de rejeição.

## 🚀 Como rodar o programa

1. Certifique-se de ter o [Python 3.x](https://www.python.org/) instalado em sua máquina.

2. Clone este repositório:
   ```bash
   git clone https://github.com/the-manning/automacao-industrial-python.git
   ```

3. Acesse a pasta do projeto:
   ```bash
   cd automacao-industrial-python
   ```

4. Execute o arquivo principal no terminal:
   ```bash
   python main.py
   ```

## 💻 Exemplos de Entradas e Saídas

### Exemplo 1: Peça Aprovada

**Entrada (Input):**
```text
ID da Peça: P100
Peso (g): 100
Cor (azul/verde): azul
Comprimento (cm): 15
```

**Saída (Output):**
```text
✅ Peça P100 APROVADA e adicionada à caixa atual.
```

### Exemplo 2: Peça Reprovada (Múltiplos Defeitos)

**Entrada (Input):**
```text
ID da Peça: P101
Peso (g): 85
Cor (azul/verde): vermelho
Comprimento (cm): 15
```

**Saída (Output):**
```text
❌ Peça P101 REPROVADA.
Motivos: Peso fora do padrão (95g - 105g), Cor inválida (deve ser azul ou verde)
```

### Exemplo 3: Fecho de Caixa

**Situação:** O utilizador regista a 10ª peça válida consecutiva.

**Saída (Output):**
```text
✅ Peça P110 APROVADA e adicionada à caixa atual.
📦 CAIXA 1 FECHADA (10 peças atingidas). Nova caixa iniciada.
```

### Exemplo 4: Relatório Final (Opção 5)

**Saída (Output):**
```text
--- 5. RELATÓRIO FINAL ---
✅ Total de Peças Aprovadas: 10
❌ Total de Peças Reprovadas: 1
📦 Quantidade de Caixas Fechadas: 1

--- Motivos das Reprovações ---
Peça ID P101: Peso fora do padrão (95g - 105g), Cor inválida (deve ser azul ou verde)
```
