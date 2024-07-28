def addElem(setin, elem):
    if(elem not in setin):
        setin.add(elem)
        return setin
    else:
        print("element already present") 

def removeElem(setin, elem):
    if(elem in setin):
        setin.remove(elem)
        return setin
    else:
        print("element not present in the set")

def unionSet(set1,set2):
    return set1.union(set2)

def intersectionSet(set1,set2):
    return set1.intersection(set2)

def diffSet(set1,set2):
    return set1-set2

def checkSubset(set1,set2):
    return set1.issubset(set2)

def calcLength(setin):
    count = 0 
    for i in setin:
        count+=1
    return count

def  symmetricDifference(set1,set2):
    return (set1-set2).union(set2-set1)

def powerSet(setin):
    # Convert the input set to a list to maintain consistent indexing
    setin = list(setin)
    power = {frozenset()}  # Initialize the power set with the empty set

    for elem in setin:
        new_subsets = []
        for subset in power:
            new_subset = frozenset(subset.union({elem}))
            new_subsets.append(new_subset)
        power.update(new_subsets)
    
    return power

def getAllSubsets(setin):
    power = powerSet(setin)
    result = []
    for i in power:
        result.append(set(i))
    return result