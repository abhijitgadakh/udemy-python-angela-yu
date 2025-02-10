# Question 1: Which version of code will produce an Indentation Error?

    # Version 1
    # def my_function():
    # ••print("Hello")  # Correct indentation with 2 spaces (may vary depending on context)

    # Version 2
    # def my_function():
    # print("Hello")  # Indentation Error: No indentation for the print statement inside the function

    # Version 3
    # def my_function():
    # ••••print("Hello")  # Correct indentation with 4 spaces

    # Version 4
    # def my_function():
    # ••print("Hello")  # Correct indentation
    # print("Bye")      # Indentation Error: Inconsistent indentation, "print('Bye')" not inside function

# Answer: Version 2 will produce an Indentation Error

################################################################

# Question 2: Which version of code will output "This will run"?

    # Version 1
    # # This is my program.
    # ••print("This will run")  # This will output "This will run"

    # Version 2
    # def my_function():
    # ••••print("This will run")  # Function defined but not called, nothing will be printed

    # Version 3
    # def my_function():
    # ••••print("This will run")
    # ••my_function()             # Indentation Error: Incorrect indentation for function call

    # Version 4
    # def my_function():
    # ••••print("This will run")
    # my_function()               # Correct code, "This will run" will be printed

    # Answer: Version 1 and Version 4 will output "This will run"

################################################################

# Question 3: In which version of code will you see "This will run" printed?

    # Version 1
    # def my_function():
    # ••••a = 3
    # ••••if a > 2:
    # ••••print("This will run")  # Indentation Error: print not properly indented inside if block
    # my_function()

    # Version 2
    # def my_function():
    # a = 3
    # ••••if a > 2:
    # ••••••••print("This will run")  # Indentation Error: Incorrect indentation of if block
    # my_function()

    # Version 3
    # def my_function():
    # ••••a = 3
    # ••••if a > 2:
    # ••••••••print("This will run")  # Correct code, but function is called inside itself causing RecursionError
    # ••••my_function()

    # Version 4
    # def my_function():
    # ••••a = 3
    # ••••if a > 2:
    # ••••••••print("This will run")  # Correct code, "This will run" will be printed
    # my_function()

    # Answer: Version 4 will correctly print "This will run"
