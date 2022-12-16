#import sympy

#expres=input("Enter an expression: ")
expres="-(a*x*x+b*x+c)/2.65"
symblist= ['+', "-", "*", "/", "^", "(", ")", "!", ";", ",", ]
expreslist=[]
states=["def", "num", "float", "ident", "floatexp", ]

buf=""
state="def"
i=0
#transform expression into list
#chek every part of the list if it belongs to numeral, variable or whatever
for char in expres:
    i=i+1

    if char in symblist:
        if state=="def":
            expreslist.append(char)
        else:
            expreslist.append(buf)
            expreslist.append(char)
            state="def"
            buf=""
        
    elif char.isdigit()==True and i<len(expres):
        if state=="def":
            buf=buf+char
            state="num"
        else:
            buf=buf+char
    elif char.isdigit()==True and i==len(expres):
        buf=buf+char
        expreslist.append(buf) 
    
    elif char==".":
        if state in states[:2] and i<len(expres):
            buf=buf+char
            state="float"
        elif state in states[:2] and i==len(expres):
            buf=buf+char
            expreslist.append(buf)
        else:
            print("You can not use . in identifyers or use it more than once in numbers")
            break

    elif char in [" ","    ", ]:
        if state=="def":
            continue
        else:
            expreslist.append(buf)
            state="def"
            buf=""

    elif char in ["e", "E"] and i<len(expres):
        if state=="def":
            buf=buf+char
            state="ident"
        elif state=="num":
            buf=buf+char
            state="float"
        elif state=="float":
            buf=buf+char
            state="floatexp"
        elif state=="ident":
            buf=buf+char
        elif state=="floatexp":
            print ("You are not allowed to use e/E twice in the number")
            break
    elif char in ["e", "E"] and i==len(expres):
        if state=="floatexp":
            print ("You are not allowed to use e/E twice in the number")
            break
        else:
            buf=buf+char
            expreslist.append(buf)

    elif char.isalpha()==True or char=="_":
        if state=="def" or state=="ident":
            buf=buf+char
            state="ident"
            if i==len(expres):
                expreslist.append(buf)    
        else:
            print ("Letters except e/E are not allowed after numbers")
            break

print(expreslist)
        