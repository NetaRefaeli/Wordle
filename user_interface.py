import re
from datetime import date,timedelta,datetime, time
import math

class UI:
  start_play: bool = False
  round: int = 1
  user_guess: str = ''
  wordle_game = None

  def __init__(self, wordle_game):
    self.wordle_game = wordle_game

  def ask_user_if_to_play (self) -> None:
    try:
      unswer = input('שנתחיל במשחק? כן/לא')
      if unswer =='כן':
        self.start_play = True
      else:
        pass
    except:
      self.start_play = input('התשובה חייבת להכין את האחת המילים: כן/לא')

  def get_user_guess(self) -> str:
    self.user_guess = input('_ _ _ _ _\n')
    while self.wordle_game.is_real_word(self.user_guess) == False:
      print('מילה לא קיימת, נסה שוב')
      self.user_guess = input('_ _ _ _ _\n')

    print(self.wordle_game.check_input(self.user_guess))

  def time_until_next_word(self) -> str:
    israel_offset = timedelta(hours=2)
    tomorrow = datetime.combine(date= date.today(),time = time())+ timedelta(days = 1) + israel_offset
    hours_until_next_word =  math.ceil((tomorrow - datetime.now()+israel_offset).total_seconds()/60/60)
    print(f'שעות עד למילה הבאה {hours_until_next_word}')
