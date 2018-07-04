# function that returns count for letters and digits in sentence.
def letters_and_digits(sentence):
  count = {"digits": 0, "letters": 0}
  for ch in sentence:
    if ch.isalpha():
      count['letters'] += 1
      # have to include constraint for punctuation.
    elif not ch.isalpha() and ch != " ":
      count ['digits'] += 1
  return count['letters'], count['digits']


assert letters_and_digits("This sentence has 31 letters and 3 digits") == (31,3)
