![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | Code Simplicity and Efficiency

## Introduction

In the lesson we have learn a lot of principles and techniques about how to make codes simple and efficient. But it takes a lot of effort to achieve true code simplicity and efficiency. Below are several tips useful for you:

* Read a lot of source code from community websites such as GitHub and Stack Overview. Learn how top programmers write simple and efficient codes.

* Iterate your own code. When you are done writing a piece of code, you should always try to improve it even if it's functioning perfectly. Ask yourself whether you can make the code more clean and readable? Whether you can make it more efficient? 

* To make your code *perfect* is impossible becasue it will prevent you from delivering the project on time. There is a balance point of how much time you spend in improving the code versus delivering the project. As your programming skills improve, you will spend less and less time on iterating your code.

* Deepen your knowledge of programming algorithms and keep practicing. A great programmer must possess exellent mathematical and logical thinking abilities which are developed gradually with intensive practice. Use websites such as [LeetCode](https://leetcode.com/) and [CodeWars](https://www.codewars.com/) to challenge yourself and improve your solution by comparing with other programmers' solutions.

In this exercise, you will undertake several challenges to practice cleaning code and improving code efficiency. Remeber the tips we gave you above. In certain challenges you may want to google what the more efficient ways are to refactor the code.

## Getting Started

Complete the challenges in order in the `your-code` directory.

### Challenge 1-3

In these three challenges you will improve some poorly written Python codes. Reflect on what you have learned in the lesson about code simplicity and efficiency then revamp the codes. **Please use comments between the Python lines to explain why you refactor the code that way**.

Despite the poor practice in those Python codes, they are fully functional. To run the Python code in command line, navigate to the `your-code` directory containing the Python files, then execute (note we are using Python 3 interpreter instead of 2):

```python
python3
>>> exec(open("challenge-1.py").read())
```

**After refactoring the code you should test your solution to make sure it is still working as expected.**

### Bonus Challenge

In this challenge, you will focus on improving the code efficiency only. The code is a Python class that solves the following puzzle programmatically:

> **You are climbing a stair case. It takes N steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?**

For instance, if the stair has 4 steps, there are 5 ways to climb to the top:

1. 1, 1, 1, 1
1. 1, 2, 1
1. 1, 1, 2
1. 2, 1, 1
1. 2, 2

If you execute `bonus.py` in command line you'll find it can give the correct answer. Read the code carefully and make sure you understand how it calculates the correct answer. However, the solution is extremely inefficient (e.g. try input `10000` and you'll be stuck forever) because it uses a *brute force* solution that performs massive redundant computations. Your goal in this challenge is to make the code more efficient. 

Your solution is considered *ideal* if it performs less than 10,000 calculations for a stair with 10,000 steps. But any minor improvement of the algorithm is congratulatable because Rome can't be built in a day.

:information_source: You are encouraged to google the Internet to solve this challenge.

## Deliverables

* `challenge-1.py`, `challenge-2.py`, `challenge-3.py`, and optionally `bonus.py` that contain your refactored code.

* Make sure you explain your solutions in the deliverables.

## Submission

* Add the deliverables to git
* Commit your code
* Push to your fork
* Create a pull request to the class repo
