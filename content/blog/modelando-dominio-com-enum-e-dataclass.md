Title: Sintaxe perfeita, domínio errado: modelando regras com Enum e dataclass
Date: 2026-11-06 09:00
Modified: 2026-11-06 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Código que roda nem sempre é código certo. Veja como Enum e dataclasses ajudam a deixar as regras do negócio explícitas no seu código Python.

Inspirado na palestra **Sintaxe perfeita, domínio errado**, do 11° encontro: um código pode estar impecável, passar no linter e mesmo assim não representar o problema real. Vamos ver como algumas ferramentas do Python ajudam a aproximar o código do **domínio**.

## Strings mágicas

Veja este código de pedidos:

```python
pedido = {"status": "pago", "valor": -50}

if pedido["status"] == "pgo":  # erro de digitação
    print("Enviar pedido")
```

Ele roda sem erro nenhum, mas o pedido nunca será enviado. E um valor negativo passou sem ninguém perceber.

## Use Enum para valores fixos

```python
from enum import Enum


class Status(Enum):
    AGUARDANDO = "aguardando"
    PAGO = "pago"
    ENVIADO = "enviado"


status = Status.PAGO
print(status == Status.PAGO)  # True
```

Agora um `Status.PGO` gera erro na hora, e o editor sugere as opções válidas.

## Proteja as regras na dataclass

```python
from dataclasses import dataclass


@dataclass
class Pedido:
    valor: float
    status: Status = Status.AGUARDANDO

    def __post_init__(self):
        if self.valor <= 0:
            raise ValueError("O valor do pedido deve ser positivo")

    def pagar(self):
        if self.status != Status.AGUARDANDO:
            raise ValueError("Só é possível pagar pedidos aguardando pagamento")
        self.status = Status.PAGO


pedido = Pedido(valor=120.0)
pedido.pagar()
print(pedido.status)  # Status.PAGO

Pedido(valor=-50)  # ValueError: O valor do pedido deve ser positivo
```

A regra "só se paga um pedido que está aguardando" agora vive **dentro** do `Pedido`, e não espalhada em `if` por todo o sistema.

## Use os nomes do negócio

Se o pessoal da empresa fala em "pedido", "faturar" e "despachar", use esses nomes no código. Um `processar_dados(d)` não diz nada; um `faturar(pedido)` diz tudo.

## Dica final

Antes de escrever código, converse com quem entende do negócio. A sintaxe o Python e o linter conferem para você; o domínio, só você.

Contribua com novos artigos no nosso [repositório](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
