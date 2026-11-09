Title: Padrão Strategy em Python com um exemplo de RPG
Date: 2026-11-02 09:00
Modified: 2026-11-02 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Entenda o padrão de projeto Strategy de forma simples, usando personagens de um RPG de turno como exemplo.

No 9° encontro tivemos a palestra **Padrões de Projeto em RPGs de Turno**, e jogos são mesmo um ótimo jeito de entender padrões de projeto. Neste post vamos ver um dos mais úteis no dia a dia: o **Strategy**.

## O problema

Imagine um RPG onde cada personagem ataca de um jeito: o guerreiro usa a espada, o mago lança magia, o arqueiro dispara flechas. O primeiro impulso é encher o código de `if`:

```python
def atacar(personagem):
    if personagem.classe == "guerreiro":
        return 10
    elif personagem.classe == "mago":
        return 15
    elif personagem.classe == "arqueiro":
        return 8
```

Funciona, mas cada nova classe de personagem obriga a mexer nessa função. Com o tempo ela vira um monstro maior que o chefe final.

## A solução com Strategy

A ideia do Strategy é separar o **comportamento** em objetos próprios e deixar o personagem apenas usar a estratégia que recebeu:

```python
from dataclasses import dataclass
from typing import Protocol


class Ataque(Protocol):
    def executar(self) -> int: ...


class Espada:
    def executar(self) -> int:
        return 10


class BolaDeFogo:
    def executar(self) -> int:
        return 15


@dataclass
class Personagem:
    nome: str
    ataque: Ataque

    def atacar(self) -> str:
        return f"{self.nome} causou {self.ataque.executar()} de dano!"


heroi = Personagem("Bruna", Espada())
print(heroi.atacar())  # Bruna causou 10 de dano!

heroi.ataque = BolaDeFogo()  # trocou de estratégia em pleno combate
print(heroi.atacar())  # Bruna causou 15 de dano!
```

## O jeito ainda mais pythônico

Em Python, funções são objetos. Se a estratégia é só um comportamento, uma função já resolve:

```python
def espada() -> int:
    return 10


def flecha() -> int:
    return 8


estrategias = {"espada": espada, "flecha": flecha}
print(estrategias["flecha"]())  # 8
```

## Quando usar

- Quando existem várias formas de fazer a mesma coisa;
- Quando o comportamento precisa mudar em tempo de execução;
- Quando aquele `if/elif` não para de crescer.

Gostou? Sugira o próximo padrão que devemos explicar no nosso [repositório](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
