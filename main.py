from wordle_game import Wordle
from user_interface import UI


if __name__ == '__main__':
# creating an instance of class/type "Wordle"
  wordle_game = Wordle()
  wordle_ui = UI(wordle_game)
  print(wordle_game.word_of_the_day)
  
  # welcome message
  wordle_ui.print_welcome_message()
  does_user_want_to_play = wordle_ui.ask_user_if_to_play()
  while does_user_want_to_play == True and wordle_game.is_game_running() == True:
    wordle_ui.get_user_guess()

  wordle_ui.time_until_next_word()