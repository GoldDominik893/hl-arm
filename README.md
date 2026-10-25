# hl-arm

my new project, I want to build a compiler to convert high level code into 64 bit arm assembly code, merely for fun

The name is pronounced, H-L-Arm, not hlarm.

## definitions

The new complier will have its own language, the repository houses both the language definitions and the compiler for it.

Since I have been working with mainly PHP and Python for the past 6 or so years, I want the syntax to be very similar so that it's easy to understand.

Below I have listed the planned syntax that will be used for the language.

variables: $variablename
array: $arrayname[numberofpositions]

arrays start at: 0

setting a variable or array position: =

comparison of values: ==, !=, >, <, >=. <=

basic arithmetic operations: a*b, a-b, a+b, a/b

defining of strings or other data types anywhere in the program: str(), boo(), int(),

the outputs will be: echo(), return().

an input will be: input(), however a data type must always be set.

basic arithmetic operations can be used anywhere in the program for example in the defining of a variable or in a branch,

indentation does NOT matter.

the end of an instruction must be closed off with a ; rather than a new line like in other languages(python).

in any operation which performs some sort of action like a function or a branch will start with { and end with }

comments: start with // and end with a new line

loops: loop(), loopif()

halt() ends the execution of the program, similar to the php exit() command.

## progress

I am currently building the lexer part of the compiler.

in my testing, i am using the /tests/ folder, the versioning i am using is where the first number dictates the version of the code, the second number dictates the generation attempt by the program. For example "testprogram1.1.hlarmtok", means program 1, 1st attempt of generating tokens, testprogram1.1.s means program 1, 1st attempt of converting into arm assembly code.