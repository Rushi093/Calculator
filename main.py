git branch -m main <BRANCH>
git fetch origin
git branch -u origin/<BRANCH> <BRANCH>
git remote set-head origin -a
from mean_var_std import calculate
from test_module import TestMeanVarStd
import unittest

# Manual test
print(calculate([0,1,2,3,4,5,6,7,8]))

# Run unit tests
if __name__ == "__main__":
    unittest.main()

