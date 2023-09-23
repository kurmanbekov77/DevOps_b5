



# A DevOps team needs to perform 
# a system update on 212 servers. However, 
# they can only update 8 servers per day due to 
# resource restrictions.
# They want to find out how many full 
# days it will take to complete the updates
# and if there will be servers left over on
# the end of final full day.


#My example below


num_of_servers, num_servers_per_day = 212, 8


print(num_of_servers//num_servers_per_day,"days it will take to complete the updates")

print(num_of_servers % num_servers_per_day, "will be left over on the end of final full day. ")


#Teachers example


servers,daily_updated_servers = 212, 8

full_day = servers // daily_updated_servers
print("They will be doing updates for",full_day,"full days.")

outdated_servers = servers % daily_updated_servers

print("We will have",outdated_servers,"outdated servers at the end.")











```
















