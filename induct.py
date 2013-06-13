########################################################
# PROJECT	SHERLOCK
# FILENAME	induct.py
# AUTHOR	K. C. Chambers
# UPDATED	June 4th, 2013
########################################################
#
# This module looks at a file and attempts to
# classify it.
#
########################################################
import Orange
import sys
import shutil
import profile

def main():
  """ look at a file, convert it to instances, and attempt to classify it! """
  
  # we need exactly one argument
  if len(sys.argv) != 2:
    print "Induct.Py requires at exactly one argument."
    return

  filename = sys.argv[1]

  # create a temporary file to store this information in
  shutil.copyfile ("template.txt", "temp.tab")

  # open the file, and convert it to instances.
  instances = profile.profile_file (filename)
  
  # write instances to the now empty file.
  f = open('temp.tab', 'a')
  for i in instances:
      f.write(i.get_tablist() + '\n')
  f.close()
  
  # set up the data
  train = Orange.data.Table("brain.tab")
  test = Orange.data.Table("temp.tab")
  
  classifier = Orange.classification.neural.NeuralNetworkLearner()
  #classifier = Orange.regression.tree.TreeLearner(m_pruning = 2)
  learner = classifier(train)
   
  # now let's try something INDUCTIVE!
  print learner(test[0])

if __name__ == '__main__':
  main()