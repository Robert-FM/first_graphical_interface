import customtkinter as ctk

#Configuração de aparência
ctk.set_appearance_mode('dark')

#Criação das funções de funcioanlidade
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    #verificar usuario
    if usuario == 'Robert' and  senha == '88087666':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
    else:
        resultado_login.configure(text='Login/senha incorreto', text_color='red')

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