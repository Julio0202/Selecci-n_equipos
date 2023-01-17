import flet as ft
def main(page:ft.Page):
    page.title = "Imagenes"
    imag = ft.Image(src=f"BORUSIA_MONCHENGLASBACH.png")
    
    

    page.add(imag)




ft.app(target=main,assets_dir="Imagenes")