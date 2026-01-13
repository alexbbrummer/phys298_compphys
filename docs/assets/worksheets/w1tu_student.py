#### - Introduction to Python - Week 1 Tuesday ####

# In this day we will discuss the format of the workshop, Spyder, IPython, and Python, assignment and variables, mathematical operations, reassignment, floats and integers, object types and coercion, text (strings), lists, dictionaries, numpy arrays, simple indexing, and simple functions.


# Our weeks will be broken up into the two days of Tuesday and Thursday.  In Tuesday, we are introduced to different aspects of Python, programming, and computational physics.  In this first portion you are reading instructions from the .py files (or from what the instructor says aloud) and typing code along with the instructor.  In the second portion on THursdays, you will work on implementing the techniques introduced, but with slight variations and extensions on the goals and or methods.  After each day has finished, I will posted online copies of the tutorials with my own code written into the blanks.  But, don't let that demotivate you from typing anything.  Most of programming is troubleshooting, so I encourage you to type along, and we will address any questions and errors as they arise.  My own coding results in errors every single day, it is a natural part of programming.


# So, what is Spyder and how does it communicate with Python?  The Spyder Integrated Development Environment (IDE) is a computer program that has both IPython and a text editor.  You are reading from the text editor.  
# IPython is an interpreter for Python.  It is a computer application that allows you to execute Python commands and programs.  
# Python itself is a programming language.  It is the language that you write computer programs in.  
# You can think of Python as the grammer and style with which you write code, IPython then reads, interprets, and executes the code (hence being called an interpreter), and Spyder is software that allows to do all of these things at once in a structured environment.
# Within Spyder, we have the text editor (the window in which you are currently reading text) the variable/file expolorer and help menu on the upper right, and the IPython console in the bottom right.
# We can execute code both in the console directly, or by running chunks of code (cells) from the text editor file, or even the entire text editor file itself.  Spyder does not run code line by line.


#%% '#%%' Defines a cell.  With each cell we can write a block of code that can be executed independently of the other cells using hot keys (or by clicking on the right pointing green arror button).  This gives us a natural way to set up a tutorial, where every block of code that we want to run is entered into a separate cell.  This may seem arduous at first (it is not how Python is inteded to be run), but hopefully it will pay off by providing the tactile experience of programming.  As we learn more we will transition to more standard uses of Python (scripting), and will also experiment with something called Jupyter (essentially a web-based version of Spyder).

# Separately, a single pound symbol will define a 'comment', or 'commented code'.  This is code that the interpreter will not read, and hence will not be executed, allowing you to narrate and describe what you code does.  It is very important that you develop a healthy habbit of ALWAYS COMMENTING YOUR CODE.  We do this so that when sharing our code with others, they can quickly understand what the code does.

#%% To 'execute' a cell in Spyder, press Ctrl+Enter.  Try it in this cell.  Nothing should happen because this cell is commented.  To execute a cell and advance to the next cell, press Shift+Enter

#%% Excellent.  Now we will execute our first line of actual Python code.  Execute this cell of code, which contains the following 'print()' function, and the argument 'hello world'.



#%% In the console you should see the input to 'print('hello world')', and the output 'hello world'.




#%% ------ ASSIGNMENT OF SIMPLE VARIABLES ------
# The basic variables that are common across many languages are strings, integers, floats, and booleans.  Strings are collections of letters, numbers, and punctuation.  Integers are the numerical integers (including positives and negatives).  Floats are integers with decimal values.  Booleans are the values 'True' or 'False'.  The use of 'True' and 'False' in programming is fundamental.  Other variable types do exist, and we will explore them, but they are particular to Python, where as those we have just mentioned are common to all interpreted languages (e.g. R and Matlab).

#%% Assign the string "this our 1^st string" to the variable named "sometext"



#%% Now tell Python to print the value of the variable "sometext" using the print() function.



#%% Assign the integer 42 to the variable name "someinteger"



#%% Now tell Python to print the value of the variable "someinteger"



#%% Now tell Python to print the values of both of the variables "sometext" and "someinteger".  Hint: this can be done in more than one way.



#%% Notice that if you type only the names of variables, and that is the final piece of code in a cell, or script, or console entry, then the value of the final variable in that group will be displayed.


#%% Now assign the value of 'True' to the variable name "aboolean"



#%% Now tell Python to print the value of "aboolean".








#%% ------ MATHEMATICAL OPERATIONS ------
# Here we practice using different mathematical operations.  All of your favorite, basic operations are available in Python.  These are (with their respective commands): addition +, subtraction -, division /, multiplication *, exponentiation **, and the modulo operation (or remainder) %, and equality ==.  Let's try them all.

#%% Addition



#%% Subtraction


#%% Division


#%% Multiplication


#%% Exponentiation

#%% Remainder (modulor)


#%% Equality





#%% ------- REASSIGNMENT OF VARIABLES ------
# Here we demonstrate the idea of reassignment.  That is, assigning a value to an existing variable.  This may seem trivial, but it will prove to be an essential tool later.
# 







#%% ------ FLOATS AND INTEGERS ------
# Here we provide a few quick comments on differences between floats and integers.
# As mentioned before, integers are the counting numbers, can be positive and negative, and never have either decimals or commas.
# Floats on the other hand are expressed with decimals, or in scientific notation.  "Float" is short for floating point number, where the phrase "floating point" expresses the fact that some truncation error will exist depending on the bit-type of the float.  A throrough discussion of bit-types and "machine epsilon" (a fundamental quantity for numerical computing) is beyond the scope of this workshop.  In short, we'll say two things.  (1)  Even for computers, the number line is discrete and (2) At some point rounding will occur.  We can do two quick calculations to demonstrate these ideas.

# For point (1) tell Python to print the operations 1 + 1e-15 and 1 + 1e-16.  What do you expect the answers to be?  What are they really?  


#%% For point (2) tell Python to print the operations 1.200000*10**8 + 2.5000*10**(-7) and 1.200000*10**8 + 2.5000*10**(-8) and 1.200000*10**8 + 2.5000*10**(-9).  What do you expect the answers to be?  What are they really?







#%% ------ WORKING WITH NUMBERS, TYPES, AND COERCION ------
# Here we introduce a few functions that can be useful when working with collections of numbers.
# You may be interested in the maximum, minimum, and absolute values of numbers.  These functions exist in Python, and have sensible names.  For example, consider th collection of numbers 5, 7, 3, 5, 8, 2.  What would you guess is the name of the Python functionto find the maximum, or the minimum?

#%% Maximum


#%% Minimum


#%% Absolute value:  How about the absolute value of a negative number, like -10?

#%% Types:  We can also ask Python to tell us the type of number we are working with.

# Integer type

#%% Float type

#%% String type

#%% Coercion:  There can be instances where we need to "coerce" a type from what Python might first assume to what we actually want.  An example of this is that Python assumes the number 10 is an integer.  But maybe we need to treat 10 as a string (it could be part of a filename, directory, date, etc.).  To coerce a number to a string, we use the str() function.

# Try coercing the integer 10 into a string using the str() function.  How can you tell it worked?


#%% On the other hand, we may need to coerce a string into a float.  Try coercing the string '10' into a float using the float() function. How can you tell it worked?

#%% What about strings to integers?  


#%% Floats to integers?


#%% Letters and punctuation to floats or integers?



#%% ------ WORKING WITH TEXT ------
# You *will* still use strings in physics computing: filenames, labels, units, and metadata.
# But instead of spending a long time on "string math", we're going to pivot to the data
# structures you'll need immediately: lists, dictionaries, and arrays.

#%% Strings as labels
# Goal: make simple labels you can use in prints/plots later.


#%% f-strings (very convenient formatting)
# f-strings let you embed variables directly into a string.


#%% ------ LISTS: a small collection of things ------
# A list is an ordered collection. Today we won't focus on indexing (that's next week),
# but we *will* learn to create lists and combine them with built-in functions.

#%% A list of measurements (same physical quantity, repeated trials)



#%% A list can contain different types (but we usually avoid mixing for data!)



#%% ------ DICTIONARIES: a labeled collection ------
# A dictionary stores "key : value" pairs. Think: constants, settings, metadata.
# Today we won't iterate over dictionaries or do anything fancy—just create and access.

#%% Metadata for an "experiment"



#%% Dictionary access (by key)



#%% A constants dictionary (useful habit!)



#%% ------ ARRAYS: numerical collections (NumPy) ------
# For physics, we'll almost always use NumPy arrays for numerical data.
# Lists are great to *start*, but arrays make math fast and clean.



#%% Turn a list into a NumPy array



#%% Array "vectorized" math (no loops required)
# This is one of the biggest reasons we use NumPy.



#%% A safer version
# For now, just start t at 1 s so the demo is clean.



#%% --------INDEXING---------
# Sometimes we want to access individual (or collections) of elements inside a string, list, dictionary, array, etc.
# To do so, we use "indexing".  We say this already with the "key" we used in the dictionary.  For example, suppose you want to isolate the second entry from your "mixed" list, the value of 1.02.


#%%
# Print the second element of the mixed list.



#%% Note that I used the integer value of 1 to access the 2nd element.  This is because python is a so-called zero-indexed language, that is, indexing starts at "0".  Let's try indexing to access the third position in our numpy array x.


#%% ------- FUNCTIONS ------

# Like the functions that are inherent in Python, we can write our own functions to use multiple times for variable inputs.  The typical form of a function in python goes as follows.
    
#   def function_name(parameter1, parameter2):
#       enter
#       here
#       any
#       code
#       needed
#       and comments
#   return result_of_function

# For our first function, we will write a function that takes a parameter, and returns three times it the value of the parameter.
    



#%% Now let's run our function with different inputs.



#%% If we assign an instance of running the function to a variable name, then the output from the function is supressed, and assigned to that variable name.



#%% -------OUR FIRST BIG KID FUNCTION ------
# Today: a function that takes inputs and returns outputs.  We're going to end today with a short introduction to functions, and writing our very one function that calculates the gravitational force of attractions between two masses separated in three-dimensional space.

#%% Ostensibly, a function is still a variable, but only in that it also has a name assigned ot it.  However, here our variable (function) takes parameters as inputs and returns something new as an operation on those inputs.  Functions can do numerical operations (like those we know and love) but it can also do operational tasks, like loading/saving files, generating graphs, etc.  Importantly, when we write functions, we can define them within our working file, or we can write a wholly new .py file just for that individual (or collection) of functions.  Today we'll just write our function inside this larger tutorial.

#%% First, we're going to write a function to calculate the euclidean distance between two points.  It will take as arguments lists of coordinates for the two points, and return the euclidean distance.

#%% Euclidean distance between two points in 3D




#%%
# Try it:

    

#%% Now we'll caclulate the force of attraction, and we will do so using a function that calls on our previous one!


#%% Gravitational force magnitude between two point masses



#%%
# Example: two 1 kg masses separated by 1 m



#%% Congratulations on your completing your first day!
