import flet as ft
from flet import Stack, Container
from flet import *
from flet import View, Page
from register import Register

#medidas universales
width = 1600
height= 850

class Login(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        self.title = "Login"
        self.window_max_width= width
        self.window_max_height= height
        self.window_width = width
        self.window_height = height
        self.window_resizable = False
        self.padding=0

        #contenedor principal
        self.body= ft.Container(
            width=width,
            height=height,
            gradient= ft.LinearGradient([
            "#295C9A",
            "#0E1F34"
            ])
        )

        #contenedor de info
        self.other_hand = ft.Container(
            ft.Column([
                ft.Container(
                ft.Image(
                    src= "assets/logoicsi.png",
                    width=150,
                    height=80, 
                ),
            alignment= ft.alignment.center,
        ), 

        ft.Container(
            ft.Text(
                "ICSI OIL & GAS",
                width=300,
                size=40,
                text_align="center",
                weight="w900"
            ), 
            alignment= ft.alignment.center
        ),

        ft.Container(
            ft.Text(
                "Empresa Líder en la Industria del Gas",
                width=400,
                size=20,
                text_align= "center",
            ),
            alignment= ft.alignment.center,
        ),

        ft.Container(
            ft.Text(
                "Genera tus reportes de manera automatizada.",
                width=300,
                size=20,
                text_align= "right"
            ),
            padding= ft.padding.only(top= 270, left=250)
        )
        ],
        alignment= ft.MainAxisAlignment.CENTER,
        ),
        width= 600,
        height= 700,
        bgcolor= ft.colors.WHITE,
        margin= ft.margin.only(left=150, top=50),
        border_radius= ft.border_radius.all(10),
        padding=0,
        alignment= ft.alignment.center,
    )

        #contenedor de login
        self.login = ft.Container(
            ft.Column([
                ft.Container(
                    ft.Text(
                        'Iniciar Sesión',
                        width=300,
                        size=40, 
                        weight= "w600",
                        text_align='left',
                        color= 'black'
            ),
            padding= ft.padding.only( left=80),
            alignment= ft.alignment.center_left
        ),
                ft.Container(
                    ft.TextField(
                        width=400,
                        height=40,
                        #border= "underline",
                        label= "Correo electronico", 
                        color= "black", 
                        prefix_icon= ft.icons.EMAIL,
                        border_color='#295C9A'
                    ),
            padding= ft.padding.only(top= 20, left= 80),
            alignment= ft.alignment.center_left
        ),
                ft.Container(
                    ft.TextField(
                        #border= "underline",
                        label = 'Contraseña',
                        color= "black", 
                        border_color= "#295C9A", 
                        prefix_icon= ft.icons.LOCK,
                        width=400,
                        height=40, 
                        password=True
            ),
            padding= ft.padding.only(top= 20, left=80),
            alignment= ft.alignment.center_left
        ),
                ft.Container(
                    ft.Checkbox(
                        label= "Recordar contraseña", 
                        check_color= "blue",
                        width= 300,
            ),
            alignment= ft.alignment.center_left,
            padding= ft.padding.only(left=80)
        ), 
                ft.Container(
                    ft.ElevatedButton(
                        text= "INICIAR SESIÓN", 
                        bgcolor= "#295C9A",
                        color= 'white'
            ),
            padding= ft.padding.only(top= 50),
            alignment= ft.alignment.center
        ),
                ft.Container(
                    ft.Row(
                        [
                            ft.Text(
                                'No tienes una cuenta?',
                                text_align= 'center',
                                color='black'
                ),
                ft.TextButton(
                    'Registrate',
                    #on_click=
                )
                ],
            alignment= ft.MainAxisAlignment.CENTER
            )
        )
    ],
    alignment= ft.MainAxisAlignment.CENTER,
    ),
    width=600,
    height=700,
    bgcolor= ft.colors.WHITE,
    margin= ft.margin.only(right=150, top=50),
    padding=0,
    border_radius= ft.border_radius.all(10),
    alignment= ft.alignment.center
)
     #añadiendo widgets a la pagina principal
        #stack para superponer elementos
        st = ft.Stack(
            [
                self.body, 
                ft.Row(
                    [self.other_hand, 
                    self.login]
                )
            ],
            width=width,
            height=height,
        )
        return st

