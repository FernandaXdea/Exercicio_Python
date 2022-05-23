nome = input('Digite seu nome: ')
print(type(nome))

peso = float (input('informe a seu peso: '))
print(type(peso))

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite mais um numero: '))
s = n1+n2
print('Oi {}, você pesa {} e você informou o numero {} e o {}, a soma entre eles é {}'.format(nome, peso, n1, n2, s))
