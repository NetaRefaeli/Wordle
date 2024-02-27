import pickle
from datetime import date

from colors import Color
from constants import PATH_TO_PICKLE_FILE


class Wordle:
  word_of_the_day: str = ''
  all_words_dict: dict = {}
  round = 0
  _is_running = True

  def __init__(self):  # self is how the instance talks to itself
    # unpickle dict and save in this instance
    with open(PATH_TO_PICKLE_FILE, 'rb') as f:
      self.all_words_dict = pickle.load(f)

    # get the word of day and save in this instance as a parameter
    self.word_of_the_day: str = self.all_words_dict[date.today()]

  def get_word_of_the_day(self) -> str:
    return self.word_of_the_day

  def is_game_running(self) -> bool:
      return self._is_running and self.round < 6

  def is_real_word(self, user_guess: str) -> bool:
    if user_guess in list(self.all_words_dict.values()):
      return True
    else:
      return False

  def check_input(self, user_guess: str) -> str:
    # compare input with answer
    output = Color.BOLD
    correct_guess_output = Color.BOLD

    if user_guess == self.word_of_the_day:
      self._is_running = False
      correct_guess_output += Color.GREEN + user_guess
      return 'Correct!🥳\n' + correct_guess_output + Color.END

    for index, letter in zip(range(0,5) , user_guess):
      if self.word_of_the_day[index] == letter:
        output += Color.GREEN + letter + ' '
      elif letter in self.word_of_the_day:
         output += Color.YELLOW + letter + ' '
      else:
        output += Color.LIGHT_GREY + letter + ' '

    self.round += 1
    if self.round == 6:
      return output + '\nOpps.. you are out of guesses!\nThe correct word is: ' + self.word_of_the_day
    else:
      return output + Color.END
