from nicegui import ui
from contextlib import contextmanager
from menu import menu
import datetime
from about_page import about_page


@contextmanager
def frame():
  global header
  with ui.header().classes('my-sb rm-md row items-center bg-transparent p-[10px] text-gray-900 dark:text-white fill-gray-900 dark:fill-white'):
    ui.button(on_click=lambda: left_drawer.toggle(), 
              icon='settings')\
                .props('flat color="inherit"')\
                .classes('text-inherit')\
                .tooltip('Preferences')
    with ui.tabs().classes('w-auto').props('shrink stretch') as tabs:
       about = ui.tab("About")
       test = ui.tab('Test')
    
    ui.space()
    ui.label('Typing Speed Test').classes('no-underline text-inherit font-bold text-xl mx-(10px) p-[3px]')
    ui.html('<img width="48" height="48" src="https://img.icons8.com/color/48/t-key.png" alt="t-key"/>').classes('text-inherit')

  with ui.footer(value=False, fixed=False, bordered=True)\
    .classes('bg-transparent justify-center') as footer:
      with ui.column().classes('gap-2 text-sm font-medium items-center opacity-[0.8]'):
          ui.label(f"Created by Mila Arroyo © {datetime.datetime.now().year}")
          ui.markdown("Find me on [Github](https://github.com/milarr65)")


  with ui.left_drawer(value=False).props('overlay bordered').classes('rm-md my-sb bg-dark-page absolute-center items-center overflow-x-hidden') as left_drawer:
    menu()


  with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20).tooltip('Toggle footer'):
      ui.button(on_click=footer.toggle, icon='expand_circle_down').classes('material-symbols-rounded').props('fab-mini')

  
  with ui.column().classes('my-sb absolute-center items-center h-[96%] justify-center').style("width: 80%;"):
    with ui.tab_panels(tabs, value=test).classes('w-full'):
        with ui.tab_panel(about):
          about_page()
        with ui.tab_panel(test):
          yield
    
