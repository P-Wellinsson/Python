from math import radians, sin, cos, tan
a = float(input('\033[33;42mDigite o ângulo que você deseja:\033[m\033[33m '))
print(f'\033[m\033[35mO ângulo de {a} tem o seno de {sin(radians(a)):.2f}')
print(f'O ângulo de {a} tem o cosseno de {cos(radians(a)):.2f}')
print(f'O ângulo de {a} tem o tangente de {tan(radians(a)):.2f}\033[m')
