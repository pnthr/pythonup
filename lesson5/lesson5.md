# More Loops

## For Loop

> The drawback to a for loop is that it should run for a predetermined number of iterations, a while loop on the other hand runs continuously until a condition no longer holds.

```python
for x in range(20):
  print(x)

for x in range(4,8):
  print(x)
```

The "range" here provides us with an indexing system. If one number is provided it starts from zero until 1 less the number, if two, it covers from the first number until 1 less the second, and if 3, the third number indicates the interval.

## Break and Continue Statements

**break** statement where present forces the loop to exit
**continue** makes the loop skip a block and move on to the next.

# Packages

Imagine if everyone had to write code for everything they had to do and there was no way to reuse someone else's code... the world would have very few software.

Packages are a way include extra functionality in our programs. Python has built-in methods associated with different object types. We have seen the `index` method which works on various data types like; strings and lists. We also saw the `append` function which works on lists.

But python is applied to many tasks in a wide range of industries, adding methods to solve every problem will make it too large and difficult to maintain. That is why we have packages. They focus on a subset of functionality and write modules which contain some niche methods.

Examples of packages in python include:

- Numpy [used for handly arrays]
- Matplotlib [used for data visualization]
- Pandas [Used data analysis]
- Scikit [Used for machine learning]

These are just a couple of packages, there are so many more out there.

To use a python package, you have to install them on your machine and import them into your code.
