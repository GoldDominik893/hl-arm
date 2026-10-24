# copyright of Dominic Wajda, refer to the LICENSE file for details
# this file contains the workings for the lexer part of the HLARM compiler

hlarmvar = input("enter the path to your hlarm program: ")
hlarmfile = open(hlarmvar, "r")
hlarmvar = hlarmfile.read()
hlarmfile.close()


# removing comments

nocommentshlarmvar = ""

nocommentshlarmarray = hlarmvar.splitlines()
linescount = len(nocommentshlarmarray)


for i in range(linescount):
    nocommentshlarmarray[i] = nocommentshlarmarray[i].split('//')[0]

print("hlarm program without comments: ")
for i in range(linescount):
    nocommentshlarmvar = nocommentshlarmvar + nocommentshlarmarray[i] + "\n"

print(nocommentshlarmvar)

# creating tokens

tokentable = []
thereisstilltokens = True
currenttoken = 0
currentposition = 0
temp_variablename = ""

while thereisstilltokens:
    print("there are still tokens to be found")

## searching for a variable declaration

    currentchar = nocommentshlarmvar[currentposition]

    if currentchar == "$":
        tokentable.append({
            "type": "VARIABLE"
        })
        
        currentposition = currentposition + 1
        currentchar = nocommentshlarmvar[currentposition]
        
        while currentchar != " ":
            temp_variablename = temp_variablename + currentchar
            currentposition = currentposition + 1
            
        tokentable[currenttoken] = {
            "value": temp_variablename
        }
        currenttoken = currenttoken + 1

    if len(nocommentshlarmvar) == currentposition:
        thereisstilltokens = False
        
print(tokentable)