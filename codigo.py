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
    texto = ft.Text('Bate-Papo')
    
    chat = ft.Column()

    nome_usuario = ft.TextField(label='Escreva seu nome')

    def enviar_mensagem_tunel(mensagem):
       tipo = mensagem['tipo']
       
       if tipo == 'mensagem':
            texto_mensagem = mensagem['texto']
            usuario_mensagem = mensagem['usuario']
            #adicionar a mensagem no chat
            chat.controls.append(ft.Text(f'{usuario_mensagem}: {texto_mensagem}'))
       else:
            usuario_mensagem = mensagem['usuario']
            #adicionar a mensagem no chat
            chat.controls.append(ft.Text(f'{usuario_mensagem} entrou no chat',
                                         size=12,
                                         italic=True,
                                         color=ft.colors.CYAN_300))
       pagina.update()
       
       #túnel de mensagem
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
      
    def enviar_mensagem(evento):
       pagina.pubsub.send_all({'texto':campo_mensagem.value, 'usuario':nome_usuario.value, 'tipo':'mensagem'})
       #limpar o campo de mensagem
       campo_mensagem.value=''
       pagina.update()
    
    campo_mensagem = ft.TextField(label='Digite sua mensagem')

    botao_enviar_mensagem = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    
    def entrar_popup(evento):
       pagina.pubsub.send_all({'usuario':nome_usuario.value, 'tipo':'entrada'})
       #adicionar o chat
       pagina.add(chat)
       #fechar popup
       popup.open=False
       #remover botão iniciar chat
       pagina.remove(botao_iniciar)
       pagina.remove(texto)
       #adicionar campo de mensagem do usuário
       #adicionar botão de enviar mensagem
       pagina.add(ft.Row([campo_mensagem, botao_enviar_mensagem])),
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
        

    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=entrar_chat)
    
    pagina.add(texto)
    pagina.add(botao_iniciar)
    
    
ft.app(target=main, view=ft.WEB_BROWSER)#,port=8000
#deploy