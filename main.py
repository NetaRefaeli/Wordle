from wordle_game import Wordle
from user_interface import UI

if __name__ == '__main__':
  # creating an instance of class/type "Wordle"
  wordle_game = Wordle()
  wordle_ui = UI(wordle_game)

  # play
  wordle_ui.print_welcome_message()
  while wordle_game.is_game_running():
    wordle_ui.get_user_guess()

  wordle_ui.time_until_next_word()