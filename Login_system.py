import pandas as pd
import database
import login

Login_usuario = input("Entra com o seu email para continuar:")
login_senha_usuario = input("Agora digite sua senha para terminar:")

if Login_usuario == database.Dados_pessoas and login_senha_usuario == database.Dados_senha:
    print(f"Bem vindo {database.Dados_Nome_Usuario} {database.Dados_Sobrenome_Usuario}")
else:
    print("Senha de usuario ou email incorretos")

