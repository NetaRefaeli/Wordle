from wordle_game import Wordle
from user_interface import UI
import streamlit as st

if __name__ == '__main__':
# creating an instance of class/type "Wordle"
  wordle_game = Wordle()
  wordle_ui = UI(wordle_game)
  # welcome message
  st.write(''' # !"ברוכים הבאים למשחק "מילה אחת ביום
  :הנחיות
  1. עלייך לנחש מילה בעלת 5 אותיות
  2. אות ירוקה = אות קיימת במיקום הנכון
  3. אות צהובה = אות קיימת אך לא במיקום הנכון
  4. יש לך 6 ניחושים
  ''')
  # play
  while wordle_ui.ask_user_if_to_play()==True and wordle_game.is_game_running()==True:
    wordle_ui.get_user_guess()

  wordle_ui.time_until_next_word()