print("**************************")
print("Teste de condição 'if' - 1")
print("**************************")

minha_idade = 26
idade_namorado = 25
if(minha_idade == idade_namorado):
    print("Resposta>>>>>Temos idades iguais")
else:
    print("Resposta>>>>>Temos idades diferentes")

print("**************************")
print("Teste de condição 'if' - 2")
print("**************************")

usuario = input("Agora informe o usuário da pessoa:")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
elif(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
elif(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")
