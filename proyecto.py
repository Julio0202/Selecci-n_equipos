

import flet as ft

def main(page: ft.Page):
    lv = ft.ListView(expand=1,spacing=5, padding=20, auto_scroll=True)
    page.title = "DropdownMenu Equipos"
    imag = ""
    def dropdown_changed(e):
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
            lv.controls.append(vEquiposSelecionados)
        else:
            dlg = ft.AlertDialog(title=ft.Text("Equipo ya seleccionado"))
            page.dialog = dlg
            dlg.open = True
            page.update()

        

    def cargarequipos():
        vEquipos=[]
        f=open("Equipos.txt","r")
        linea = f.readline()
        vEquipos = linea.split(sep=";")
        f.close()
        return vEquipos



    menu = ft.Dropdown(hint_text="Selecciona un equipo",width=250, on_change=dropdown_changed)
   


    img = ft.Image(
            src=f"Imagenes/{imag}",
            width=300,
            height=300
        )

    vEquiposSelecionados = []
    vEquipos = cargarequipos()
    for equipo in vEquipos:
        menu.options.append(ft.dropdown.Option(equipo))
    
    boton=ft.ElevatedButton(text="Añadir equipo",on_click=equipolista)
    

    page.add(menu,img,lv)
    page.add(boton)
ft.app(target=main,assets_dir="Imagenes")