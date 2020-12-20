# Modules, Packages and Basic DataViz

When you start writing complex programs, your code would be made up of lots of functions, and to make it readable and easily manageable, it's best to split them into logical sections - these sections would have their python files which could be imported and called upon wherever you need them. These python files are called modules

## Let's create a Module

- As long as files are in the same directory, you can import them directly as modules into your project.
- You can import a single function from your module, import them by name.

## Let's Create a Package

> A package can have sub-packages and or modules in it.

- Create a folder and add the `__init__.py` file, this tells python to treat your folder as a package.
- You can create subfolders with each one having an `init` file.

## Importing external packages

- First, ensure the package is installed in the environment you are working in.
- Importing a package is simply done with the `import` keyword.
- You can rename your imports with the `as` keyword to make using them easier for you.

## Pandas

- It's a package used for data analysis, it provides a suite of modules to help you quicky make meaning of large and or complicated data sets.

### Series

- To create a series pass panda a list of values

### Dataframes

- You can pass in a dictionary and create a Dataframe out of it.
