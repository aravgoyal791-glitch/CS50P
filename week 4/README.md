# CS50P Week 4

## Completed Problems

- Emojize
- Frank, Ian and Glen's Letters (Figlet)
- Adieu, Adieu
- Guessing Game
- Little Professor
- Bitcoin Price Index

---

## Emojize

Converts emoji aliases into Unicode emojis using the `emoji` module.

Example:
```
Input: :thumbs_up:
Output: 👍
```

---

## Frank, Ian and Glen's Letters (Figlet)

Uses the `pyfiglet` module to print text as ASCII art.

Features:
- Random font if no arguments are given.
- Specific font using `-f` or `--font`.
- Exits with `Invalid usage` for invalid arguments.

Example:
```
python figlet.py -f slant
Input: CS50
```

---

## Adieu, Adieu

Reads names until EOF and prints them in proper English using the `inflect` module.

Example:
```
Name: Liesl
Name: Friedrich
Name: Louisa
Ctrl-D

Adieu, adieu, to Liesl, Friedrich, and Louisa
```

---

## Guessing Game

Generates a random number and repeatedly asks the user to guess until the correct answer is entered.

Outputs:
- Too large!
- Too small!
- Just right!

---

## Little Professor

Generates 10 addition problems based on the selected difficulty level.

Rules:
- Three attempts per question.
- Prints `EEE` for incorrect answers.
- Displays the correct answer after three incorrect attempts.
- Prints the final score.

---

## Bitcoin Price Index

Retrieves the current Bitcoin price from CoinDesk using the `requests` library and calculates the value of the specified number of Bitcoins.

Example:
```
python bitcoin.py 2.5
$244,612.5608
```

---

## Libraries Used

- random
- sys
- requests
- pyfiglet
- emoji
- inflect

---

## Author

Aarav Goyal
