from nicegui import ui
from tt_state import app_settings, tg
from test_functions import restart_game, timer

def menu():
  ui.label('Preferences').classes('text-2xl mb-[1rem]')

  ui.label('Test Duration').classes('text-bold')
  duration = ui.toggle({15: '15s', 
                        30: '30s', 
                        60: '60s', 
                        120: '120s'}, 
                        value=app_settings.duration, 
                        on_change=lambda: update_settings('duration', duration.value))\
                          .classes('mb-[1rem]')

  ui.label('Difficulty').classes('text-bold').tooltip('Prioritize short, medium or long words.')
  difficulty = ui.toggle(['easy', 'medium', 'hard'], 
                         value=app_settings.difficulty, 
                         on_change=lambda: update_settings('difficulty', difficulty.value))\
                          .classes('mb-[1rem]')

  ui.label('Word Variety').classes('text-bold').tooltip('Words sample size')
  word_var = ui.toggle({
                        200: '200', 
                        500: '500', 
                        1000: '1k', 
                        3000: '3k', 
                        5000: '5k'}, 
                        value=app_settings.word_var, 
                        on_change=lambda: update_settings('word_var', word_var.value))\
                          .classes('mb-[1rem]')
  
  theme_label = ui.label('Dark theme: On').classes('text-bold')
 
  theme = ui.dark_mode(value=app_settings.dark_theme)
  
  with ui.row(align_items="center").classes("gap-0"):
    
    ui.icon("light_mode").style("font-size: 27px; padding: 6px;")
    
    ui.switch(value=app_settings.dark_theme,
              on_change=lambda: update_theme())\
      .props("color=primary")\
      .tooltip("Toggle dark mode")\
      .set_visibility(True)
    
    ui.icon("dark_mode").style("font-size: 27px; padding: 6px;")


  
  def update_settings(option, value):
    match option:
      case "duration":
        app_settings.duration = value
        timer.set_duration(value)
      case 'difficulty':
        app_settings.difficulty = value
      case 'word_var':
        app_settings.word_var = value
    
    app_settings.save()
    restart_game()
    


  def update_theme():
    theme.toggle()
    if theme.value:
      theme_label.set_text('Dark theme: On')
      app_settings.dark_theme = theme.value
    else:
      theme_label.set_text('Dark theme: Off')
      app_settings.dark_theme = False
    
    app_settings.save()
