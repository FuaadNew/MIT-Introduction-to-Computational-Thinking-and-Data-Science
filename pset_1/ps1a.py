###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import heapq

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cowDict = {}
    with open(filename) as file:
        for line in file:
            name,weight= line.split(",")
            weight = weight.strip()
            cowDict[name] = int(weight)
    
    return cowDict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # : Your code here

    cow_list = sorted((-weight, cow) for cow,weight in cows.items())
    used = set()
    res = []
    while len(used) != len(cows.values()):
        sublist = []
        subweight = 0
        for weight,cow in cow_list:
            weight = -weight
            if cow not in used and weight + subweight <= limit:
                used.add(cow)
                subweight+= weight
                sublist.append(cow)   
        res.append(sublist)
    print(res)
    return res

    




    #if a cow has not been picked up

    #find the first heaviest cow you can find that can be fit the weight limit that

    #add cow to visit set

    #if we're limited by size add this sublist to res

    #add this cow to the sublist and find the next heaviest cow


    #else find the next






    #if the cow can 


    

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    #: Your code here
    

    #for every partition 

    #do a brute force traversal where we make the list of trips 
    res = float('inf')
    def isvalidPartition(partitions):
        
        for partition in partitions:
            subweight = 0
            for cow in partition:
                subweight+=cows[cow]
            if subweight > limit:
                return False
        

        return True

    fewest_trips = float('inf')
    best_partition = []

    weightIsValid = False
    lenghFlag = False
    for partitions in get_partitions(cows.keys()):
        if isvalidPartition(partitions) and len(partitions) < fewest_trips:
            fewest_trips = len(partitions)
            best_partition = partitions


        
    
    return best_partition
    



    
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


if __name__ == "__main__":
    cows = load_cows('ps1_cow_data.txt')
   
    print(brute_force_cow_transport(cows,limit=10))
