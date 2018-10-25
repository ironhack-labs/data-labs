![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | Error Handling and List Comprehensions

## Introduction

When doing data science, you might find yourself wanting to read lists of lists, filtering column names, removing vowels from a list or flattening a matrix. You can easily use a lambda function or a for loop; There are multiple ways to go about this. One other way to do this is by using **list comprehensions**.

As you have learned in today's learning, list comprehensions are a tool for transforming one list (any iterable actually) into another list. During this transformation, elements can be conditionally included in the new list and each element can be transformed as needed.

**Every list comprehension can be rewritten as a for loop but not every for loop can be rewritten as a list comprehension**. The key to understanding when to use list comprehensions is to practice identifying problems that *smell* like list comprehensions. If you can rewrite your code to look like a single loop, you can also rewrite it as a list comprehension. 

On the other hand, error and exception handling is a very important aspect of writing efficient and robust programs. Error handling guards against potential failures that would cause your program to exit in an uncontrolled fashion.This can have major consequences, imagine of a software for the automatic pilot in a passenger plane not working. 

In this exercise, you will both practice list comprehensions and error handling we discussed in the lessons and learn new techniques by looking up documentations and references. You will work on your own but remember the teaching staff is at your service whenever you encounter problems.


## Getting Started

Open the `main.py` file in the `your-code` directory with your favorite text editor. There are a bunch of commentations starting with `#` which instruct what you are supposed to do step by step. Follow the order of the instructions from top to bottom. Read each instruction carefully and provide your answer beneath it. You should also test your answers in Python in the terminal to make sure your responses are correct. 

For instance, in the first few lines of `main.py`, you see this example:

```python

#Example: 
""" 
eggs = (1,3,8,3,2)

percentage = [1/egg for egg in eggs]

"""

```

:bulb: The `#` sign in Python allows you to make single-line commentation. The `"""` (triple quotes) allows you to make multi-line commentation. Remember you always need a pair of triple quotes and you insert your commentations in between.

Continue answering each question until you reach the end of `main.py`.

## Deliverables

- `main.py` with your responses to each of the instructions.

## Submission

Upon completion, add your deliverables to git. Then commit git and push your branch to the remote.

## Resources

[List Comprehension Data Camp Tutorial](https://www.datacamp.com/community/tutorials/python-list-comprehension)

[Errors and exceptions Python3 documentation](https://docs.python.org/3/tutorial/errors.html)

[Python Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#built-in-exceptions)

[Exception Handling](https://www.datacamp.com/community/tutorials/exception-handling-python)

## Additional Challenges for the Nerds

If you are way ahead of your classmates and willing to accept some tough challenges about Error Handling and List Comprehensions, you will find three bonus questions in `main.py`.
