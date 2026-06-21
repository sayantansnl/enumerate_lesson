# ENUMERATE

At this point, you’re pretty aware of `for` loops and iterables (lists, tuples, dicts, strings, etc.). 

If you were to keep track of the index of every item and print the value of an individual item along with an incremented index, you’d probably write a program like this: 

```
pure_saiyans = [‘Kakarot’, ‘Vegeta’, ‘Nappa’, ‘Raditz’, ‘Bardock’]

for i in range(0, len(pure_saiyans)):
    print(f’{i + 1}: {pure_saiyans[i]}’) 

# 1: Kakarot
# 2: Vegeta
# 3: Nappa
# 4: Raditz
# 5: Bardock
```

This approach may be fine for other programming languages like C or Java, but we’re writing Python. And we have to be [Pythonic](https://en.wikipedia.org/wiki/Zen_of_Python#Being_Pythonic) (ugly code: yuck; beautiful code: yayyy)! 

But how do we make this code beautiful? That’s where the `enumerate` function comes in. We can write the above code like this: 

```
pure_saiyans = [‘Kakarot’, ‘Vegeta’, ‘Nappa’, ‘Raditz’, ‘Bardock’]

for count, saiyan in enumerate(pure_saiyans, start=1):
    print(f’{count}: {saiyan}’)

# 1: Kakarot
# 2: Vegeta
# 3: Nappa
# 4: Raditz
# 5: Bardock
```

Isn’t this beautiful? The syntax of `enumerate` is really simple.

`enumerate(iterable, start)`

* `enumerate`: function name.
* `iterable`: list, tuples, dicts, strings, etc.
* `start` (optional): integer value that specifies the starting point of the counter, defaults to 0 if not mentioned.

The enumerate function returns an enumerate object. It looks something like this:

```
saiyan_obj = enumerate([pure_saiyans]) # we are not specifying ‘start’
print(saiyan_obj)

# <enumerate object at 0x7f88bc123450>
```

We can use the `next` function on the enumerate object to get the next item in the list in the form of a tuple. 

`(index, item)`

We will print the names in `pure_saiyans` like this as well:

```
print(next(saiyan_obj)) # (0, ‘Kakarot’)
print(next(saiyan_obj)) # (1, ‘Vegeta’)
print(next(saiyan_obj)) # (2, ‘Nappa’)
print(next(saiyan_obj)) # (3, ‘Raditz’)
print(next(saiyan_obj)) # (4, ‘Bardock’)
```

If you keep calling `next()` after the iterator is completely empty, Python will raise a `StopIteration` error.

To prevent your code from crashing, you can pass a default value to the `next` function as a fallback:

`print(next(saiyan_obj, "No more Saiyans!"))  # No more Saiyans!`

### Assignment (difficulty: 7)

You are given a list of integers representing consecutive sensor readings. Due to intermittent interference, some readings are corrupted and show up as `-1`.

Write a function `clean_and_analyze(readings)` that does two things using `enumerate()`:

* **Fix the Corrupted Data:** Replace any -1 with the average of its immediate neighbors (the number right before it and the number right after it). Assume the first and last items in the list will never be `-1`.
* **Find the Peaks:**  Identify the indices of all "peaks" in the corrected data. A peak is a number that is strictly greater than both its left and right neighbors.

Example input: 
`readings = [10, 12, -1, 14, 11, 15, 12]`

Example Output:

```
# The -1 at index 2 gets replaced by the average of 12 and 14 -> 13
Cleaned Data: [10, 12, 13, 14, 11, 15, 12]

# Peaks are 14 (index 3) and 15 (index 5)
Peaks found at indices: [3, 5]
```

Return the result as tuple: `(Cleaned Data, Peaks)`
