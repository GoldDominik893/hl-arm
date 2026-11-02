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

        while currentchar != " " and currentchar != ")":
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


    ## searching for a comparison operator (!=)

    elif currentchar == "!" and nocommentshlarmvar[currentposition + 1] == "=":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "COMPARISON",
            "value": "!="
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 1


    ## searching for data types (str(), bool(), int())

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
        
        ### checking if the value has an operator in it, it will create a data start token and the variables and what not can be added to it
        if "+" in temp_datastring or "-" in temp_datastring or "*" in temp_datastring or "/" in temp_datastring or "%" in temp_datastring or "$" in temp_datastring:
            tokentable[currenttoken] = {
                "type": "START_DATA_STRING",
                "value": None
            }
            currentposition = currentposition - len(temp_datastring) - 4
            
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
        
        ### checking if the value has an operator in it, it will create a data start token and the variables and what not can be added to it
        if "+" in temp_databoolean or "-" in temp_databoolean or "*" in temp_databoolean or "/" in temp_databoolean or "%" in temp_databoolean or "$" in temp_databoolean:
            tokentable[currenttoken] = {
                "type": "START_DATA_BOOLEAN",
                "value": None
            }
            currentposition = currentposition - len(temp_databoolean) - 4
            
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
        
        ### checking if the value has an operator in it, it will create a data start token and the variables and what not can be added to it
        if "+" in temp_dataint or "-" in temp_dataint or "*" in temp_dataint or "/" in temp_dataint or "%" in temp_dataint or "$" in temp_dataint:
            tokentable[currenttoken] = {
                "type": "START_DATA_INTEGER",
                "value": None
            }
            currentposition = currentposition - len(temp_dataint) - 4

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
        
    ## searching for halt (halt())
    
    elif currentchar == "h" and nocommentshlarmvar[currentposition + 1] == "a" and nocommentshlarmvar[currentposition + 2] == "l" and nocommentshlarmvar[currentposition + 3] == "t" and nocommentshlarmvar[currentposition + 4] == "(" and nocommentshlarmvar[currentposition + 5] == ")":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "HALT",
            "value": "halt"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 6
        
    ## search for a built in function call (echo(), return(), input(), if(), loopif(), loop())

    elif currentchar == "e" and nocommentshlarmvar[currentposition + 1] == "c" and nocommentshlarmvar[currentposition + 2] == "h" and nocommentshlarmvar[currentposition + 3] == "o" and nocommentshlarmvar[currentposition + 4] == "(":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "FUNCTION_BASE",
            "value": "echo"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 5

    elif currentchar == "i" and nocommentshlarmvar[currentposition + 1] == "n" and nocommentshlarmvar[currentposition + 2] == "p" and nocommentshlarmvar[currentposition + 3] == "u" and nocommentshlarmvar[currentposition + 4] == "t" and nocommentshlarmvar[currentposition + 5] == "(":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "FUNCTION_BASE",
            "value": "input"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 6
    
    
    elif currentchar == "i" and nocommentshlarmvar[currentposition + 1] == "f" and nocommentshlarmvar[currentposition + 2] == "(":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "FUNCTION_BASE",
            "value": "if"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 3
    
    elif currentchar == "l" and nocommentshlarmvar[currentposition + 1] == "o" and nocommentshlarmvar[currentposition + 2] == "o" and nocommentshlarmvar[currentposition + 3] == "p" and nocommentshlarmvar[currentposition + 4] == "i" and nocommentshlarmvar[currentposition + 5] == "f" and nocommentshlarmvar[currentposition + 6] == "(":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "FUNCTION_BASE",
            "value": "loopif"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 7
    
    elif currentchar == "l" and nocommentshlarmvar[currentposition + 1] == "o" and nocommentshlarmvar[currentposition + 2] == "o" and nocommentshlarmvar[currentposition + 3] == "p" and nocommentshlarmvar[currentposition + 4] == "(":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "FUNCTION_BASE",
            "value": "loop"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 5
    
    elif currentchar == "r" and nocommentshlarmvar[currentposition + 1] == "e" and nocommentshlarmvar[currentposition + 2] == "t" and nocommentshlarmvar[currentposition + 3] == "u" and nocommentshlarmvar[currentposition + 4] == "r" and nocommentshlarmvar[currentposition + 5] == "n" and nocommentshlarmvar[currentposition + 6] == "(":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "FUNCTION_BASE",
            "value": "return"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 7
    
    
    ## searching for opening and closing of code definitions ({, })
    
    elif currentchar == "{":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "CODE_OPEN",
            "value": "{"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 1
        
    elif currentchar == "}":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "CODE_CLOSE",
            "value": "}"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 1
    
    
    ## searching for an arithmetic operator (+, -, *, /, %)
    
    elif currentchar == "+":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "ARITHMETIC",
            "value": "+"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 1

    elif currentchar == "-":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "ARITHMETIC",
            "value": "-"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 1

    elif currentchar == "*":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "ARITHMETIC",
            "value": "*"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 1

    elif currentchar == "/":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "ARITHMETIC",
            "value": "/"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 1

    elif currentchar == "%":
        tokentable.append({})

        tokentable[currenttoken] = {
            "type": "ARITHMETIC",
            "value": "%"
        }
        currenttoken = currenttoken + 1
        currentposition = currentposition + 1


    else:
        currentposition = currentposition + 1

    if len(nocommentshlarmvar) == currentposition:
        thereisstilltokens = False

print(*tokentable, sep="\n")
