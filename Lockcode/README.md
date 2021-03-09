# LOCKCODE - WRITEUP

Download and extract the file

Check the file

![I](pics/1.png)

Lets check it with "checksec"

![I](pics/2,png)

So there is nothing in stack that we can do

We have to play with the program in this situation

Lets check the program how it works

![I](pics/3.png)

We can clearly say that it takes only one argument

But we dont know what this program does with that argument

So lets decompile the binary in Ghidra

We can see there are three functions

main(),res(),val()

![I](pics/4.png)

![I](pics/5.png)

![I](pics/6.png)

Now after analyzing the val() it justs comapres the value of the input same as the string defined in the program

res(),justs prints the statement

Now lets decode the string which is stored as hex

![I](pics/7.png)

Passing the string as input

![I](pics/8.png)

We cracked the binary


