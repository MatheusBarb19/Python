import random #Emite caracteres aleatórios
import string 

def gerar_senha(comprimento, incluir_maiusculas=True, incluir_numeros=True, incluir_especiais=True):
    """
    Gera uma senha aleatória com base nos parâmetros
    
    Parâmetros:
    - comprimento (int): comprimento da senha
    - incluir_maisculas(bool): se True, inclui caracteres maíusculos
    - incluir_numeros(bool): se True, inclui caracteres números
    - incluir_especiais(bool): se True, inclui caracteres especiais (!,@,#.....)
    
    Retorna(return):
    - str: senha gerada
    """
    
    #Conjunto básico de caracteres: apenas letras minúsculas
    caracteres = string.ascii_lowercase #Lowercase = minusculas
    
    #Adiciona letras maíusculas, números e caracteres especiais
    
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += string.punctuation

        
    #Garante que o comprimento seja pelo menos 1
    
    if comprimento < 1:
        raise ValueError ("O comprimento da senha deve ser pelo menos 1") # Sinaliza erro
    
    #Gerar senha aleatória
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main(): #função principal que interage com os usuários
    print("Bem-Vindo ao Gerador de Senhas!")
    
    #Solicita ao usuário o comprimento da senha
    
    while True:
        try:
            comprimento = int(input("Digite o comprimento desejado para a senha (mínimo 1): "))
            if comprimento < 1:
                raise ValueError
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido maior que 0.")
            
    #Solicita ao usuário as configurações adicionais   
    incluir_maiusculas = input("incluir letras maísculas? (s/n) ").strip().lower() == "s" #.strip() remove os qualquer espaço em branco
    incluir_numeros = input("incluir números? (s/n) ").strip().lower() == "s"
    incluir_especiais = input("incluir especiais? (s/n) ").strip().lower() == "s"
    
    #Gera a senha com as configurações adicionais
    senha = gerar_senha(comprimento, incluir_maiusculas, incluir_numeros, incluir_especiais)
    
    print(f"Senha gerada: {senha}")
    print("Use-a com responsabildiade e guarde-a em um local seguro!")

# Executa o programa principal apenas se o script for executado diretamente   
if __name__ == "__main__":
    main()
    