import flet as ft

def main(page: ft.Page):
    page.title = "DropdownMenu Equipos"
    imag = ""
    def dropdown_changed(e):
        imag.value = f"Dropdown changed to {dd.value}"
        page.update()
        if (dd.value == "Rayo Fuentealbilla"):
            imag = "RAYO_FUENTEALBILLA.jpg"
        elif (dd.value == "Depor"):
            imag = "DEPOR.jpg"
        elif (dd.value == "Leganés"):
            imag = "LEGANES.jpg"
    dd = ft.Dropdown(
        options=[
            ft.dropdown.Option("Rayo Fuentealbilla"),
            ft.dropdown.Option("Depor"),
            ft.dropdown.Option("Leganés"),
            ft.dropdown.Option("Real Zaragoza"),
            ft.dropdown.Option("Borusia Mochenglasbach"),
            
        ],
        width=200,
        on_change=dropdown_changed
    )
    page.add(dd, imag)




ft.app(target=main,assets_dir="Imagenes")