########################################################
# PROJECT	SHERLOCK
# FILENAME	observe.py
# AUTHOR	K. C. Chambers
# UPDATED	June 4th, 2013
########################################################
#
# This module reads in a collection of text files,
# converts them to instances using profile.py, adds
# them to the datafile, and then trains on them.
#
# At startup, this module takes a list of arguments.
# The first argument is the classifier to be associated
# with the files to be observed, and everything after
# this is the list of files.
#
########################################################

import sys
import Orange
import profile

def main():
  """ reads a collection of text files, converts them to instances, adds them to the datafile, and train on them."""
  
  # make sure the right number of arguments are there.
  if len(sys.argv) < 3:
    print "Observe.Py requires at least one classifier and filename to run."
    return
  
  # read arguments
  classifier = sys.argv[1]
  filenames = sys.argv[2:]
  
  # go through each file
  for filename in filenames:
    
    # convert each file into a list of instances
    instances = profile.profile_file (filename, classifier)
    
    # open the datafile
    f = open('brain.tab', 'a')
    
    # add these instances to the datafile
    for i in instances:
      f.write(i.get_tablist() + '\n')
      
    # train on the datafile
  
if __name__ == '__main__':
  main()