# 1. Sorting by Keys

data = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = {k: data[k] for k in sorted(data)}
# Output: {'a': 1, 'b': 2, 'c': 3}

sorted_dict = {key: data[key] for key in sorted(data)}
data = {'a': 3, 'b': 1, 'c': 2}
sorted_dict_by_key = {key: value for key,value in sorted(data.items())}
print(sorted_dict)
print(sorted_dict_by_key)