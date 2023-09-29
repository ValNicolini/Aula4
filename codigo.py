# botão de iniciar chat
# popup pra entrar no chat
# qdo entrar no chat (aparece para todos)
# a mensagem q vc entrou no chat
# o campo e o botão de enviar mensagem
# a cada mensagem enviada, aparece para todos
# Nome: texto de mensagem
#O FLET -> BACKEND/FRONTEND

import flet as ft

def main(pagina):
    texto = ft.Text('Val Nicolini')

    nome_usuario = ft.TextField(label='Escreva seu nome')

    campo_mensagem = ft.TextField(label='Digite sua mensagem')

    botao_enviar_mensagem = ft.ElevatedButton('Enviar')
    
    def entrar_popup(evento):
       popup.open=True,
       pagina.remove(botao_iniciar),
       pagina.add(campo_mensagem),
       pagina.add(botao_enviar_mensagem),
       pagina.remove(texto),

       pagina.update()
    
       
       

    popup = ft.AlertDialog(
       open=False,
       modal=True,
       title=ft.Text('Bem vindo'),
       content=nome_usuario,
       actions=[ft.ElevatedButton('Entrar', on_click=entrar_popup)],
    )

    def entrar_chat(evento):
     pagina.dialog = popup
     popup.open=True
     pagina.update()

     texto = ft.Text('Entrou no chat')
     pagina.add(texto)
        

    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=entrar_chat)

    pagina.add(botao_iniciar)
    
    
ft.app(target=main, view=ft.WEB_BROWSER)
