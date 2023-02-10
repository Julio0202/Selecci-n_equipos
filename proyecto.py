import flet as ft

def main(page: ft.Page):
    lv = ft.ListView(expand=1,spacing=5, padding=20, auto_scroll=True)
    page.title = "DropdownMenu Equipos"
    imag = ""
    img = ft.Image(
            src=f"Imagenes/{imag}",
            width=300,
            height=300
        )
    def dropdown_changed(e):
        if (menu.value == "Rayo Fuentealbilla"):
            imag = "RAYO_FUENTEALBILLA.jpg"
        elif (menu.value == "Depor"):
            imag = "DEPOR.jpg"
        elif (menu.value == "Leganes"):
            imag = "LEGANES.jpg"
        elif(menu.value=="Real Zaragoza"):
            imag = "REAL_ZARAGOZA.jpg"
        elif(menu.value=="Borusia Monchenglasbach"):
            imag = "BORUSIA_MONCHENGLASBACH.png"
        else:
            imag="imagen_no_disponible.jpg"
        img.src=f"{imag}"
        page.update()
    
    def equipolista(e):
        seleccionado=""
        ss=menu.value
        if(vEquiposSelecionados.count(menu.value)==0):
            vEquiposSelecionados.append(menu.value)
            print(vEquiposSelecionados)
            row = ft.Row(spacing=30,controls=[ft.Text(ss), ft.Image(width=50,height=50,src=img.src)])
            lv.controls.append(row)
        else:
            dlg = ft.AlertDialog(title=ft.Text("Equipo ya seleccionado"))
            page.dialog = dlg
            dlg.open = True
            img.src="imagen_no_disponible.jpg"

        page.update()
    


    
        

    def cargarequipos():
        vEquipos=[]
        f=open("Equipos.txt","r")
        linea = f.readline()
        vEquipos = linea.split(sep=";")
        f.close()
        return vEquipos


    def añadir_equipo(e):
        g = open("EquiposSeleccionados.txt","w")
        for i in vEquiposSelecionados:
            g.write(i+";")
        g.close()
    
    menu = ft.Dropdown(hint_text="Selecciona un equipo",width=250, on_change=dropdown_changed)

   


    

    vEquiposSelecionados = []
    vEquipos = cargarequipos()
    for equipo in vEquipos:
        menu.options.append(ft.dropdown.Option(equipo))
    
    
    boton=ft.ElevatedButton(text="Añadir equipo",on_click=equipolista)
    botonañadir = ft.FloatingActionButton(text="Añadir lista", on_click=añadir_equipo)

    page.add(menu,img,lv,boton,botonañadir)
    
ft.app(target=main,assets_dir="Imagenes")