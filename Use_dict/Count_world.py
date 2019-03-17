def count_world(text_file):
    count = {}  #define emty dict
    fhand = open(text_file)
    for line in fhand:
        TEMP = line.split()
        for name in TEMP:
            count[name] = count.get(name, 0) + 1
            '''
            The get(name,0) function adds 1 to the key value if "name" exists in "key" and,
            if not, initializes to "key = name" and "value = 0".
            '''
    Big_count = None
    for A,B in count.items(): # A = key , B = value
        if Big_count is None or B > Big_count:
            max_array = list()
            max_array = [(A, int(B))]
            Big_count = B
        elif B == Big_count:
            max_array.append((A , int(B))) #add A,B in max_array
    return max_array   

if __name__ == '__main__':
    print('Func_called - main')
    max_array = count_world("example1.txt")
    print("------ example1.txt -----")
    for world, count in max_array:
        print("world : " + world  + " //count : "+str(count))
    print("------ example.txt ------")
    max_array = count_world("example.txt")
    for world, count in max_array:
        print("world : " + world  + " //count : "+str(count))
    print("-------------------------")
        
else:
    print('Func_called - imported')
    
'''
----------result---------
Func_called - main
------ example1.txt -----
world : hello //count : 3
world : hi //count : 3
------ example.txt ------
world : to //count : 87
-------------------------
-------------------------
'''