Registrer_system.py

print("bem vindo a simulação de cadastro de pessoas")

Nome_usuario = input("Para começar Digite seu nome:")
Sobrenome_usuario = input("Agora Digite seu sobrenome:")
Email_usuario = input("Agora digite seu email:")
Senha_usuario = input("Agora digite sua senha:")

if Email_usuario and Senha_usuario and Nome_usuario and Sobrenome_usuario:
    print("cadastro concluido")


Database.py

import pandas as pd
import Registrer_system

Dados_pessoas = Registrer_system.Email_usuario
Dados_senha = Registrer_system.Senha_usuario
Dados_Nome_Usuario = Registrer_system.Nome_usuario
Dados_Sobrenome_Usuario = Registrer_system.Sobrenome_usuario

print(f"Bem vindo {Dados_Nome_Usuario} {Dados_Sobrenome_Usuario}, sua senha é {Dados_senha} e seu email é {Dados_pessoas}")

BONUS

Login_system

import pandas as pd
import database
import login

Login_usuario = input("Entra com o seu email para continuar:")
login_senha_usuario = input("Agora digite sua senha para terminar:")

if Login_usuario == database.Dados_pessoas and login_senha_usuario == database.Dados_senha:
    print(f"Bem vindo {database.Dados_Nome_Usuario} {database.Dados_Sobrenome_Usuario}")
else:
    print("Senha de usuario ou email incorretos")



