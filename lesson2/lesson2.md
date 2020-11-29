# Control Flow

The program flow is the order in which instructions are carried out, and a control flow coordinates this order.

> Look at the defined function, who can tell us how it will run? what happens first and what follows?

- Show `control_flow_1`
- This function is an example of the default program flow, when a function is run, it goes from top to bottom evaluating each line.
- What happens if we want to change this order? say modify our greet function to welcome people with their titles, i.e. if the visitor is male, add a "Herr." or if female "Frau".

The question leads us to our first control flow structure

## Conditional

### if/elif/else Control Structure

- Show `control_flow_2`
- The if/else statement helps direct the flow of the program using results from expressions that yield a boolean. Such as Logic or Comparison operations.
- Remember blocks are delimited by indentation!!!
- In the image shown above, the choice between yes and no can be made with an if/else control structure.

#### nested if/else statements

- When there are more than two possibilities you could use nested if/else statements.
- Show `control_flow_3`

#### elif

- "elif" is short for `else if` and it is used instead of writing nested if/else statements.

> So we've seen two ways to achieve the same thing, we could use nested if/else statements or incorporate an elif statement, and this is common in programming, there are usually many ways to accomplish the same thing.

## Loops

> An instruction in a computer program which runs endlessly until a condition is met, is a loop

### While Loops

- A while loop instructs the computer to keep running a program **while** a condition remains true, and end it once it becomes false.
- Show `control_flow_4`
