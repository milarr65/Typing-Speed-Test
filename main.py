# macOS packaging support
from multiprocessing import freeze_support  # noqa
freeze_support()  # noqa

from pathlib import Path
from nicegui import ui, app, native
from frame import frame
from test_functions import test_container


assets_path = Path(__file__).parent / 'static'
media = Path(__file__).parent / 'media'

app.add_static_files('/static', f'{assets_path}')
app.add_media_files("/media", media)
ui.add_head_html(f'''
                 <link rel="stylesheet" type="text/css" href="/static/styles.css">
                 <link type="image/png" sizes="96x96" rel="icon" href="/media/icons8-t-key-color-96.png">
                 ''')

my_icon = "Typing Speed Test\\media\\icons8-t-key-96.png"


ui.tooltip.default_classes('rm-md text-sm bg-dark')


with frame():
 
 test_container()


ui.run(title="Typing Speed Test", 
       favicon=my_icon, 
       show=False, 
       native=False, 
       port=native.find_open_port(),
       reload=False)

