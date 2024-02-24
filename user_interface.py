import re
import math
from datetime import date,timedelta,datetime, time

import streamlit as st


class UI:
  round: int = 1
  user_guess: str = ''
  wordle_game = None


  def __init__(self, wordle_game):
    self.wordle_game = wordle_game

  @staticmethod
  def ask_user_if_to_play () -> bool:
    answer = st.text_input('שנתחיל במשחק? כן/לא')
    while answer not in ['כן','לא']:
      st.error("התשובה חייבת להכיל את האחת המילים: כן/לא'")
      answer = st.text_input('שנתחיל במשחק? כן/לא')
    
    if answer =='כן':
      return True
    else:
      return False

  def get_user_guess(self) -> str:
    self.user_guess = st.text_input('_ _ _ _ _\n')
    while self.wordle_game.is_real_word(self.user_guess) == False:
      st.error('מילה לא קיימת, נסה שוב')

    st.write(self.wordle_game.check_input(self.user_guess))

  def time_until_next_word(self) -> str:
    israel_offset = timedelta(hours=2)
    tomorrow = datetime.combine(date= date.today(),time = time())+ timedelta(days = 1) + israel_offset
    hours_until_next_word =  math.ceil((tomorrow - datetime.now()+israel_offset).total_seconds()/60/60)
    st.write(f'שעות עד למילה הבאה {hours_until_next_word}')
