import flet as ft

def main(page: ft.Page):
    page.title = "Exemplo de Navegação - IMC"
    page.theme_mode = ft.ThemeMode.LIGHT

    # --------- VIEW 1: Tela inicial ----------
    def view_home(page: ft.Page) -> ft.View:
        # Labels e resultados
        resultado = ft.Text("", size=20, weight=ft.FontWeight.W_500)

        def calcular_imc(e):
            try:
                peso = float(peso_input.value.replace(",", "."))
                altura = float(altura_input.value.replace(",", "."))
                if altura <= 0:
                    raise ValueError
                imc = peso / (altura * altura)
                # Classificação
                if imc < 18.5:
                    classificacao = "Abaixo do peso"
                elif imc < 25:
                    classificacao = "Peso normal"
                elif imc < 30:
                    classificacao = "Sobrepeso"
                else:
                    classificacao = "Obesidade"
                resultado.value = f"IMC: {imc:.2f} — {classificacao}"
                resultado.color = ft.colors.BLUE_900
            except:
                resultado.value = "Verifique os valores de peso e altura."
                resultado.color = ft.colors.RED_700
            page.update()

        # Inputs
        peso_input = ft.TextField(label="Peso (kg)", width=200, keyboard_type=ft.KeyboardType.NUMBER)
        altura_input = ft.TextField(label="Altura (m)", width=200, keyboard_type=ft.KeyboardType.NUMBER)

        return ft.View(
            route="/",
            appbar=ft.AppBar(
                leading=ft.IconButton(ft.icons.MENU), 
                title=ft.Text("Calculadora de IMC"),
                center_title=True,
            ),
            navigation_bar=ft.NavigationBar(
                destinations=[
                    ft.NavigationBarDestination(icon=ft.icons.CALCULATE_ROUNDED, label="Home"),
                    ft.NavigationBarDestination(icon=ft.icons.PERSON, label="Sobre"),
                ],
                on_change=lambda e: page.go("/sobre" if e.control.selected_index == 1 else "/"),
            ),
            controls=[
                ft.Column(
                    [
                        ft.Image(src="Users/marcoswryell/desktop/projetinho/imagens/texty.png", width=200),
                        peso_input,
                        altura_input,
                        ft.ElevatedButton("Calcular IMC", on_click=calcular_imc),
                        resultado
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=12,
                    expand=True
                ),
            ]
        )

    # --------- VIEW 2: Tela "sobre" ----------
    def view_sobre(page: ft.Page) -> ft.View:
        return ft.View(
            route="/sobre",
            navigation_bar=ft.NavigationBar(
                destinations=[
                    ft.NavigationBarDestination(icon=ft.icons.CALCULATE_ROUNDED, label="Home"),
                    ft.NavigationBarDestination(icon=ft.icons.PERSON, label="Sobre"),
                ], 
                on_change=lambda e: page.go("/" if e.control.selected_index == 0 else "/sobre")
            ),
            controls=[
                ft.Column(
                    [
                        ft.Text("ℹ️ Tela SOBRE", size=30, weight="bold"),
                        ft.Text("Esta tela pode conter informações adicionais sobre o IMC."),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True
                )
            ]
        )

    # --------- Função de mudança de rota ----------
    def route_change(e):
        page.views.clear()  # limpa as telas abertas
        if page.route == "/":
            page.views.append(view_home(page))
        elif page.route == "/sobre":
            page.views.append(view_sobre(page))
        page.update()

    # --------- Função de voltar ----------
    def view_pop(e):
        page.views.pop()
        page.go(page.views[-1].route)

    # Conecta os eventos de rota
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Começa pela rota inicial
    page.go(page.route or "/")

ft.app(target=main)