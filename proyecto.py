

import flet as ft

def main(page: ft.Page):
    page.title = "DropdownMenu Equipos"
    imag = ""
    def dropdown_changed(e):
        page.update()
        if (equipos.value == "Rayo Fuentealbilla"):
            imag = "RAYO_FUENTEALBILLA.jpg"
        elif (equipos.value == "Depor"):
            imag = "DEPOR.jpg"
        elif (equipos.value == "Leganés"):
            imag = "LEGANES.jpg"
        elif(equipos.value=="Real Zaragoza"):
            imag = "REAL_ZARAGOZA.jpg"
        else:
            (equipos.value=="Borusia")
            imag = "BORUSIA_MONCHENGLASBACH.png"

        img.src=f"{imag}"
        page.update()
    
    def equipolista(e):
        seleccionado=""
        
        if(vEquiposSelecionados.count(equipo)==0):
            vEquiposSelecionados.append(equipo)
            print(vEquiposSelecionados)
        
        else:
            dlg = ft.AlertDialog(title=ft.Text("Equipo Repetido"))
            page.dialog = dlg
            dlg.open = True
            page.update()
        

        
   

   


    
    equipos = ft.Dropdown(hint_text="Selecciona un equipo",width=250, on_change=dropdown_changed)
   


    img = ft.Image(
            src=f"Imagenes/{imag}",
            width=300,
            height=300
        )

    vEquipos = ["Rayo Fuentealbilla", "Depor", "Leganés", "Real Zaragoza", "Borusia Monchenglasbach"]
    vEquiposSelecionados = []
    
    


    for equipo in vEquipos:
        equipos.options.append(ft.dropdown.Option(equipo))
    
    boton=ft.ElevatedButton(text="Añadir equipo",on_click=equipolista)
    
    
    page.add(equipos,img)
    page.add(boton)
ft.app(target=main,assets_dir="Imagenes")