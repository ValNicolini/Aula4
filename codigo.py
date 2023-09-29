import flet as ft

def main(pagina):
    texto = ft.Text('TESTE')
    popup = ft.AlertDialog()
    
    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    botao_iniciar = ft.ElevatedButton('Iniciar chat', on_click=entrar_chat)
        
    pagina.add(texto)
    pagina.add(botao_iniciar)
    
ft.app(target=main, view=ft.WEB_BROWSER)
