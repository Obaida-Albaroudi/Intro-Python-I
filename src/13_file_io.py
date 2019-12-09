"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
def foo():
    text_file=open("foo.txt", "r")
    info = text_file.read()
    print(info)
    text_file.close()
# YOUR CODE HERE

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
def bar():
    text_file=open("bar.txt", "w")
    text_file.write("Wow Line one\n")
    text_file.write("Wow Line two\n")
    text_file.write("Wow Line three")
    text_file.close()

foo()
bar()