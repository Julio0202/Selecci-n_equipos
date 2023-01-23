import flet as ft

def main(page: ft.Page):
    page.title = "DropdownMenu Equipos"
    imag = ""
    def dropdown_changed(e):
        page.update()
        if (dd.value == "Rayo Fuentealbilla"):
            imag = "RAYO_FUENTEALBILLA.jpg"
        elif (dd.value == "Depor"):
            imag = "DEPOR.jpg"
        elif (dd.value == "Leganés"):
            imag = "LEGANES.jpg"
        elif(dd.value=="Real Zaragoza"):
            imag = "REAL_ZARAGOZA.jpg"
        else:
            (dd.value=="Borusia")
            imag = "BORUSIA_MONCHENGLASBACH.png"


        
        
        img.src=f"{imag}"
    
        page.update()
    
    
    dd = ft.Dropdown(label="Equipos",
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
    page.add(dd)

    img = ft.Image(
            src=f"Imagenes/{imag}",
            width=300,
            height=300
        )

    boton=ft.ElevatedButton(text="Añadir equipo")
    page.add(boton)

    page.add(img)



ft.app(target=main,assets_dir="Imagenes")