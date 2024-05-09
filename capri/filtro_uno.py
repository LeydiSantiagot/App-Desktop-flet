import flet as ft 

#medidas universales
width = 1600
height= 850

class FiltroUno(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page
    
    def build(self):
        #contenedor principal
        self.body= ft.Container(
            width=width,
            height=height,
            bgcolor= 'white'
        )

        self.nav_bar= ft.Container(
            ft.Column(
                [
                    ft.IconButton(
                        icon= ft.icons.HOME,
                        icon_color= 'white',
                        icon_size= 60,
                        tooltip= 'Inicio'
                    ),
                    ft.IconButton(
                        icon= ft.icons.SETTINGS,
                        icon_color='white',
                        icon_size=60,
                        tooltip='Configuración'
                    ),
                    ft.IconButton(
                        icon= ft.icons.EXIT_TO_APP,
                        icon_color='white',
                        icon_size=60,
                        tooltip='Salir'
                    )
                ],
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                alignment= ft.MainAxisAlignment.CENTER
            ),
            width=200,
            height= 660,
            gradient= ft.LinearGradient([
                "#295C9A",
                "#0E1F34"
                ]),
            border_radius=10,
            margin= ft.margin.only(left=40),
            )
        

        self.seccion_uno = ft.Container(
            ft.Column(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Text('Seccion 1', size= 50, color= ft.colors.BLACK, weight= ft.FontWeight.W_800),
                                ft.Text('Ingresa los datos correspondientes y genera tus documentos fácilmente.', size= 20, weight= ft.FontWeight.W_700, color= ft.colors.BLACK, font_family='fonts/Poppins/Poppins-Black.ttf')
                            ]
                        ),
                        width= 800,
                        height=150,
                        border_radius= 10,
                        bgcolor= ft.colors.GREY_200,
                        margin= ft.margin.only(top= 100),
                        padding= ft.padding.all(20)
                        
                    ),
                    ft.TextField(
                        label = 'Ingresa el número de partida',
                        color= "black", 
                        border_color= "gray", 
                        width=800,
                        height=40, 
                        
                    ),
                    ft.TextField(
                        label = 'Ingresa el sitio',
                        color= "black", 
                        border_color= "gray", 
                        width=800,
                        height=40, 
                    ),
                    ft.TextField(
                        label = 'Ingresa la fecha',
                        color= "black", 
                        border_color= "gray", 
                        width=800,
                        height=40, 
                    ),
                    ft.Container(
                        ft.Checkbox(
                            label= "Generar folio automaticamente", 
                            active_color= "gray",
                            width= 500
                            ),
                        alignment= ft.alignment.center_left,
                        
                    ),
                    ft.Container(
                        ft.Checkbox(
                            label= "Generar TAG automaticamente", 
                            active_color= "gray",
                            width= 500
                            ),
                        alignment= ft.alignment.center_left,
                        #padding= ft.padding.only(left=10)
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                ft.CupertinoButton(
                                content= ft.Text('VOLVER', color= ft.colors.WHITE),
                                bgcolor= "#295C9A",
                                alignment= ft.alignment.top_left,
                                border_radius= ft.border_radius.all(15),
                                opacity_on_click= 0.5,
                                #on_click
                            ),
                            margin= ft.margin.only(left=90)
                            ),
                            ft.CupertinoButton(
                                content= ft.Text('SIGUIENTE', color= ft.colors.WHITE),
                                bgcolor= "#3C9B36",
                                alignment= ft.alignment.top_left,
                                border_radius= ft.border_radius.all(15),
                                opacity_on_click= 0.5
                                #on_click
                            ),
                            
                        ],
                        spacing= 200,
                        alignment= ft.MainAxisAlignment.END,
                        
                    )
                ],
                spacing= 30
            )
        )

        self.side_bar = ft.Container(
            ft.Container(ft.Image(src="assets/logoicsi.png", width=150, height=150), alignment=ft.alignment.top_right, margin=0),
            width=200,
            height=660,
            margin= ft.margin.only(top=10)
        )

        st = ft.Stack(
            [
                self.body,
                ft.Row(
                    [self.nav_bar, 
                    self.seccion_uno,
                    self.side_bar],
                    alignment= ft.CrossAxisAlignment.CENTER,
                    spacing= 80
                )
            ],
            width=width,
            height=height,
        )
        return st