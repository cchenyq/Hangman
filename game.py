class Hangman:
  def __init__(self,word,clue):
    self.word = []
    for i in word:
      self.word += [i] #conversion from string to list

    self.clue = clue
    self.state = ["_"]*len(self.word)
    self.used = [] #bank of used and wrong letters
    self.count = 8 #number of remaining tries
    self.status = False
    print str(len(self.word)) + " letters long, " + clue

  def printState(self):
    print "Current state:"
    print self.state
    print "Used letters:"
    print self.used
    print "Number of remaining tries: " + str(self.count)

  def check(self, guess):
    if guess in self.word: #update self.state
      for i in range(0,len(self.state)):
        if self.word[i] == guess:
          self.state[i] = guess
    else:
      self.count -= 1
    self.used += [guess]
    self.updateStatus()

  def updateStatus(self):
    if self.count == 0:
      self.status = True
      print "Game over, the word was " + ''.join(self.word)
    elif self.state == self.word:
      self.status = True
      print "You won!"
