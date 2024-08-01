# Exercício 10
# Escreva um código que funcione de acordo com o enunciado

# Você está enchendo uma piscina e tem 3 mangueiras. A mangueira vermelha enche em 2 horas, a mangueira azul leva 1,2 hora e a mangueira amarela em 1 hora. Você deseja acelerar o processo usando as três mangueiras. Quanto tempo levará usando todas as mangueiras, em minutos?

# Escreva seu código aqui

# Tempo em horas
mangueira_Vermelha = 2
mangueira_Azul = 1.2
mangueira_Amarela = 1

# Tempo em minutos
min_Vermelha = 60 * mangueira_Vermelha
min_Azul = 60 * mangueira_Azul
min_Amarela = 60 * mangueira_Amarela

# Taxa de Vazão
v_MangVer = 1 / min_Vermelha
v_MangAz = 1 / min_Azul
v_ManAma = 1 / min_Amarela

# Taxa de Vazão com as 3 mangueiras juntas

txVz_Juntas = v_MangVer + v_MangAz + v_ManAma

# Tempo para completar a encher a piscina em minutos
tempo = 1 / txVz_Juntas 
print(f'{tempo:.1f}')
