
# ASSIGN TWO VARIABLES NAMED "first_name" AND "last_name".
first_name = "ada"
last_name= "lovelace"

#USE "first_name" AND "last_name" TO PRINT THE "full_name".
full_name=f"{first_name} {last_name}"

#PRINT "Hello, Ada Lovelace"
print("Hello "+full_name.title())

#PRINT USING f-string INSIDE PRINT STATEMENT.
print(f"Hello {full_name.title()}!")

#.format METHOD
full_name = "{} {}".format(first_name, last_name)
print(full_name)

#ADDING WHITESPACES, USE \t.
print("\tPython")

# USE "\n" FOR NEW LINE.
print("Python\nJava\nC++\nJavaScript")

#USE "\n\t" FOR NEW LINES AND NEW TABS.
print("Languages\n\tKotlin\n\tC\n\tPHP\n\tC#")

#RIGHT STRIPPING WHITESPACES
name = "Python "
print(name+" ",len(name))
#Removing Whitespaces
name = name.rstrip()
print(name+" ",len(name))



favourite_language = " Python"
print(favourite_language+" ",len(favourite_language))
print(favourite_language.lstrip() + " ",len(favourite_language.lstrip()))



# 3 STRIP FROM BOTH THE SIDES.
favourite_language = " PYHTON "
print(favourite_language+" ",len(favourite_language))
print(favourite_language.strip()+" ",len(favourite_language.strip()))


#YOU CAN ALWAYS USE "strip" IF YOU HAVE WHITESPACES AT JUST ONE SIDE AND YOU WANT TO REMOVE IT.