import random
import string

def gerar_senha(tamanho, opcao):
    opcoes = {
        1: string.ascii_letters,
        2: string.digits,
        3: string.ascii_letters + string.digits + string.punctuation,
        4: string.ascii_letters + string.digits + string.punctuation,
    }
    caracteres = opcoes.get(opcao, string.ascii_letters + string.digits + string.punctuation)
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

print("Escolha o tipo de senha:")
print("1 - Apenas caracteres")
print("2 - Apenas números")
print("3 - Caracteres e números")
print("4 - Aleatório")

opcao_escolhida = int(input("Digite o número da opção desejada: "))
tamanho_senha = int(input("Digite o tamanho da senha desejado: "))

senhas_geradas = [gerar_senha(tamanho_senha, opcao_escolhida) for _ in range(3)]

print("\nSenhas geradas:")
for i, senha in enumerate(senhas_geradas, start=1):
    print(f"Senha {i}:")
    print(senha)
    print()
