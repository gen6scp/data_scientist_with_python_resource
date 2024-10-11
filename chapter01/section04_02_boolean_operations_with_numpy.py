## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section4_01_comparing_arrays_with_numpy import group_a, group_b, np

sys.stdout = org_stdout


# Use logical_or to find ages less than 20 or greater than 35
result = np.logical_or(group_a < 20, group_a > 35)
print(result)

# Use logical_and to find ages between 20 and 35 inclusive
result_and = np.logical_and(group_a >= 20, group_a <= 35)
print(result_and)
