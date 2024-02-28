import math
from datetime import date,timedelta,datetime, time

from colors import Color


class UI:
  welcome: str  = (
  f"{Color.BOLD}Welcome to Wordle!{Color.END}\n"
  f"{Color.UNDERLINE_START}Instructions:{Color.UNDERLINE_END}\n"
  "1. You should guess a 5-letter-only word.\n"
  "2. Green letter = letter is guessed in the right place.\n"
  "3. Yellow letter = letter exists in word but at another place.\n"
  "4. You have 6 guesses.\n"
  "Good luck! 🍀\n"
  )
  round: int = 1
  wordle_game = None


  def __init__(self, wordle_game):
    self.wordle_game = wordle_game
  
  def print_welcome_message (self) -> None:
    print(self.welcome)

  @staticmethod
  def ask_user_if_to_play () -> bool:
    answer = input('Shell we play?\n Yes / No\n ')
    while answer.lower() not in ['yes','no','y','n']:
      print("Sorry.. Coudn't undestand your answer.")
      answer = input('Is it Yes or No?\n')
    
    if answer.lower() in ['yes','y']:
      return True
    else:
      return False

  def get_user_guess(self) -> str:
    user_guess = input('_ _ _ _ _\n')
    while self.wordle_game.is_real_word(user_guess) == False:
      print('word is not valid, please try again.')
      user_guess = input('_ _ _ _ _\n')

    print(self.wordle_game.check_input(user_guess))

  def time_until_next_word(self) -> str:
    israel_offset = timedelta(hours=2)
    tomorrow = datetime.combine(date= date.today(),time = time())+ timedelta(days = 1) + israel_offset
    hours_until_next_word =  math.ceil((tomorrow - datetime.now()+israel_offset).total_seconds()/60/60)
    print(f'{hours_until_next_word} hours for the next word.😊')
