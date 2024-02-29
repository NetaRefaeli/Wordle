# Wordle Game

## Pre-processing:

- Words source: [3000 most common words in english](https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/)
- Saved it in common_words.txt file.
- Filtered only for 5-letter words.
- Created the word for each day ahead in a dictionary {date: word}
- Save dictionary in a pickle 'daily_words.pickle'

## Wordle Game:

- The game logic, managed the rounds, is game still running, words validation functions..

## User Interface:

- Prints the output to the user and interacts with the WordleGame file.

## Instructions:

- Run the pre_processing.py (run it only once to create the daily words pickle). constants.py have the path to the pickle.
- Run main.py every time we want to play.

## Enjoy!