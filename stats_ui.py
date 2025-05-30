from nicegui import ui

def stats_ui(restart_game):
  from tt_state import app_settings, stats, tg

  with ui.column().classes('my-sb w-[85%] rm-md gap-9 transition-all duration-500 ease-in-out') as stats_container:
    ui.label('Results').classes('w-full text-center text-3xl text-bold')


    with ui.element('div').classes('row justify-between w-full gap-2'):
      
      with ui.element(tag='div').classes('column justify-start gap-4'):
        
        ui.label('Wpm').classes('text-xl')
        
        ui.label(f'{stats.wpm:.0f}')\
          .classes('text-primary big-num text-bold text-[4.25rem]')
        with ui.tooltip().props('anchor="top right" self="top middle"'):
          ui.html(f'<p>Words per minute <br/> {stats.wpm:.1f}</p>')
        
        with ui.row()\
          .classes('gap-3 items-end content-end'):
          
          with ui.tooltip(''):
            ui.html(f'<p>Wpm, mistakes included <br/> {stats.raw:.1f}</p>')
          
          ui.label('Raw').classes('text-base')
          
          ui.label(f'{stats.raw:.0f}').classes('text-primary text-xl')

      with ui.element(tag='div').classes('column justify-start gap-4'):
        
        ui.label('Accuracy').classes('text-xl')
        
        ui.label( f'{stats.accuracy:.1f}%').\
          classes('text-primary big-num text-bold text-[4.25rem]')
        
        with ui.tooltip().props('anchor="top right" self="top middle"'):
          ui.html((f'<p>Percentage of correctly pressed keys <br/>{stats.accuracy:.2f}%</p>'))

        with ui.row().classes('gap-3 items-end content-end'):
          
          ui.label('Time').classes('text-base')
          
          ui.label(f'{app_settings.duration}s').classes('text-xl text-primary')

      with ui.element('div').classes('column justify-start gap-4'):
        
        ui.label('Cpm').classes('text-xl')
        
        ui.label(f'{stats.cpm:.0f}')\
          .classes('text-bold big-num text-primary text-[4.25rem]')
        ui.tooltip('Characters per minute').props('anchor="top right" self="top middle"')

        with ui.row()\
          .classes('gap-3 items-end content-end')\
          .tooltip('Correct / mistakes / extra / missed'):
          
          ui.label('Typed').classes('text-base')
          
          ui.label(f'{stats.correct_chars}/{stats.mistakes}/{stats.extra_chars}/{stats.missed}')\
            .classes('text-xl text-primary')


    with ui.column().classes('w-full justify-start'):
      
      with ui.row().classes('justify-between w-full'):
        show_hist_btn = ui.dropdown_button('Show word history', 
                                color='primary',
                                # icon='keyboard_arrow_down', 
                                on_click=lambda: handle_button(),
                                value=False)\
          .classes('icon-right gap-2')\
          .props('dropdown-icon="keyboard_arrow_down" rounded outline no-caps persistent')
        
        ui.button("New Test", icon='refresh', on_click=lambda: restart_game())\
          .classes('self-center icon-right gap-2').props('no-caps outline rounded')

  
        with ui.element('div').bind_visibility_from(show_hist_btn, 'value')\
          .classes('row wrap gap-1 h-auto overflow-hidden text-lg transition-all duration-500 ease-in-out')\
            as word_hist:
           
          for idx, word in enumerate(tg.word_refs):
            
            if 'typed' in word.classes:
              w_copy = word
              w_copy.classes('text-lg')
              w_copy.move(word_hist)
              
              for char in tg.letter_refs[idx]:
                char_copy = char
                char.classes(remove='cursor')
                char_copy.move(w_copy)
    
  
  def handle_button():
    if show_hist_btn.value == True:
      word_hist.classes(remove='opacity-100 max-h-[500px]', add='opacity-0 max-h-0')
      show_hist_btn.set_text('Show word history')
    else:
      show_hist_btn.set_text('Hide word history')
      word_hist.classes(remove='opacity-0 max-h-0', add='opacity-100 max-h-[500px]')


  stats_container.move(tg.test_cont)
  tg.stats_container = stats_container
  stats_container.set_visibility(False)
  
  return stats_container
  