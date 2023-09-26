



#We should create a program to calculate if there is still a ticket 
# for the game tonight. We are given two variables: Capacity of the stadium 
#and the amount of tickets sold. 
# Print True if I can still buy a ticket, False otherwise.


stadium_capacity = int(input("Enter the capacity of the stadium:"))

sold_tickets = int(input("Enter amount of tickets sold:"))


is_there_space = stadium_capacity > sold_tickets 

print("There is space for the game tonight;", is_there_space)



