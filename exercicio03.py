# Exercício 3
# Tarefa - Fazer 
# Escreva um programa que produza uma história. A história e a conclusão da história devem sair em várias linhas.

# Tarefa - Fazer

# Escreva um programa que gere uma história com várias linhas.
print('O Leão e o Javali')
print('Num dia muito quente, um leão e um javali chegaram juntos a um poço.')
print('Estavam com muita sede e começaram a discutir para ver quem beberia primeiro.')
print('— Olhe lá! — disse o leão. — Aqueles urubus estão com fome e esperam para ver qual de nós dois será derrotado.')
print('— Então, é melhor fazermos as pazes — respondeu o javali. — Prefiro ser seu amigo a ser comida de urubus.')
print(' ')


# Tarefa de extensão 1
# Existe uma maneira de usar uma única instrução de impressão para gerar texto em várias linhas. Crie o programa de história que funciona da mesma forma do que anteriormente, mas usa apenas uma instrução de impressão.#
print('O Leão e o Javali', ''' 
      Num dia muito quente, um leão e um javali chegaram juntos a um poço. Estavam com muita sede e começaram a discutir para ver quem beberia primeiro.Nenhum cedia a vez ao outro. Já iam atracar-se para brigar, quando o leão olhou para cima e viu vários urubus voando.
   — Olhe lá! — disse o leão. — Aqueles urubus estão com fome e esperam para ver qual de nós dois será derrotado.
   — Então, é melhor fazermos as pazes — respondeu o javali. — Prefiro ser seu amigo a ser comida de urubus. ''')
print(' ')



# Tarefa de extensão 2
# Existe uma maneira de adicionar um atraso de tempo no código python. Faça alguma pesquisa e crie um programa de história que produza a história e atrase antes de gerar a conclusão.

import time
time.sleep(1)
print('O Leão e o Javali')
time.sleep(2)
print('Num dia muito quente, um leão e um javali chegaram juntos a um poço.')
time.sleep(2)
print('Estavam com muita sede e começaram a discutir para ver quem beberia primeiro.')
time.sleep(2)
print('— Olhe lá! — disse o leão. — Aqueles urubus estão com fome e esperam para ver qual de nós dois será derrotado.')
time.sleep(2)
print('— Então, é melhor fazermos as pazes — respondeu o javali. — Prefiro ser seu amigo a ser comida de urubus.')
time.sleep(2)
print(' ')
