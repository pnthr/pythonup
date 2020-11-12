# The `not` Operator

- We mentioned the not operator as part of the logical operators last week, but did not talk about it. Did anyone read it up?
- The NOT operator in Boolean algebra returns True when the expression is False and vice versa.
  ```python
  print(not 6 > 8)
  print(not 6 <= 8)
  ```
- Under the comparison operators we missed the not equal (!=) operator.
  ```python
  print(5 != 7)
  ```

# Brief Review of String Operators

- Just like we learned last week, on a high level, python strings are characters constrained by single, double, or triple quotes.

## String Operators

- The `+`,
- The `*`,
- The `in`, and
- The `not in` operators

## Basic Operators

### The `+` Operator: Concatenation

- Similar to the arithmetic addition operator, it is used to combine multiple strings

  ```python
  fav_food = 'plantain'
  our_long_string = 'Today is a good day to eat' + fav_food  + ' because it is my birthday'
  ```

- You cannot combine a string and an integer using this operator.
  ```python
  print( 1 + "sorry")
  ```

### The `*` Operator: Replication

- It carries out two operations -> makes 'n' number of a given string, where n is the number of duplication we want, and then concatenates them.
- The syntax is `string * n`.
- Just like in basic maths, the `*` operator is commutative that means `n * string == string* n`
- `n` has to be an integer, negative values of `n` would yield an empty string.

## Membership Operators

### The `in` Operator

- The `in` operator returns True if a character or a substring exists in a given string and returns False otherwise.
  ```python
  print('elf' in 'elephant')
  print('ant' in 'elephant')
  print('t' in 'elephant')
  ```
- Did Judith notice James' suit?
  ```python
  judith_speech = "a very long speech about the weather, covid and James' suit"
  print('James' in judith_speech)
  print('James )
  ```

### The `not in` Operator

- This returns False if a character or substring exists in a given string and True otherwise.
  ```python
  print('elf' not in 'elephant')
  print('ant' not in 'elephant')
  print('t' not in 'elephant')
  ```

## Comparison Operators in Strings

- Who can remind us what comparison operators are? Someone give two examples of comparison operators.
- String comparison is done between Unicode values of the string characters.
  | Characters | Ordinal value |
  | - | - |
  |'A' - 'Z' | 65 to 90 |
  |'a' to 'z' | 97 to 122 |
- To get the ordinal value of a string you use the python method ord(), it's opposite is chr().
- So when you do "a" == "a", the computer checks 97 == 97 which is true.
- Application is in sorting names
- String comparison is case sensitive

---

# Functions

- A function is a sequence of repeatable instructions to carry out a specific task or related tasks, coupled together as a unit.
- They are sometimes called methods in python.
- You have already used a couple of functions... the most popular one is the `print` function.
- To use a function, you write the name of the function followed by arguments inside a parenthesis.
  ```python
  print('somethin', 56)
  ```
- You can also define your own function, this is important because it helps you reuse your code. For example, imagine writing a program that greets visitors to your store.
  ```python
  visitor = 'James'
  print(f"Hello {visitor} Welcome to the world's best coffee store")
  ```
- If you need to greet some other visitor somewhere else in your code, you have to rewrite the entire greet sequence again. Using functions, however, you can define a `greet` function to call whenever you need to greet someone.
- The act of using a function is called "calling", so to create a function, you define it while to use it, you "call" it. So you have the power to call or summon functions to do your bidding.
- So let's define a function that we can reuse to welcome visitors to our store.

### Structure of a Function

- You need the keyword `def` to define a function, and these are the other parts (show png 1).
- Just like in Maths, a function is like f(x) [show png2].
- If you run this function definition, nothing happens. You have to call it.

### Function Output and Side Effects

- Say we don't want to print the result from a function, but use it somewhere else in our code, how do we do that? we use a return statement.
- It tells the computer that our program has ended and it should send back the value of whatever we put after it(return).
- A return statement marks the end of a function, and the function exits.
- Effects that are observable outside the function, except the return of a value, are called side effects.

### Named Arguments (or keyword or Optional Parameters) and Positional Arguments

- When an argument is required and a default value is not provided in the function definition, it is called a positional argument.
- When an argument is instantiated with a default value in the function, it is a named argument or an optional parameter.
