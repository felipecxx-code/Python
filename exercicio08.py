# Exercício 8
# No código abaixo, são mostradas algumas linhas para manipulação de números em horas. Adicione os comentários apropriados para deixar o código mais inteligível.

# O código foi gerado inicialmente por causa desse enunciado:

# Você está enchendo uma piscina e tem duas mangueiras. A mangueira verde enche em 1,5 horas e a mangueira azul em 1,2 horas. Você deseja acelerar o processo usando as duas mangueiras. Quanto tempo levará usando as duas mangueiras, em minutos?

# Por fim, preveja qual vai ser o valor da variável time, escrevendo a resposta como comentário

# variáveis para definir o tempo de cada mangueira em horas

time_green = 1.5
time_blue = 1.2

# variável para transformar o tempo em horas para minutos

minutes_green = 60 * time_green
minutes_blue = 60 * time_blue

# Taxa de vazão de cada mangueira por minuto

rate_hose_green = 1 / minutes_green
rate_hose_blue = 1 / minutes_blue

# Taxa de vazão das duas mangueiras juntas

rate_host_combined = rate_hose_green + rate_hose_blue

# Tempo para encher a piscina

time = 1 / rate_host_combined

# Escreva neste comentário qual será o valor de time no final da execução do código

# Resposta A piscina encherá em 40 minutos utilizando as duas mangueiras juntas.