array = [1,2,1,3,4,8]

def find_cycle(some_list):
    seen = {}
    for index in range(len(some_list)):
        seen[index] = False

    index,count = 0,0
    found = False
    while not found:
        if seen[index] == True:
            return True

        seen[index] = True
        index = some_list[index]
        if index >= len(some_list):
            return False
        if index < 0:
            return False
        count +=1
        if count == len(some_list):
            return False
    return False

print(find_cycle(array))