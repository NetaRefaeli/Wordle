class UI:
  welcome: str = (''' !"ברוכים הבאים למשחק "מילה אחת ביום
  :הנחיות
  1. עלייך לנחש מילה בעלת 5 אותיות
  2. אות ירוקה = אות קיימת במיקום הנכון
  3. אות צהובה = אות קיימת אך לא במיקום הנכון
  4. יש לך 6 ניחושים
  ''')
  round: int = 1
  user_guess: str = ''
  wordle_game = None

  def __init__(self, wordle_game):
    self.wordle_game = wordle_game

  def print_welcome_message (self) -> None:
    print(self.welcome)

  def get_user_guess(self) -> str:
    self.user_guess = input('_ _ _ _ _\n')
    while self.wordle_game.is_real_word(self.user_guess) == False:
      print('מילה לא קיימת, נסה שוב')
      self.user_guess = input('_ _ _ _ _\n')

    print(self.wordle_game.check_input(self.user_guess))

  def time_until_next_word(self) -> str:
    tz = pytz.timezone('Israel')
    tomorrow = datetime.combine(date= date.today(),time = time(), tzinfo = tz)+ timedelta(days = 1)
    hours_until_next_word =  math.ceil((tomorrow - datetime.now(tz)).total_seconds()/60/60)
    print(f'שעות עד למילה הבאה {hours_until_next_word}')
