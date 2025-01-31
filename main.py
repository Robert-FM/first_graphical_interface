import customtkinter as ctk
import os

#Configuração de aparência
ctk.set_appearance_mode('dark')

# Função para validar login
def validar_login():
    usuario_digitado = campo_usuario.get()
    senha_digitada = campo_senha.get()

    if not os.path.exists('senha.csv'):
        resultado_login.configure(text='Erro: Arquivo de usuários não encontrado!', text_color='red')
        return
    
    # Abrir o arquivo CSV e verificar as credenciais
    with open('senha.csv', encoding='utf-8') as arquivo:
        credenciais = [linha.strip() for linha in arquivo]  # Remove espaços e quebras de linha
        if f"{usuario_digitado},{senha_digitada}" in credenciais:
            resultado_login.configure(text='Login feito com sucesso!', text_color='green')
        else:
            resultado_login.configure(text='Login/senha incorretos', text_color='red')

#Criação da janela principal
app = ctk.CTk()
app.title('Sistema K')
app.geometry('300x300')
#Criação dos campos
#Label1
label_usuario = ctk.CTkLabel(app, text='Usuário:')
label_usuario.pack(pady=10)
#Entry1
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)
#Label2
label_senha = ctk.CTkLabel(app, text='Senha:')
label_senha.pack(pady=10)
#Entry2
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite seu senha', show='*')
campo_senha.pack(pady=10)
#Button
botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)
#campo feedback de login
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)

#Iniciar a aplicação
app.mainloop()