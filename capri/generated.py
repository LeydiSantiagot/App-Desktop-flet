import flet as ft 

#medidas universales 
width = 1600
height= 850

class Generado(ft.UserControl):
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
        
        self.done= ft.Container(
            ft.Column(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Text('Sección 4', size= 50, color= ft.colors.BLACK, weight= ft.FontWeight.W_800),
                                ft.Text('Los reportes han sido generados, haz click en el icono para descargar automaticamente.', size= 15, weight= ft.FontWeight.W_700, color= ft.colors.GREY_500, font_family='fonts/Poppins/Poppins-Black.ttf')
                            ]
                        ),
                        width= 800,
                        height=150,
                        border_radius= 10,
                        bgcolor= ft.colors.GREY_200,
                        margin= ft.margin.only(top= 100),
                        padding= ft.padding.all(20)
                        
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                ft.FloatingActionButton(
                                    icon= ft.icons.DOWNLOAD,
                                    bgcolor= ft.colors.GREY_300,
                                    tooltip='Reporte de Mtto'
                                )
                            ),
                            ft.Container(
                                ft.Text("Reporte de Mantenimiento", weight= ft.FontWeight.W_600, color= ft.colors.BLACK, size=20),
                            )
                        ]
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                ft.FloatingActionButton(
                                    icon= ft.icons.DOWNLOAD,
                                    bgcolor= ft.colors.GREY_300,
                                    tooltip='Carta de Mtto'
                                )
                            ),
                            ft.Container(
                                ft.Text("Carta de Mantenimiento", weight= ft.FontWeight.W_600, color= ft.colors.BLACK, size=20),
                            )
                        ]
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                ft.FloatingActionButton(
                                    icon= ft.icons.DOWNLOAD,
                                    bgcolor= ft.colors.GREY_300,
                                    tooltip='Historico de Mtto'
                                )
                            ),
                            ft.Container(
                                ft.Text("Historico de Mantenimiento", weight= ft.FontWeight.W_600, color= ft.colors.BLACK, size=20),
                            )
                        ]
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                ft.FloatingActionButton(
                                    icon= ft.icons.DOWNLOAD,
                                    bgcolor= ft.colors.GREY_300,
                                    tooltip='Reporte Fotografico'
                                )
                            ),
                            ft.Container(
                                ft.Text("Reporte Fotografico", weight= ft.FontWeight.W_600, color= ft.colors.BLACK, size=20),
                            )
                        ]
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                ft.FloatingActionButton(
                                    icon= ft.icons.DOWNLOAD,
                                    bgcolor= ft.colors.GREY_300,
                                    tooltip='Generador de Obra'
                                )
                            ),
                            ft.Container(
                                ft.Text("Generador de Obra", weight= ft.FontWeight.W_600, color= ft.colors.BLACK, size=20),
                            )
                        ]
                    )
                ],
                spacing=30
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
                    self.done,
                    self.side_bar],
                    alignment= ft.CrossAxisAlignment.CENTER,
                    spacing= 80
                )
            ],
            width=width,
            height=height,
        )
        return st