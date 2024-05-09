from flet import *
from views import views_handler
from login import Login
from register import Register
from home import Home
from filtro_uno import FiltroUno
from folio_auto import FolioAutomatico
from folio_manual import FolioManual
from tag_auto import TagAutomatico
from tag_manual import TagManual
from add import Add
from generated import Generado

def main (page: Page):
    page.title = 'App'

    def route_change(e: RouteChangeEvent):
        
        page.views.clear()
        #page por defecto
        page.views.append(
            View(
                route='/login',
                controls=[
                    Login (page)
                ]
            )
        )

        if page.route == '/register':
             page.views.append(
                View(
                    route='/register',
                    controls=[
                        Register(page)
                ]
            )
        )
             
        if page.route == '/home':
            page.views.append(
                View(
                    route= '/home',
                    controls= [
                        Home(page)
                    ]
                )
            )
        if page.route == "/filtro_uno":
            page.views.append(
                View(
                    route='/filtro_uno',
                    controls=[
                        FiltroUno(page)
                    ]
                )
            )
        
        if page.route == "/folio_auto":
            page.views.append(
                View(
                    route= '/folio_auto',
                    controls=[
                        FolioAutomatico(page)
                    ]
                )
            )
        
        if page.route == "/folio_manual":
            page.views.append(
                View(
                    route= '/folio_manual',
                    controls=[
                        FolioManual(page)
                    ]
                )
            )
        
        if page.route=='/tag_auto':
            page.views.append(
                View(
                    route= '/tag_auto',
                    controls=[
                        TagAutomatico(page)
                    ]
                )
            )
        
        if page.route == '/tag_manual':
            page.views.append(
                View(
                    route='/tag_manual',
                    controls=[
                        TagManual(page)
                    ]
                )
            )
        
        if page.route == '/add':
            page.views.append(
                View(
                    route= '/add',
                    controls=[
                        Add(page)
                    ]
                )
            )
        
        if page.route == '/generado':
            page.views.append(
                View(
                    route= '/generado',
                    controls=[
                        Generado(page)
                    ]
                )
            )
        page.update()
    page.on_route_change = route_change
    page.go('/login')

if __name__ == '__main__':
    app(target=main)