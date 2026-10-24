# copyright of Dominic Wajda, refer to the LICENSE file for details
# this file contains the workings for the lexer part of the HLARM compiler

hlarmvar = input("enter the path to your hlarm program: ")
hlarmfile = open(hlarmvar, "r")
hlarmvar = hlarmfile.read()
hlarmfile.close()


# removing comments

nocommentshlarmarray = hlarmvar.splitlines()
linescount = len(nocommentshlarmarray)


for i in range(linescount):
    nocommentshlarmarray[i] = nocommentshlarmarray[i].split('//')[0]

print("hlarm program without comments: ")
for i in range(linescount):
    print(nocommentshlarmarray[i])
