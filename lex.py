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
temp_datastring = ""
temp_databoolean = ""
temp_dataint = ""

while thereisstilltokens:
    print("position: ", currentposition)


    currentchar = nocommentshlarmvar[currentposition]

    ## searching for a variable declaration ($)

    if currentchar == "$":
        tokentable.append({})

        currentposition = currentposition + 1
        currentchar = nocommentshlarmvar[currentposition]

        while currentchar != " ":
            temp_variablename = temp_variablename + currentchar
            currentposition = currentposition + 1
            currentchar = nocommentshlarmvar[currentposition]

        tokentable[currenttoken] = {
            "type": "VARIABLE",
            "value": temp_variablename
        }
        currenttoken = currenttoken + 1
        temp_variablename = ""



    ## searching for an assignment or comparison operator (= and ==)

    elif currentchar == "=":
        tokentable.append({})

        if nocommentshlarmvar[currentposition + 1] == "=":
            tokentable[currenttoken] = {
                "type": "COMPARISON",
                "value": "=="
            }

        tokentable[currenttoken] = {
            "type": "ASSIGNMENT",
            "value": "="
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 1

    ## searching for a comparison operator (>, >=)

    elif currentchar == ">":
        tokentable.append({})

        if nocommentshlarmvar[currentposition + 1] == "=":
            tokentable[currenttoken] = {
                "type": "COMPARISON",
                "value": ">="
            }

        tokentable[currenttoken] = {
            "type": "COMPARISON",
            "value": ">"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 1


    ## searching for a comparison operator (<, >=)

    elif currentchar == "<":
        tokentable.append({})

        if nocommentshlarmvar[currentposition + 1] == "=":
            tokentable[currenttoken] = {
                "type": "COMPARISON",
                "value": "<="
            }

        tokentable[currenttoken] = {
            "type": "COMPARISON",
            "value": "<"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 1

    elif currentchar == "!" and nocommentshlarmvar[currentposition + 1] == "=":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "COMPARISON",
            "value": "!="
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 1

    elif currentchar == "s" and nocommentshlarmvar[currentposition + 1] == "t" and nocommentshlarmvar[currentposition + 2] == "r" and nocommentshlarmvar[currentposition + 3] == "(":
        tokentable.append({})
        currentposition = currentposition + 4
        currentchar = nocommentshlarmvar[currentposition]
        

        while currentchar != ")":
            temp_datastring = temp_datastring + currentchar
            currentposition = currentposition + 1
            currentchar = nocommentshlarmvar[currentposition]

        tokentable[currenttoken] = {
            "type": "DATA_STRING",
            "value": temp_datastring
        }

        temp_datastring = ""
        currenttoken = currenttoken + 1
        currentposition = currentposition + 1

    elif currentchar == "b" and nocommentshlarmvar[currentposition + 1] == "o" and nocommentshlarmvar[currentposition + 2] == "o" and nocommentshlarmvar[currentposition + 3] == "(":
        tokentable.append({})
        currentposition = currentposition + 4
        currentchar = nocommentshlarmvar[currentposition]

        while currentchar != ")":
            temp_databoolean = temp_databoolean + currentchar
            currentposition = currentposition + 1
            currentchar = nocommentshlarmvar[currentposition]

        tokentable[currenttoken] = {
            "type": "DATA_BOOLEAN",
            "value": temp_databoolean
        }

        temp_databoolean = ""
        currenttoken = currenttoken + 1
        currentposition = currentposition + 1

    elif currentchar == "i" and nocommentshlarmvar[currentposition + 1] == "n" and nocommentshlarmvar[currentposition + 2] == "t" and nocommentshlarmvar[currentposition + 3] == "(":
        tokentable.append({})
        currentposition = currentposition + 4
        currentchar = nocommentshlarmvar[currentposition]

        while currentchar != ")":
            temp_dataint = temp_dataint + currentchar
            currentposition = currentposition + 1
            currentchar = nocommentshlarmvar[currentposition]

        tokentable[currenttoken] = {
            "type": "DATA_INTEGER",
            "value": temp_dataint
        }

        temp_dataint = ""
        currenttoken = currenttoken + 1
        currentposition = currentposition + 1
        
        
    ## searching for end of instruction (;)

    elif currentchar == ";":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "END",
            "value": ";"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 1



    else:
        currentposition = currentposition + 1

    if len(nocommentshlarmvar) == currentposition:
        thereisstilltokens = False

print(tokentable)
