import pandas as pd
import Registrer_system

Dados_pessoas = Registrer_system.Email_usuario
Dados_senha = Registrer_system.Senha_usuario
Dados_Nome_Usuario = Registrer_system.Nome_usuario
Dados_Sobrenome_Usuario = Registrer_system.Sobrenome_usuario

print(f"Bem vindo {Dados_Nome_Usuario} {Dados_Sobrenome_Usuario}, sua senha é {Dados_senha} e seu email é {Dados_pessoas}")
