Title: Testando seu código com pytest: do jeito certo
Date: 2026-08-18 09:00
Modified: 2026-08-18 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Aprenda a escrever testes automatizados com pytest e descubra por que testar seu código é essencial para projetos que crescem sem quebrar.

Quando seu projeto começa a crescer, chega um momento em que mexer em uma parte do código pode quebrar outra, bem longe dali. É aí que entram os **testes automatizados**: pequenos programas que verificam se seu código continua funcionando como esperado, sem depender de você testar tudo na mão.

O **pytest** é o framework mais popular para testes em Python. Simples, direto e com uma sintaxe que parece português. Vamos aprender na prática.

## Instalando o pytest

Crie um ambiente virtual (veja nosso [artigo sobre ambientes virtuais]({filename}virtual-env.md)) e instale:

```bash
pip install pytest
```

## Nosso primeiro teste

Vamos testar uma função simples. Crie o arquivo `calculadora.py`:

```python
def somar(a: float, b: float) -> float:
    return a + b
```

Agora crie o arquivo de teste `test_calculadora.py`. A convenção é que testes comecem com `test_`:

```python
from calculadora import somar


def test_somar_numeros_positivos():
    assert somar(2, 3) == 5


def test_somar_numeros_negativos():
    assert somar(-1, -1) == -2


def test_somar_zero():
    assert somar(0, 0) == 0
```

Para rodar, execute no terminal:

```bash
pytest
```

O pytest encontra sozinho os arquivos `test_*.py` e executa as funções `test_*`. O resultado será algo assim:

```bash
3 passed in 0.02s
```

O comando `assert` é a ferramenta central: se a expressão for falsa, o teste falha e o pytest mostra exatamente o que era esperado e o que veio.

## Vendo uma falha acontecer

E se alguém quebrar a função `somar` por engano? Vamos simular:

```python
def somar(a: float, b: float) -> float:
    return a + b + 1  # erro introduzido!
```

Rodando o `pytest` novamente:

```bash
FAILED test_calculadora.py::test_somar_numeros_positivos - assert 6 == 5
```

Com o teste em mãos, o erro é encontrado em segundos. Sem ele, o bug poderia passar despercebido por semanas.

## Parametrizando testes

Quando a lógica tem vários casos, o `@pytest.mark.parametrize` evita repetição:

```python
import pytest
from calculadora import somar


@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 5),
    (-1, -1, -2),
    (0, 0, 0),
    (10, -4, 6),
])
def test_somar(a, b, esperado):
    assert somar(a, b) == esperado
```

Agora temos quatro cenários em um único teste, e se um deles falhar, o pytest mostra exatamente qual combinação de valores deu problema.

## Testando com fixtures

As **fixtures** preparam dados ou recursos antes do teste. É muito útil quando vários testes precisam da mesma configuração:

```python
import pytest


@pytest.fixture
def usuarios():
    return [
        {"nome": "Maria", "idade": 28},
        {"nome": "João", "idade": 15},
    ]


def test_maioridade(usuarios):
    maiores = [u for u in usuarios if u["idade"] >= 18]
    assert len(maiores) == 1
    assert maiores[0]["nome"] == "Maria"
```

A fixture é criada antes do teste e o resultado é passado como argumento. Simples e elegante.

## Testando o que deve levantar erro

Para verificar que uma função falha quando deveria, usamos `pytest.raises`:

```python
import pytest


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Divisao por zero nao permitida")
    return a / b


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)
```

Aqui o teste passa **porque** a função levantou `ValueError`, exatamente como esperado.

## Organização do projeto

Conforme o projeto cresce, organize os testes em uma pasta separada:

```text
meu_projeto/
├── app.py
├── calculadora.py
└── tests/
    ├── test_calculadora.py
    └── test_app.py
```

Rodando apenas os testes da pasta `tests`:

```bash
pytest tests
```

## Testes não são "perda de tempo"

É comum achar que testar atrasa o desenvolvimento, mas a realidade é o contrário:

- Você muda o código **com confiança**;
- Bugs aparecem **antes** de chegar ao usuário;
- O teste serve como **documentação** viva de como a função deve se comportar;
- No futuro, a manutenção fica muito mais barata.

Comece testando as funções mais importantes do seu projeto. Aos poucos, cobrir tudo vira um hábito natural.

Testou seu código e encontrou um erro? Conta pra gente nos comentários ou contribua com um artigo no nosso [repositorio](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
