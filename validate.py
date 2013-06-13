########################################################
# PROJECT	SHERLOCK
# FILENAME	validate.py
# AUTHOR	K. C. Chambers
# UPDATED	June 4th, 2013
########################################################
#
# This module runs cross-validation checks to
# verify that the learning algorithm is doing a
# good job.
#
##################################################

import Orange

data = Orange.data.Table("brain.tab")

#learner = classifier(train)

tree = Orange.classification.tree.TreeLearner(sameMajorityPruning=1, mForPruning=2)
tree.name = "tree"
nbc = Orange.classification.bayes.NaiveLearner()
nbc.name = "nbc"
lr = Orange.classification.logreg.LogRegLearner()
lr.name = "lr"

learners = [nbc, tree, lr]
print " "*9 + " ".join("%-4s" % learner.name for learner in learners)
res = Orange.evaluation.testing.cross_validation(learners, data, folds=5)
print "Accuracy %s" % " ".join("%.2f" % s for s in Orange.evaluation.scoring.CA(res))
print "AUC      %s" % " ".join("%.2f" % s for s in Orange.evaluation.scoring.AUC(res))