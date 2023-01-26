

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
    
    def equipolista(e):
        seleccionado=""
        if(vEquiposSelecionados.count(menu.value)==0):
            vEquiposSelecionados.append(menu.value)
            print(vEquiposSelecionados)
            list_view.controls.append(ft.Text(vEquiposSelecionados.pop))
        
        else:
            dlg = ft.AlertDialog(title=ft.Text("Equipo ya seleccionado"))
            page.dialog = dlg
            dlg.open = True
    page.update()

        
   

   


    
    menu = ft.Dropdown(hint_text="Selecciona un equipo",width=250, on_change=dropdown_changed)
   


    img = ft.Image(
            src=f"Imagenes/{imag}",
            width=300,
            height=300
        )

    vEquipos = ["Rayo Fuentealbilla", "Depor", "Leganés", "Real Zaragoza", "Borusia Monchenglasbach"]
    vEquiposSelecionados = []
    
    


    for equipo in vEquipos:
        menu.options.append(ft.dropdown.Option(equipo))
    
    boton=ft.ElevatedButton(text="Añadir equipo",on_click=equipolista)
    list_view = ft.ListView(expand=1,spacing=10,padding=20, auto_scroll=True)
    page.update()
    

    page.add(menu,img)
    page.add(boton)
    page.add(list_view)
ft.app(target=main,assets_dir="Imagenes")