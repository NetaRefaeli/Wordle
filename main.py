from wordle_game import Wordle
from user_interface import UI
import streamlit as st

if __name__ == '__main__':
  # creating an instance of class/type "Wordle"
  wordle_game = Wordle()
  wordle_ui = UI(wordle_game)

  # play
  with st.echo():
    st.write(''' # !"ברוכים הבאים למשחק "מילה אחת ביום
  :הנחיות
  1. עלייך לנחש מילה בעלת 5 אותיות
  2. אות ירוקה = אות קיימת במיקום הנכון
  3. אות צהובה = אות קיימת אך לא במיקום הנכון
  4. יש לך 6 ניחושים
  ''')
    while wordle_game.is_game_running():
      wordle_ui.get_user_guess()

    wordle_ui.time_until_next_word()