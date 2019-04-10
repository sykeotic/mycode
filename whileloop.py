leave = 'get your ass outta here!'

mylist = []

print("Welcome to the never ending loop!")

while leave.lower() != 'quit':

    switch = {}
    userip = input("what is the ip address? ")
    switch["ip"] = userip    ## we add the key {"ip":userip}

    userven = input("What is the vendor associated with the IP? ")
    switch["vendor"] = userven

    biglist.append(switch)

    leave = input("The only way to exit is to quit")

print("That is the end of the program!")
print("On your list is", biglist)
