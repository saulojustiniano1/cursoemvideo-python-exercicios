print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if (a - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
  print('Os segmentos acima PODEM FORMAR triângulo!')
else:
  print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
