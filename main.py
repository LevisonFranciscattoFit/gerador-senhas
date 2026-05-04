import random
import string

def gerar_senha(tamanho=12, incluir_numeros=True, incluir_especiais=True):
    caracteres = string.ascii_letters
    
    if incluir_numeros:
        caracteres += string.digits
        
    if incluir_especiais:
        caracteres += string.punctuation
        
    senha = "".join(random.choice(caracteres) for i in range(tamanho))
    return senha

if __name__ == '__main__':
    print("="*30)
    print("   GERADOR DE SENHAS SEGURAS   ")
    print("="*30)
    
    try:
        tamanho = int(input("Digite o tamanho da senha (ex: 12): "))
        num = input("Incluir números? (s/n): ").lower() == 's'
        esp = input("Incluir caracteres especiais? (s/n): ").lower() == 's'
        
        senha_gerada = gerar_senha(tamanho=tamanho, incluir_numeros=num, incluir_especiais=esp)
        print(f"\nSenha gerada: {senha_gerada}\n")
    except ValueError:
        print("Por favor, digite um número inteiro válido para o tamanho da senha.")