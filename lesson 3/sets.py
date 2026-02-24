from PIL.ImageChops import difference
from pandas.core.computation.expr import intersection

my_set = {1,2,3,3,4,5,6}

print(my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_result_method = set1.union(set2)

union_result_operator = set1 | set2

print(union_result_method)
print(union_result_operator)

intersection_results_method= set1.intersection(set2)
intersection_results_operator = set1 & set2

print(intersection_results_method)
print(intersection_results_operator)

difference_results_method = set1.difference(set2)
difference_results_operator = set1 - set2

print(difference_results_method)
print(difference_results_operator)

symetric_difference_method = set1.symmetric_difference(set2)
symetric_difference_operator = set1 ^ set2

