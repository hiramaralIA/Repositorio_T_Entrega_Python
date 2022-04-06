def fatorial(num):
 fat = 1 # Inicialização da variável "fat"
 if num < 0:
  raise Exception('O fatorial de um número negativo não é definido.')
 elif num == 0:
  fat = 1
 else:
  for i in range(1, num + 1):
    fat *= i
 return fat
num = 4
print(f'O fatorial de {num} é {fatorial(num)}.')
