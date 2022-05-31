"""
Tipos de dados em python

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
---------------------------------------------
Tipo de texto:	str
Tipos Numéricos:	int, float, complex
Tipos de sequência:	list, tuple, range
Tipo de mapeamento:	dict
Tipos de conjunto:	set,frozenset
Tipo booleano:	bool
Tipos binários:	bytes, bytearray, memoryview
Nenhum Tipo:	NoneType
"""
texto = "nome de pessoas"

inteiro = 45

decimal = 45.7

boleano = True

# uma lista pode ter valores de diferentes tipos, inclusive outras listas dentro dela
lista = ["banana", "morango", 45, 70, True, ["Manga", "pêssigo"] ]

dados_aluno = {"nome": "Mateus", "idade": 25}

tupla = ("banana", "morango", 45, 70, True, ["Manga", "pêssigo"])

conjunto = {45, 67, 89}
"""
print(type(texto))
print(type(inteiro))
print(type(decimal))
print(type(boleano))
print(type(lista))
print(type(dados_aluno))
print(type(conjunto))
print(type(tupla))
"""

# Conversão de tipo

x = 34
y = 19.7
z = 1j

x_float = float(x)

print(type(x))
print(type(x_float))

y_int = int(y)
print(y_int)

print(type(y))
print(type(y_int))

x_complex = complex(x)
print(x_complex)

"""
z_int = int(z) não é possivel converter do tipo complexo para o tipo inteiro
print(z_int)
"""

x_range = range(10)
print(x_range)
print(type(x_range))

import random

x_radom = random.randrange(1, 10)
print(x_radom)