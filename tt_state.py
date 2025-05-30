import os
import json
from anyio import Path
from nicegui import ui
from nicegui.elements.slider import Slider
from nicegui.elements.label import Label
from nicegui.elements.keyboard import Keyboard
from nicegui.element import Element

SETTINGS_FILE = Path(__file__).parent / 'settings.json'

class TestState:
  def __init__(self) -> None:
    # ----- Stats -----------
    self.total_words = 0   # Words fully typed, mistakes included
    self.correct_words = 0
    
    self.mistakes = 0      # amount of characters typed wrong
    self.correct_chars = 0 # amount of characters typed correctly
    self.missed = 0        # Untyped chars
    self.extra_chars = 0  
    
    self.accuracy = 0.0    # percentage of correct chars
    self.wpm = 0.0         # only includes correct words
    self.raw = 0.0         # includes all words typed
    self.cpm = 0.0         # chars per minute
    
    self.is_paused = False
  
  def reset(self):
    self.total_words = 0
    self.correct_words = 0
    
    self.mistakes = 0
    self.correct_chars = 0
    self.missed = 0
    self.extra_chars = 0 

    self.accuracy = 0.0
    self.wpm = 0.0
    self.raw = 0.0
    self.cpm = 0.0

    self.is_paused = False

class TestOptions():
  def __init__(self, duration: int = 30, dark_theme: bool = True, difficulty: str = 'easy', word_var: int = 1000) -> None:
    self.duration = duration
    self.difficulty = difficulty
    self.word_var = word_var
    self.dark_theme = dark_theme

  def to_dict(self):
    return {
      'duration': self.duration,
      'difficulty': self.difficulty,
      'word_var': self.word_var,
      'dark_theme': self.dark_theme,
    }
  
  def save(self):
    with open(SETTINGS_FILE, 'w') as file:
      json.dump(self.to_dict(), file)


  @classmethod
  def load(cls):
    if os.path.exists(SETTINGS_FILE):
      with open(SETTINGS_FILE, 'r') as file:
        data = json.load(file)
        return cls(**data)
      
    return cls() # return defaults if no file    

class GuiElements():
  def __init__(self) -> None:
    # ----- Dynamic elements -----------
    self.word_idx = 0           # To access words in list
    self.char_idx = 0           # to access letters in each word
    
    self.letter_refs = []       # stores references to every <span> letter element
    self.word_refs = []         # stores references to every <div> word element
    self.word_list = []
    
    self.time_slider: Slider
    self.time_label: Label
    self.words_container: Element
    self.time_container: Element
    self.test_cont: Element

    self.stats_container: Element
    self.keyboard: Keyboard


class GameTimer():
  def __init__(self, duration, on_end_callback, keyboard: Keyboard) -> None:
    self.duration = app_settings.duration
    self.count = duration
    self.on_end = on_end_callback
    self.timer = ui.timer(1.0, self._tick, active=False)
    self.keyboard = keyboard

  def start(self):
    self.timer.update()
    self.count = self.duration
    tg.time_slider.set_value(self.count)
    tg.time_label.set_text(f'{self.count}s')
    self.timer.activate()

  def _tick(self):
    if self.count > 0:
      self.count -= 1
      tg.time_slider.set_value(self.count)
      tg.time_label.set_text(f'{self.count}s')
    if self.count == 0:
      self.timer.deactivate()
      self.keyboard.active = False
      self.on_end()
  
  def stop(self):
    self.timer.deactivate()
    self.timer.update()

  def is_active(self):
    return self.timer.active
  
  def set_duration(self, new_duration):
    self.duration = new_duration

app_settings = TestOptions.load()
stats = TestState()
tg = GuiElements()

