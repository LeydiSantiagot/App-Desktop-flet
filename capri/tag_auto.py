import flet as ft

#medidas universales
width = 1600
height= 850

class TagAutomatico(ft.UserControl):
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
        
        self.Tag_automatico = ft.Container(
            ft.Column(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Text('Tag Automatico', size= 50, color= ft.colors.BLACK, weight= ft.FontWeight.W_800),
                                ft.Text('Añade el número de TAG incial y el final.', size= 20, weight= ft.FontWeight.W_700, color= ft.colors.BLACK, font_family='fonts/Poppins/Poppins-Black.ttf')
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
                        label = 'Número inicial',
                        color= "black", 
                        border_color= "gray", 
                        width=800,
                        height=40, 
                        
                    ),
                    ft.TextField(
                        label = 'Número final',
                        color= "black", 
                        border_color= "gray", 
                        width=800,
                        height=40, 
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                ft.CupertinoButton(
                                content= ft.Text('GENERAR', color= ft.colors.WHITE),
                                bgcolor= "#3C9B36",
                                alignment= ft.alignment.top_left,
                                border_radius= ft.border_radius.all(15),
                                opacity_on_click= 0.5,
                                #on_click
                            ),
                            margin= ft.margin.only(left=90)
                            ),
                            ft.CupertinoButton(
                                content= ft.Text('BORRAR', color= ft.colors.WHITE),
                                bgcolor= "#CE3C3C",
                                alignment= ft.alignment.top_left,
                                border_radius= ft.border_radius.all(15),
                                opacity_on_click= 0.5
                                #on_click
                            ),
                            
                        ],
                        spacing= 200,
                        alignment= ft.MainAxisAlignment.END,
                        
                    ),
                    ft.Text("TAG'S generados", weight= ft.FontWeight.W_700, color= ft.colors.GREY_400, size=20),
                    ft.Container(
                        width=800,
                        height=100,
                        border= ft.border.all(3, ft.colors.GREY_300),
                        border_radius= 8
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
                        
                    ),
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
                    self.Tag_automatico,
                    self.side_bar],
                    alignment= ft.CrossAxisAlignment.CENTER,
                    spacing= 80
                )
            ],
            width=width,
            height=height,
        )
        return st