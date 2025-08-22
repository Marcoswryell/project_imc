import flet as ft
import os
from banco import data
from inserir_func import salvar_anotacao, listar_anotacoes, listar_tudo

def main(page: ft.Page):
    page.title = "IMC CALCULATOR"
    page.theme_mode = ft.ThemeMode.LIGHT
    data()

    # --------- VIEW 1: Tela Home ----------
    def view_home(page: ft.Page) -> ft.View:
        resultado = ft.Text("", size=20, weight=ft.FontWeight.W_500)

        def calcular_imc(e):
            try:
                nome = nome_input.value
                peso = float(peso_input.value.replace(",", "."))
                altura = float(altura_input.value.replace(",", "."))
                if altura <= 0:
                    raise ValueError
                imc = peso / (altura * altura)
                if imc < 18.5:
                    classificacao = "Abaixo do peso"
                elif imc < 25:
                    classificacao = "Peso normal"
                elif imc < 30:
                    classificacao = "Sobrepeso"
                else:
                    classificacao = "Obesidade"
                resultado.value = f"Olá {nome}, seu IMC é {imc:.2f} — {classificacao}"
                resultado.color = ft.colors.BLUE_900
            except:
                resultado.value = "Verifique os valores de peso e altura."
                resultado.color = ft.colors.RED_700
            page.update()

        nome_input = ft.TextField(label="Nome", width=300)
        peso_input = ft.TextField(label="Peso (kg)", width=300, keyboard_type=ft.KeyboardType.NUMBER)
        altura_input = ft.TextField(label="Altura (m)", width=300, keyboard_type=ft.KeyboardType.NUMBER)

        return ft.View(
            bgcolor=ft.colors.WHITE,
            route="/",
            appbar=ft.AppBar(
                bgcolor=ft.colors.with_opacity(0.3, ft.colors.WHITE),
                leading=ft.IconButton(
                    ft.icons.LIST_ALT,
                    icon_color=ft.colors.with_opacity(0.5, ft.colors.GREEN_900),
                    on_click=lambda e: page.go("/nova_tela")
                ),
                actions=[ft.Image(src="imagens/bmi.png", width=50)]
            ),
            navigation_bar=ft.NavigationBar(
                bgcolor=ft.colors.with_opacity(0.3, ft.colors.GREEN_900),
                destinations=[
                    ft.NavigationBarDestination(icon=ft.icons.CALCULATE_ROUNDED, label="Home"),
                    ft.NavigationBarDestination(icon=ft.icons.PERSON, label="Sobre"),
                ],
                on_change=lambda e: page.go("/sobre" if e.control.selected_index == 1 else "/"),
            ),
            controls=[
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Image(src="imagens/texty.png", width=500),
                            nome_input,
                            peso_input,
                            altura_input,
                            ft.ElevatedButton(
                                "Calcular IMC",
                                bgcolor=ft.colors.WHITE,
                                opacity=0.6,
                                icon_color=ft.colors.BLUE_GREY_900,
                                color=ft.colors.BLUE_GREY_900,
                                icon=ft.icons.CALCULATE_SHARP,
                                on_click=calcular_imc
                            ),
                            resultado
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=15
                    ),
                    alignment=ft.alignment.center,
                    expand=True
                )
            ]
        )

    # --------- VIEW 2: Tela Sobre ----------
    def view_sobre(page: ft.Page) -> ft.View:
        return ft.View(
            bgcolor=ft.colors.GREEN_ACCENT_100,
            route="/sobre",
            navigation_bar=ft.NavigationBar(
                destinations=[
                    ft.NavigationBarDestination(icon=ft.icons.CALCULATE_ROUNDED,  label="Home"),
                    ft.NavigationBarDestination(icon=ft.icons.PERSON, label="Sobre"),
                ],
                on_change=lambda e: page.go("/" if e.control.selected_index == 0 else "/sobre")
            ),
            controls=[
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Image(src="imagens/bmi.png", width=200),
                            ft.Text(
                                '''Benefícios de calcular o IMC diariamente: 
Calcular o IMC todos os dias ajuda a acompanhar 
seu peso e saúde, identificar mudanças no corpo e 
ajustar hábitos de alimentação e exercícios. 
Manter o IMC dentro da faixa saudável contribui para reduzir 
riscos de doenças e promover um estilo de vida equilibrado.

MARCOS URIEL DEV - SOFTWARES LTDA®''',
                                size=14,
                                text_align=ft.TextAlign.CENTER,
                                width=600
                            ),
                            ft.Image(src="imagens/texty.png", width=350),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=15
                    ),
                    alignment=ft.alignment.center,
                    expand=True,
                )
            ]
        )

    # --------- VIEW 3: Tela Anotações ----------
    def view_nova(page: ft.Page) -> ft.View:
        entrada = ft.TextField(label='Sua anotação aqui:', width=500, height=100, multiline=True)
        lista = ft.Column(spacing=5)

        def carregar_anotacoes():
            lista.controls.clear()
            for id, texto in listar_anotacoes():
                lista.controls.append(ft.Text(f"{id}: {texto}", size=16))
            page.update()

        def salvar_click(e):
            if entrada.value.strip() != "":
                salvar_anotacao(entrada.value.strip())
                entrada.value = ""
                carregar_anotacoes()

        carregar_anotacoes()

        return ft.View(
            route="/nova_tela",
            appbar=ft.AppBar(
                leading=ft.Row([
                    ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda e: page.go("/")),
                    ft.Image(src="imagens/texty.png")
                ]),
            ),
            navigation_bar=ft.NavigationBar(
                destinations=[ft.NavigationBarDestination(icon=ft.icons.LIST, label='Listar Todas')],
                on_change=lambda e: page.go("/listar" if e.control.selected_index == 0 else "/")
            ),
            controls=[
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text('Anotações', size=24, weight=ft.FontWeight.BOLD),
                            entrada,
                            ft.ElevatedButton('Salvar', on_click=salvar_click, color='white', bgcolor='red'),
                            lista
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=15
                    ),
                    alignment=ft.alignment.center,
                    expand=True
                )
            ]
        )

    # --------- VIEW 4: Tela Listar ----------
    def view_listar(page: ft.Page) -> ft.View:
        lista = ft.Column(spacing=5)
        for id, texto in listar_tudo():
            lista.controls.append(ft.Text(f"{id}: {texto}", size=16))

        return ft.View(
            route="/listar",
            appbar=ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda e: page.go("/nova_tela")),
                title=ft.Text("Todas as Anotações"),
            ),
            controls=[
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Listagem Completa", size=24, weight=ft.FontWeight.BOLD),
                            lista
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10
                    ),
                    alignment=ft.alignment.top_center,
                    expand=True
                )
            ]
        )

    # --------- Funções de rota ----------
    def route_change(e):
        page.views.clear()
        routes = {
            "/": view_home,
            "/sobre": view_sobre,
            "/nova_tela": view_nova,
            "/listar": view_listar
        }
        page.views.append(routes.get(page.route, view_home)(page))
        page.update()

    def view_pop(e):
        page.views.pop()
        page.go(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route or "/")

# Porta dinâmica para Railway
PORT = int(os.environ.get("PORT", 8080))
ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=PORT)