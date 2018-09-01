import hangman

game = Hangman("(word)", "(clue)")
while game.status == False:
  game.printState()
  game.check(raw_input("Guess a letter:"))
  game.updateStatus()
