import pprint
from nicegui import ui
from nicegui.events import KeyEventArguments
from tt_state import GameTimer, app_settings, stats, tg
from word_logic import get_new_words
from stats_ui import stats_ui

@ui.refreshable
def test_container(): 

  tg.letter_refs = [] # clear it everytime the test resets
  tg.word_list = get_new_words(app_settings)
  
  with ui.element('div').classes('flex w-full justify-center my-sb') as test_cont:
      time_container()
        
      with ui.element('div').style("height: 153px; scroll-behavior: smooth;")\
        .classes("my-sb flex justify-start gap-[10px] rm-md text-1xl overflow-y-scroll")\
        .props('id=words_container') as container:
        tg.words_container = container
        
        for word in tg.word_list:
          with ui.row().classes('word').style('gap: 0; padding: 0 8px;') as word_section:
            tg.word_refs.append(word_section)  # <- store reference to word container
            letter_row = []
            
            for char in word:
              letter = ui.html(char, tag='span').classes('letter')
              letter_row.append(letter)
            
            tg.letter_refs.append(letter_row)
            tg.word_refs[0].classes(add='active')
            tg.letter_refs[0][0].classes(add='cursor-left')
    
  tg.test_cont = test_cont
  return test_cont

def time_container():  
  with ui.row().classes("timer justify-between items-center w-full flex-nowrap gap-[5px] mb-[1rem]") as time_container:
    tg.time_container = time_container

    with ui.column().classes('gap-1 w-full').bind_visibility_from(timer.timer, 'active', value=False):
      ui.label('Type to start test.')\
        .classes("text-semibold text-[1rem] w-full text-center")\
        .bind_visibility_from(timer.timer, 'active', value=False)
      
      ui.label('Press Shift + Space to pause.')\
        .classes("text-semibold text-[1rem] w-full text-center")\
        .bind_visibility_from(timer.timer, 'active', value=False)

    tg.time_label = ui.label(f"{app_settings.duration}s")\
      .classes("rm-md text-[1rem] w-[4%] text-primary")\
      .bind_visibility_from(timer.timer, 'active')
    
    tg.time_slider = ui.slider(min=-0, max=app_settings.duration, value=app_settings.duration)\
      .props("color=primary track-size=14px thumb-size=0px readonly")\
      .style("width: 96%").bind_visibility_from(timer.timer, "active")
    
  return time_container

def refresh_words_ui():
    tg.words_container.clear()
    
    tg.word_refs = []
    tg.letter_refs = []
    tg.word_list = get_new_words(app_settings)

    test_container.refresh()

def show_test_results():
  grade_test()

  with ui.column().classes('absolute-center items-center').style("width: 85%;"):

    tg.stats_container = stats_ui(restart_game)
    tg.stats_container.set_visibility(True)
  
  tg.words_container.set_visibility(False)
  tg.time_container.set_visibility(False)
  
def handle_key(e: KeyEventArguments):
  # print(e.key)
  ignored_keys = {
        'Shift', 'Control', 'Alt', 'Meta', 'Escape', 'Tab',
        'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight',
        *[f'F{i}' for i in range(1, 13)]
    }
  
  # Detect Shift + Space to toggle pause
  if e.key == ' ' and e.modifiers.shift and e.action.keydown:
      if timer.is_active():
          timer.timer.deactivate()
          stats.is_paused = True
          print("Paused")
      else:
          timer.timer.activate()
          stats.is_paused = False
          print("Resumed")
      return


  # Don't do anything if paused
  if stats.is_paused:
      return
  
  # === Ignore modifier and non-letter keys ===
  if str(e.key) in ignored_keys:
    return

  # Skip keys that shouldn’t start the test
  if not timer.is_active():
      if str(e.key).isalpha() and len(str(e.key)) == 1:  # only a-z
        stats.is_paused = False
        timer.start()
      else:
        return

  # Ignore all keyup actions
  if not e.action.keydown:
      return
 
  if all(x == False for x in e.modifiers):
    
    if tg.word_idx >= len(tg.letter_refs): 
      return # return if index is bigger than the amount of words
    elif e.key == ' ': 
      handle_spacebar()
      return
    elif e.key == "Backspace":
      handle_backspace()
      return
    else:
      handle_letter_input(e.key)

def handle_spacebar():
  # grading the word just typed
  word_chars = tg.letter_refs[tg.word_idx]
  if all("correct" in l.classes for l in word_chars):
      tg.word_refs[tg.word_idx].classes(remove='wrong', add='typed correct')
  else:
      tg.word_refs[tg.word_idx].classes(remove='correct', add='typed wrong')

  # remove active class from word
  tg.word_refs[tg.word_idx].classes(remove='active')
  
  for l in word_chars:
     l.classes(remove='cursor cursor-left')

     if l.classes == ['letter']:
       l.classes(add='missed')
  
  # move to next word
  tg.word_idx += 1
  tg.char_idx = 0

  # get new active word/chars and update classes
  new_word = tg.word_refs[tg.word_idx]
  new_word.classes(add="active")
  
  first_letter = tg.letter_refs[tg.word_idx][0]
  first_letter.classes(add='cursor-left')

  # auto scroll to active word AFTER layout updates
  ui.timer(0.1, lambda: ui.run_javascript('''
  const container = document.getElementById('words_container');
  const active = container?.querySelector('.word.active');
  if (active) {
      // how tall each “line” is:
      const lineHeight = container.clientHeight / 3;
      // where the active word sits relative to the top of the scroll area:
      const offset  = active.offsetTop - container.offsetTop;
      // scroll so that the active word lands exactly one lineHeight down:
      const target  = offset - lineHeight;
      container.scrollTo({ top: target, behavior: 'smooth' });
  }
'''))
  
  # ui.timer(0.1, lambda: ui.run_javascript('''
  #     const container = document.getElementById('words_container');
  #     const active = container?.querySelector('.word.active');
  #     if (active) {
  #         const containerRect = container.getBoundingClientRect();
  #         const activeRect = active.getBoundingClientRect();

  #         const isVisible =
  #             activeRect.top >= containerRect.top &&
  #             activeRect.bottom <= containerRect.bottom;

  #         if (!isVisible) {
  #             active.scrollIntoView({ behavior: 'smooth', block: 'center' });
  #         }
  #     }
  # '''))

def handle_backspace(): 
  ############ If at the start of the word ##############
  if tg.char_idx == 0:
    if tg.word_idx == 0:
      char = tg.letter_refs[tg.word_idx][tg.char_idx]
      
      if 'cursor' in char.classes:
        char.classes(remove='wrong correct missed cursor', add='cursor-left')    
      else:
        return

    # Update stats
    word_classes = tg.word_refs[tg.word_idx].classes
    char = tg.letter_refs[tg.word_idx][tg.char_idx]

    if any(x in char.classes for x in ['wrong', 'correct', 'cursor']):
      char.classes(remove='wrong correct cursor', add='cursor-left')
      return 

    # Unmark the current word
    tg.word_refs[tg.word_idx].classes(remove='active wrong correct typed')
    for l in tg.letter_refs[tg.word_idx]:
      l.classes(remove='wrong correct cursor cursor-left')

    # Move to previous word
    tg.word_idx -= 1
    tg.char_idx = len(tg.letter_refs[tg.word_idx]) - 1  # set this to the last index of that word
   
    tg.letter_refs[tg.word_idx][tg.char_idx].classes(add='cursor')
    
    return

  ######### NORMAL CASE: not at start of word ################
  else:
    char_list = tg.letter_refs[tg.word_idx]

    # Defensive: remove cursor from current char
    if tg.char_idx < len(char_list):
      char_list[tg.char_idx].classes(remove='cursor cursor-left')
    
    
    active_char = char_list[tg.char_idx]

    # Remove extra char from DOM and memory
    if 'extra' in active_char.classes:
      char_list.pop(tg.char_idx)
      active_char.delete()


    active_char.classes(remove='wrong correct cursor-left cursor missed extra')
    
    # Move index back
    tg.char_idx -= 1
    tg.letter_refs[tg.word_idx][tg.char_idx].classes(add='cursor')

def handle_letter_input(key):
  word = tg.letter_refs[tg.word_idx]

  # Put cursor AFTER current letter (but don't move char_idx)
  if 'cursor-left' in word[tg.char_idx].classes and tg.char_idx == 0:
    word[tg.char_idx].classes(remove='cursor-left', add='cursor')

  # Normal case: Advance to next char
  else:
    tg.char_idx += 1
    
    # Remove cursor from all letters first
    for letter in word:
        letter.classes(remove='cursor')

    # Prevent out-of-bounds
    if tg.char_idx >= len(word):
        add_extra_char(key)
        return
    #mark word as typed if all letters have been typed, even if user hasn't pressed spacebar
    if tg.char_idx == len(word)-1:
      tg.word_refs[tg.word_idx].classes(add='typed')
    
    word[tg.char_idx].classes(add='cursor')

  if key == word[tg.char_idx].content:
      word[tg.char_idx].classes(add='correct')
  else:
      word[tg.char_idx].classes(add='wrong')

def add_extra_char(key):
  key_str = str(key)
  current_letters = tg.letter_refs[tg.word_idx]
  
  # Remove old cursor before adding new letter
  if current_letters:
      current_letters[-1].classes(remove='cursor')

  new_letter = ui.html(content=key_str, tag='span').classes('letter extra cursor')

  #Add new letter element to refs. array
  current_letters.append(new_letter)
  
  #Move it to words_container so it shows up in DOM
  word_container = tg.word_refs[tg.word_idx]
  new_letter.move(word_container)

def grade_test():
  
  for index, word in enumerate(tg.word_refs):
    if 'typed' in word.classes:
      
      if 'correct' in word.classes:
        stats.correct_words += 1
        
      stats.total_words += 1

      for char in tg.letter_refs[index]:
        if 'correct'in char.classes:
          stats.correct_chars += 1

        elif 'wrong' in char.classes:
          stats.mistakes += 1
        elif 'extra' in char.classes:
          stats.extra_chars += 1
        elif 'missed' in char.classes:
          stats.missed += 1
  
  total_chars = (stats.correct_chars + stats.mistakes + stats.extra_chars)
  stats.wpm = (stats.correct_chars / 5) * (60/app_settings.duration)
  stats.raw = (total_chars / 5) * (60/app_settings.duration)
  stats.accuracy = float(stats.correct_chars * 100 / total_chars)
  stats.cpm = total_chars * (60 / app_settings.duration)

def restart_game():
  timer.timer.update()
  tg.stats_container.set_visibility(False)
  stats.reset()
  tg.word_idx = 0
  tg.char_idx = 0
  refresh_words_ui()
  tg.words_container.set_visibility(True)
  tg.time_container.set_visibility(True)
  tg.keyboard.active = True
  timer.stop()

tg.keyboard = ui.keyboard(on_key=handle_key, active=True)

timer = GameTimer(duration=app_settings.duration, 
                  on_end_callback=show_test_results, 
                  keyboard=tg.keyboard)





