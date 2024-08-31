# fibonacci == 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

def fibonacci(valor_verificado):
  
  num1 = 0
  num2 = 1

  while num2 < valor_verificado:

    num1, num2 = num2, num1 + num2 # atualiza os valores de num1 e num2 de acordo com a regra da sequência de Fibonacci
    
  return num2 == valor_verificado

valor_definido = 4 # valor escolhido por mim

if fibonacci(valor_definido): # informa se o valor somado com o numero anterior pertence a sequência de fibonacci
  
  print(f'O numero pertence á sequência de fibonacci: {valor_definido}')

else:
   print(f'O numero não pertence á sequência de fibonacci: {valor_definido}')