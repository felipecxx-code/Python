# Exercício 16
# Escreva um código que funcione de acordo com o enunciado

# Quatro amigas foram ao shopping comprar roupas. A amiga 1 levou R$240,00. A amiga 2 levou dois terços (2/3) do valor da amiga 1. A amiga 3 levou 3 vezes o valor da amiga 2. A amiga 4 levou o valor somado das amigas 2 e 3.

# Faça um programa que calcule o valor total que as quatro amigas levaram para o shopping. 

# Escreva seu código aqui

amiga1 = 240
amiga2 = (2/3) * amiga1
amiga3 = 3 * amiga2
amiga4 = amiga2 + amiga3

valorTotal = amiga1 + amiga2 + amiga3 + amiga4
print(f'O valor total das 4 amigas juntos: R$ {valorTotal:.2f}')