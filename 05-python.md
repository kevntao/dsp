# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

[![Think Python](img/think_python.png)](http://www.greenteapress.com/thinkpython/)

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

Complete the following exercises to check your ability with Python.

These exercises are implemented with doctests, which are runnable tests inside docstrings. Fill in the function definitions. Correct solutions will make it possible to run (for example) `python -m doctest strings.py` with no messages about failures.

 * [Strings](python/strings.py)
 * [Lists](python/lists.py)


---

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>Lists and Tuples are both collections with the ability to iterate through them by index. They are different in that tuples are immutable and its values cannot be changed once the tuple has been defined. Lists contain methods to append more items, remove them, insert into, and even extend its dimension.

>Tuples can work as keys in dictionaries because dictionary keys must be immutable. Once defined, the keys cannot be altered.

---


---

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>Lists and Sets are both collections that are mutable, in which values can be added, removed, inserted, etc. They differ in that lists are ordered and can be referenced by an index, whereas sets are not ordered. Sets also cannot have duplicate data as there is no index to differentiate identical values.

>For unique data points and checking if a value exists in a set of data, sets are faster because of the 'in' method that can return a boolean result if the value exists in the data. However, due to the lack of ordered indexes, iterating through a set would be more troublesome than using a list as each value would need to be 'pop'-ed from the set instead of iterating through the indexes of a list.

---


---

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>Python's lambda function is a quick way of creating a short function without coding a fully closed function definition and return. It is used to create quick disposable functions that can be used and then forgotten amidst coding.

> *colors = ["red", "blue", "green", "orange"]*  
> *for color in sorted(colors, key=lambda color: len(color)):*  
>     *print(color)*    

---


---

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>List comprehensions are ways to construct a list of values using almost direct mathematical formulas in code.

>S = [x**2 for x in range(1,10)]  
>print S  
>  
>T = map(lambda x: x**2, range(1,10))  
>print T  
>  
>squares = map(lambda x: x**2, range(1,10))  
>U = filter(lambda x: x > 0 and x < 100, squares)  
>print U  

---


Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

```bash
./markov.py chains.txt 40
```

A possible output would be:

> show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.
