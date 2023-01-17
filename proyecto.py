import flet as ft

def main(page: ft.Page):
    page.title = "DropdownMenu Equipos"

    Dropdown_Equipos=ft.Dropdown(width=300,options=[ft.dropdown.Option("Rayo Fuentealbilla")],label="Equipos")
    Dropdown_Equipos.options.append(ft.dropdown.Option("Depor"))
    Dropdown_Equipos.options.append(ft.dropdown.Option("Leganés"))
    Dropdown_Equipos.options.append(ft.dropdown.Option("Real Zaragoza"))
    Dropdown_Equipos.options.append(ft.dropdown.Option("Borusia Mochenglasbach"))
    page.add (Dropdown_Equipos)


ft.app(target=main)