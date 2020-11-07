## What is Programming

- Programming is communicating with computers through a set of instructions so that they can carry out tasks without errors.

- An analogy is writing a recipe and passing on to someone to use in preparing a meal. The code you write is like a recipe for the computer to produce an outcome, which could be computing a value, or identifying an object from a group.

- Coding is the act of writing a set of instructions for a computer to carry out.

- Why is programming great? it's because humans are not cut out for boring repetitive tasks. If you have to wash 50 cars, the first 10 may be clean but after a while your concentration reduces and you are no longer as efficient. But once you have an instruction well written a computer can carry out that task over and over again without any loss in precision.

| Humans                                                | Computers              |
| ----------------------------------------------------- | ---------------------- |
| Get bored                                             | Don't get bored        |
| Creative - humans can creatively pick clothes to wear | Not creative           |
| Detect patterns                                       | Computation            |
| Infer information                                     | Garbage in garbage out |

## Variables

- Variables are simply a way to store values and reuse them.
- We give them names so it's easy for us to remember and reference in our code.
- Imagine if there are no variables, and you write a long piece of code, whenever a value changes you have to go to all the places it is referenced to change it manually.

```python
  a = 5
  print(5 + 6)
  print(5 + 7)
  print(5 + 8)

  print(a + 6)
  print(a + 7)
  print(a + 8)

```

- You can equate a variable to another variable
  ```python
  a = 5
  b = a
  print (a, b)
  ```

#### Example

It's election season in the US now, so let's write a small program that takes the population of a state, the number of votes a candidate obtained and tells us the percentage he has.

```python
population = 2000000
votes_for = 1600000
percentage_for = votes_for * 100 / population
```

- In the future, we will look at functions, and how we can make our little program above run in a function to further simplify the process.

#### Classwork

So what will these print out:

```python
a = 4
b = 3
print (a + b + a)

a = 2
b = 2

temp = a
a = b
b = temp

print(b)

```

## DataTypes

- Datatypes represent the properties that a value can possess.
- They detail the characteristics computers can use to distinguish various inputs.
- Most programming languages have similar primitive data types which are: `Numbers (Integers), Strings and Booleans`
- ```python
    # Numbers
    numb = 1, 3, 5

    # Strings
    strings = "name", "Lagos", "This is could be a paragraph", "345"

    # Boolean
    bools = True, False
  ```

  > Do Kaggle Classwork

## Operators

- Different data types also have different operators that can be used on them.
- Operators here could include addition, subtraction, length, etc.
- Operators do not work for every data type. E.g. You can square a number, but squaring a string does not make sense.
- Also you cannot do these operations of different data types, e.g. you cannot subtract `"hello"` from `300`

### Arithmetic Operators

> Usually used on Number data types

- **Addition**
- **Division**
- **Subtraction**
- **Multiplication**
- **Modulo:** Returns the remainder from the division of two values, it's like the opposite of the division operator, because in the division operator you get the quotient, while in the modulo you get the remainder.

#### Classwork

Give an example of scenarios where the modulo operator could be useful?

```python
score = 57
if score % 2 == 0:
    print(f'your score, {score} is an even number')
else:
    print(f'your score, {score} is an odd number')
```

### Comparison Operators

- **Less than**
- **Greater than**
- **Equal**
- **Less or Equal**
- **Greater or Equal**

> Comparison operators return Booleans, so either True or False

```python
#Less than
6 < 3

#Greater than
3 > 6

#Equal**
2 == 2

#Less or Equal
3 <= 4

#Greater or Equal
5>= 2

```

- Comparison operators work for strings also, they compare the Unicode values of individual characters in the string.

```python
print("Jame" == "James")
```

### Logic Operators

> Used usually for expressions that yield boolean values

- **AND**
- **OR**
- **NOT**

- These logic operators are very important because they instruct the computer on how to make decisions. So you can write a statement that says if age is greater than 21 and money is equal or greater than cost, print `you can have whiskey`.

#### Example

```python
name = 'John'
age = 22
money = 6
cost = 9
if age > 21 and money > cost:
    print(f'you can have whiskey and your change is {money - cost}')
if age < 21 or money < cost:
    print(f'you cannot have whiskey')
    if money > cost:
        print('because you are underage')
    else:
        print('because you do not have enough money')
```

#### Classwork

What would these expressions print?

```python
gender1 = "male"
profession1 = "lawyer"
gender2 = "female"
profession2 = "astronaut"
if gender == "male" or gender == "female":
  print("we have a living organism")
```

### String Operations

> As we said earlier, not all operators work on every data type. There are special operators for the string type and we will look at a few now.

#### Concatenation (Addition)

- Also called string addition, it's a way to combine multiple strings into one.

  ```python
  print('hallo' + " zusammen!")
  print('his age is ' + 34) # will this work?

  ```

- So it's called a "string" because technically it's just a string of characters.
- And what defines a string in python? Being enclosed in double or single quotes.

#### To string conversion

`print(str(4))`

#### ClassWork

```python
print(a+str(b) == 54) #what do we get?

```

### MISC

```python
  # Figure out what type it is
  print(type(45, "I am a string"))
```

> If you need to learn more string functionalities, go online, search things and learn by yourself.
