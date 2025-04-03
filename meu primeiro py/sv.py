print("seja vemm vindo a magazine lira")
print()
print("vamos criar sua conta!")

usuario = input("digite seu usuario:")
senha  = input("digite sua senha:")

print("conta criada com sucesso !")

print("vamos entrar na sua conta!")

usuario_log = input("digite seu usuario:")
senha_log = input("digite sua senha:")

if usuario_log == usuario and senha_log == senha:
    print("acesso libeerado")
else:
    print("acesso negado!")