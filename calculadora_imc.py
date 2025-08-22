import sqlite3 as sql
from banco import data
import flet as ft
from inserir_func import coletar
from banco import data


def main(page: ft.Page):
  data()
  page.title = 'IMC COLECTOR'
  page.theme_mode = ft.ThemeMode.DARK
  page.padding = 170
  
  page.appbar = ft.CupertinoAppBar(
    leading=ft.Image(src='/Users/marcoswryell/desktop/projetinho/imagens/bmi.png'),
    bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
    trailing=ft.IconButton(ft.icons.BOOKMARK_ADD),
    brightness=ft.Brightness.LIGHT
  )

  def on_login_click(e):
    nome, peso, altura = nome_input.value, peso_input.value, altura_input.value
    if nome and peso and altura:
      coletar(nome, peso, altura)
      msg.value = f'Dados do usuário {nome} coletados com sucesso.'
    else:
      msg.value = 'Preencha todos o campos!'
    page.update()

  image_text = ft.Image(src='Users/marcoswryell/desktop/projetinho/imagens/texty.png')
  nome_input = ft.TextField(label='nome', color="#CF6408")
  peso_input = ft.TextField(label='peso', color="#CF6408")
  altura_input = ft.TextField(label='altura', color="#CF6408")
  botao = ft.ElevatedButton('REGISTRAR', bgcolor='#7AA4BF', elevation=7, color='white', on_click=on_login_click, offset=ft.Offset(0, 0.5))
  msg = ft.Text('', color=ft.colors.GREEN_900, offset=ft.Offset(0, 0.8))


  
  
  
 

  page.add(
    ft.Stack(
      [
        ft.Image(
          src='/Users/marcoswryell/desktop/projetinho/imagens/bmi.png', 
          width=600, 
          height=300,
          opacity=0.5,
          offset=ft.Offset(0, 1.01)
        ),
        ft.Column(
          [
            image_text,
            nome_input, 
            peso_input, 
            altura_input,
            botao,
            msg
          ],alignment=ft.MainAxisAlignment.CENTER,       
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
      ], alignment=ft.Alignment(1, -0.3)
    )
  )

  page.navigation_bar = ft.NavigationBar(
     bgcolor='grey', 
     opacity=0.4, 
     destinations=[
       ft.NavigationBarDestination(icon=ft.icons.DATA_EXPLORATION, label='COLETA'),
       ft.NavigationBarDestination(icon=ft.icons.CALCULATE_SHARP, label='CALCULAR IMC')
       
       
     ], indicator_color=ft.colors.WHITE
  )

  
  page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550, host="0.0.0.0")


