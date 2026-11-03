# copyright of Dominic Wajda, refer to the LICENSE file for details
# this file contains the workings for the parser part of the HLARM compiler

import ast

hlarmtokvar = input("enter the path to your hlarm tokens file: ")
hlarmtokfile = open(hlarmtokvar, "r")
hlarmtokvar = hlarmtokfile.read()
hlarmtokfile.close()


## searching for any variables in the code, assigning appropriate memory locations

hlarmtokarray = ast.literal_eval(hlarmtokvar)
completedvarsarray = []
currentmempos = 0
currentvarpos = 0

for currentpos in range(len(hlarmtokarray)):
    if hlarmtokarray[currentpos]['type'] == "VARIABLE":
        varname = hlarmtokarray[currentpos]["value"]
        
        
        if not any(var["name"] == varname for var in completedvarsarray): #### i had no idea how to search for a value in a dict, i used ai for this
            currentvarpos = currentvarpos + 1
            completedvarsarray.append({
                "name": varname,
                "mempos": currentmempos
                })
            print(varname, " assigned to memory location", currentmempos)
            currentmempos = currentvarpos * 16
        
