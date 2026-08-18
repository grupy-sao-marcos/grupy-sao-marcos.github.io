Title: Tratamento de erros em Python: trabalhando com exceções
Date: 2026-08-27 09:00
Modified: 2026-08-27 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Aprenda a tratar erros em Python usando try/except, criar exceções personalizadas e escrever código que não quebra quando algo dá errado.

Todo programa encontra situações inesperadas: arquivo que não existe, conexão que cai, dado com formato errado. Quando isso acontece e o Python não sabe o que fazer, ele lança uma **exceção** e o programa para abruptamente.

O tratamento de erros é o que separa um programa que funciona "quase sempre" de um que funciona **de verdade**. Vamos aprender a lidar com exceções de forma correta.

## O bloco try/except

A estrutura básica é simples:

```python
try:
    # código que pode dar erro
    resultado = 10 / 0
except ZeroDivisionError:
    # o que fazer quando o erro acontece
    print("Não é possível dividir por zero")
```

Sem o `try/except`, o Python mostraria um traceback e encerraria o programa. Com ele, o erro é tratado e o programa continua rodando.

## Capturando diferentes erros

Você pode tratar tipos diferentes de erro em blocos separados:

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Isso não é um número válido")
except ZeroDivisionError:
    print("Não pode dividir por zero")
```

Cada `except` lida com um tipo específico de erro. Isso permite dar mensagens mais úteis ao usuário.

## Capturando o erro

Você pode acessar o objeto da exceção para mais detalhes:

```python
try:
    arquivo = open("dados.txt")
    conteudo = arquivo.read()
except FileNotFoundError as erro:
    print(f"Arquivo não encontrado: {erro}")
```

O `as erro` guarda a exceção em uma variável que você pode usar para debug ou logging.

## Finally: executar sempre

O bloco `finally` é executado **sempre**, ocorreu erro ou não. É útil para liberar recursos:

```python
try:
    arquivo = open("dados.txt")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado")
finally:
    print("Fim do processamento")
```

Outro uso comum é fechar conexões ou arquivos:

```python
conexao = None
try:
    conexao = abrir_conexao()
    conexao.executar("SELECT * FROM usuarios")
except ErroConexao:
    print("Falha ao conectar ao banco")
finally:
    if conexao:
        conexao.fechar()
```

## Exceções comuns do Python

O Python já vem com muitas exceções prontas. As mais comuns:

| Exceção | Quando acontece |
|---------|-----------------|
| `ValueError` | Valor no formato errado (`int("abc")`) |
| `TypeError` | Operação com tipo incompatível (`"2" + 2`) |
| `FileNotFoundError` | Arquivo não existe |
| `KeyError` | Chave não encontrada em dict (`d["x"]` em dict vazio) |
| `IndexError` | Índice fora do range de uma lista |
| `AttributeError` | Atributo ou método não existe |
| `ImportError` | Módulo não encontrado ao importar |

## Criando exceções personalizadas

Em projetos maiores, você pode querer criar suas próprias exceções para representar erros específicos do seu domínio:

```python
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor):
        self.saldo = saldo
        self.valor = valor
        super().__init__(
            f"Saldo insuficiente: tem R${saldo}, "
            f"tentou tirar R${valor}"
        )

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError(saldo, valor)
    return saldo - valor

# Usando
try:
    novo_saldo = sacar(100, 150)
except SaldoInsuficienteError as e:
    print(e)
    # Saída: Saldo insuficiente: tem R$100, tentou tirar R$150
```

## Práticas recomendadas

### Não engula erros silenciosamente

```python
# Ruim: engole o erro sem fazer nada
try:
    processar_dados()
except Exception:
    pass

# Bom: pelo menos registre o erro
try:
    processar_dados()
except Exception as e:
    logging.error(f"Erro ao processar dados: {e}")
```

### Seja específico

```python
# Ruim: captura qualquer coisa
try:
    abrir_arquivo()
except Exception:
    print("Erro")

# Bom: captura apenas o que espera
try:
    abrir_arquivo()
except FileNotFoundError:
    print("Arquivo não encontrado")
except PermissionError:
    print("Sem permissão para ler o arquivo")
```

### Não use exceções para fluxo normal

```python
# Ruim: usar exceção como lógica de negócio
try:
    valor = dicionario[chave]
except KeyError:
    valor = valor_padrao

# Bom: usar o método seguro do dict
valor = dicionario.get(chave, valor_padrao)
```

## Resumo

- Use `try/except` para capturar erros esperados
- Seja específico nos tipos de exceção que captura
- Use `finally` para liberar recursos
- Crie exceções personalizadas em projetos maiores
- Nunca use `except Exception: pass` — pelo menos registre o erro

Tratar erros corretamente faz seu programa ser mais robusto e mais fácil de depurar quando algo dá errado. É uma das habilidades que mais faz diferença no dia a dia de um desenvolvedor.
