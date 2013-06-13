########################################################
# PROJECT	SHERLOCK
# FILENAME	profile.py
# AUTHOR	K. C. Chambers
# UPDATED	June 4th, 2013
########################################################
#
# This module provides a helper class that reads
# a given text file, and returns a list of instances
# that represent the word counts in the text.
#
########################################################

class Instance:
  def __init__ (self, c=""):
    self.words = {}	# words is a hash, containing counts for the five hundred most common words in the english language.
    self.c = c		# c represents the classifier for this data, if any is assigned.
  
    # create empty data for the hash.
    self.fill_hash ()
    
  def fill_hash (self):
    """ create blank entries for the 500 most common words in the english language, as defined in words.txt """
    
    # open the file "words.txt", go through it line by line, and make blank entries for each word.    
    f = open("words.txt", "r")    
    for line in f:
      self.words[line.strip()] = 0      
    f.close()
  
  def add_word (self, word):
    """ increment a word's count, assuming it is in the list already. """
    if word in self.words:
      self.words[word] = self.words[word] + 1

  def get_tablist (self, include_c = True):
    """ return a tab delineated list of word counts, and optionally include the classifier at the end """
    tablist = ""
        
    # go through all words in the list, sorted alphabetically, and add them to the tablist, with tabs between
    wordlist = self.words.keys()
    wordlist.sort()
    
    for word in wordlist:
      tablist += str(self.words[word]) + "\t"
    
    # include the classifier at the end
    if include_c:
      tablist += self.c
    return tablist

  def set_c (self, new_c):
    """ change the classifier for this instance """
    self.c = new_c

  def get_c (self):
    """ return the classifier for this instance """
    return self.c
  
def profile_file (filename, classifier=""):
  """ parse a file, and return a list of instance objects that represent it """
  instances = []
  
  # open the file
  f = open(filename, 'r')
  
  # start a new instance
  i = Instance(c=classifier)
  counter = 0
  
  # start reading lines
  for line in f:
    # break the line down into words by whitespace
    words = line.split()
    
    # remove all punctuation and convert words to lowercase.
    words = [word.lower().translate(None, '!@#$.,') for word in words]
    
    # go through these words    
    for word in words:
      # every 1,000 words, start a new instance
      counter += 1
      if counter > 999:
	instances.append(i)
	i = Instance(c=classifier)
	counter = 0
      i.add_word (word)
	
  # return a list of instances
  return instances
  
  
