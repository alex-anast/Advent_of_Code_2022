# WHY SO MANY FAILURES


## Version 3

Supposedly, this code should work. My solution was based on dictionaries, which would help me practice a lot with how to access dictionaries inside a dictionary etc in Python.

The solution wasn't correct and I couldn't figure out why.

## Version 4

After having spent so much time on this problem already, my frustration grew fonder and fonder.
That's why I decided to re-write my solution, but this time:

1. In the simplest method possible.
2. Everything has to be structured, implementing everything with functions.
3. Test oriented. Everything should be printable and asserted.

Quickly I realised that the element I was missing is the depth of the directory.
i.e.:
For a given dir, named "foo",
if I access ALL the directories,
this can be NOT unique,
since it can be two different directories of the same name but under different PARENT directories.

## Version 5

For the reasons above, a kind of depth element has to be included in the solution.

Two approaches:

1. Insert an extra element in the dictionaries of Version 3.
2. Use OOP.

Let's remember Python's commandment by [Zen_of_Python]("https://en.wikipedia.org/wiki/Zen_of_Python"):

1. Complex is better than complicated
2. Readibility counts
3. If the implementation is hard to explain, it's a bad idea.

...let's use OOP!