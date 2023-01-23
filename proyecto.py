import flet as ft

def main(page: ft.Page):
    page.title = "DropdownMenu Equipos"
    imag = ""
    def dropdown_changed(e):
        page.update()
        if (menu.value == "Rayo Fuentealbilla"):
            imag = "RAYO_FUENTEALBILLA.jpg"
        elif (menu.value == "Depor"):
            imag = "DEPOR.jpg"
        elif (menu.value == "Leganés"):
            imag = "LEGANES.jpg"
        elif(menu.value=="Real Zaragoza"):
            imag = "REAL_ZARAGOZA.jpg"
        else:
            (menu.value=="Borusia")
            imag = "BORUSIA_MONCHENGLASBACH.png"

        img.src=f"{imag}"
        page.update()
    

    
    menu = ft.Dropdown(hint_text="Selecciona un equipo",width=250, on_change=dropdown_changed)
   


    img = ft.Image(
            src=f"Imagenes/{imag}",
            width=300,
            height=300
        )

    img.src="aa"
    
    vEquipos = ["ivbaseui"]
    vEquiposSelecionados = []

    for equipo in vEquipos:
        menu.options.append(ft.dropdown.Option(equipo))
    

    page.add(menu,img)
 

 


ft.app(target=main,assets_dir="Imagenes")