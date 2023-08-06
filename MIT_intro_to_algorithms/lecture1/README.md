# Birthday Match Runtime Comparison

This code compares the runtime of two different implementations for finding matching birthdays - using a list vs. using a dictionary.

## Overview

The `birthday_match_list` function stores student name and birthday pairs in a list. It loops through each pair and checks if any previous student has the same birthday.

The `birthday_match_dict` function stores the student information in a dictionary, with the birthday as the key. It simply checks if a birthday already exists in the dictionary.

To test the runtime, 1000 random students are generated. The two functions are timed using the `timeit` module, running 100 times each.

## Results

The dictionary implementation runs significantly faster:

```
Birthday match (list) took 4.57722 seconds
Birthday match (dict) took 0.01517 seconds  
```

Using a dictionary provides O(1) lookup time versus the O(n) lookup with a list. This major difference in runtime is evident with even just 1000 students.
