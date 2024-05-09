import flet as ft

#medidas universales
width = 1600
height= 850

class Home(ft.UserControl):
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
        #barra lateral
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
        
        #menú de contratos
        self.menu = ft.Container(
            #columna principal 
            ft.Column(
                [
                    ft.Text('Contratos', size=60, weight=ft.FontWeight.W_700, selectable=True, color=ft.colors.BLACK),
                    ft.Row(
                        [
                            ft.TextButton(text='Todos los contratos'),
                            ft.TextButton(text='Contratos de mantenimiento'),
                            ft.TextButton(text='Contratos de medición')
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing= 60
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Container(content= ft.Text('OMA-MINA', size=30, weight=ft.FontWeight.W_700,color=ft.colors.BLACK )),
                                ft.Container(ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_DOWN, icon_color='black'))
                            ],
                            alignment= ft.MainAxisAlignment.CENTER,
                            
                        ),
                        width=800,
                        height=100,
                        border_radius=10,
                        bgcolor= ft.colors.GREY_200,
                        margin= ft.margin.only(bottom=20)
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Container(content= ft.Text('CERRITOS', size=30, weight=ft.FontWeight.W_700,color=ft.colors.BLACK )),
                                ft.Container(ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_DOWN, icon_color='black'))
                            ],
                            alignment= ft.MainAxisAlignment.CENTER
                        ),
                        width=800,
                        height=100,
                        border_radius=10,
                        bgcolor= ft.colors.GREY_200,
                        margin= ft.margin.only(bottom=20)
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Container(content= ft.Text('VIRTUAL PIPELINES', size=30, weight=ft.FontWeight.W_700,color=ft.colors.BLACK )),
                                ft.Container(ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_DOWN, icon_color='black'))
                            ],
                            alignment= ft.MainAxisAlignment.CENTER
                        ),
                        width=800,
                        height=100,
                        border_radius=10,
                        bgcolor= ft.colors.GREY_200,
                        margin= ft.margin.only(bottom=20)
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Container(content= ft.Text('CEMPOALA', size=30, weight=ft.FontWeight.W_700,color=ft.colors.BLACK )),
                                ft.Container(ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_DOWN, icon_color='black'))
                            ],
                            alignment= ft.MainAxisAlignment.CENTER
                        ),
                        width=800,
                        height=100,
                        border_radius=10,
                        bgcolor= ft.colors.GREY_200,
                        margin= ft.margin.only(bottom=20)
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Container(content= ft.Text('OMA-EDO MEX', size=30, weight=ft.FontWeight.W_700,color=ft.colors.BLACK )),
                                ft.Container(ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_DOWN, icon_color='black'))
                            ],
                            alignment= ft.MainAxisAlignment.CENTER
                        ),
                        width=800,
                        height=100,
                        border_radius=10,
                        bgcolor= ft.colors.GREY_200,
                        margin= ft.margin.only(bottom=20)
                    )
                ]
            )
            
        )
        #ultima barra
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
                    self.menu,
                    self.side_bar],
                    alignment= ft.CrossAxisAlignment.CENTER,
                    spacing= 80
                )
            ],
            width=width,
            height=height,
        )
        return st
