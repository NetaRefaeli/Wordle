import re
import math
from datetime import date,timedelta,datetime, time

import streamlit as st


class UI:
  round: int = 1
  user_guess: str = ''
  wordle_game = None
  _start_play: bool = False

  def __init__(self, wordle_game):
    self.wordle_game = wordle_game

  def ask_user_if_to_play (self) -> bool:
    unswer = st.text_input('שנתחיל במשחק? כן/לא')
    if unswer not in ['כן','לא']:
      st.error("התשובה חייבת להכין את האחת המילים: כן/לא'")
    elif unswer =='כן':
      self.start_play = True
    else:
      self.start_play = False

  def get_user_guess(self) -> str:
    self.user_guess = st.text_input('_ _ _ _ _\n')
    while self.wordle_game.is_real_word(self.user_guess) == False:
      st.write('מילה לא קיימת, נסה שוב')
      self.user_guess = st.text_input('_ _ _ _ _\n')

    st.write(self.wordle_game.check_input(self.user_guess))

  def time_until_next_word(self) -> str:
    israel_offset = timedelta(hours=2)
    tomorrow = datetime.combine(date= date.today(),time = time())+ timedelta(days = 1) + israel_offset
    hours_until_next_word =  math.ceil((tomorrow - datetime.now()+israel_offset).total_seconds()/60/60)
    st.write(f'שעות עד למילה הבאה {hours_until_next_word}')
