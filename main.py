from wordle_game import Wordle
from user_interface import UI
import streamlit as st

if __name__ == '__main__':
  # creating an instance of class/type "Wordle"
  wordle_game = Wordle()
  wordle_ui = UI(wordle_game)

  # play
  st.write(wordle_ui.print_welcome_message())
  st.echo()
  with st.echo():
    while wordle_game.is_game_running():
      wordle_ui.get_user_guess()
  
    wordle_ui.time_until_next_word()