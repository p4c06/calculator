class Set:
    
    def __init__(self, elements):
        self.elements = set(elements)
    
    def __str__(self):
        return str(self.elements)  
    
    def add(self, a):
        self.elements.add(a)
    
    @property
    def size(self):
        return len(self.elements)
    
    @classmethod
    def intersection(cls, A, B):
        result = Set({})
        for element in A.elements:
            if element in B.elements:
                result.add(element)
        return result
    
    @classmethod
    def union(cls, A, B):
        result = Set({})
        for element in A.elements:
            result.add(element)
        for element in B.elements:
            result.add(element)
        return result
    
    def difference(self, B):
        result = Set({})
        for element in self.elements:
            if element in B.elements:
                continue
            result.add(element)
        return result
    
    def issubset(self, B):
        for element in self.elements:
            if element not in B.elements:
                return False
        return True
    
    @classmethod
    def aredisjoint(cls, A, B):
        return Set.intersection(A, B).size == 0
    
    def contains(self, a):
        return a in self.elements

num = int(input("how many sets will you need: "))
arr = []

for i in range(num+1):
    arr.append(Set({}))

operation = input(">")
while operation != 'quit':
    arguments = operation.split(' ')
    name = arguments[0]

    if name == 'add':
        what = int(arguments[1])       
        for i in arguments[2:]:
            arr[what].add(int(i))
    elif name == 'show':
        what = int(arguments[1])
        print(arr[what])
    elif name == 'size':
        what = int(arguments[1])
        print(arr[what].size)
    elif name == 'reset':
        what = int(arguments[1])
        arr[what] = Set({})
    elif name == 'union':
        first, second, where = [int(i) for i in arguments[1:]]
        arr[where] = Set.union(arr[first], arr[second])
    elif name == 'intersection':
        first, second, where = [int(i) for i in arguments[1:]]
        arr[where] = Set.intersection(arr[first], arr[second])
    elif name == 'difference':
        first, second, where = [int(i) for i in arguments[1:]]
        arr[where] = arr[first].difference(arr[second])
    elif name == 'issubset':
        first, second = [int(i) for i in arguments[1:]]
        if arr[first].issubset(arr[second]):
            print("YES")
        else:
            print("NO")
    elif name == 'contains':
        first, second = [int(i) for i in arguments[1:]]
        if arr[first].contains(second):
            print("YES")
        else:
            print("NO")
    elif name == "aredisjoint":
        first, second = [int(i) for i in arguments[1:]]
        if Set.aredisjoint(arr[first], arr[second]):
            print("YES")
        else:
            print("NO")
    elif name == "help":
        print("""
Welcome to set calculator!

You can do 11 operations:
    1. show {id}: shows all elements of the give set
    2. add {id} {number1} {number2} ...: add given numbers to given set
    3. aredisjoint {id1} {id2}: checks if giiven sets are disjoint
    4. issubset {id1} {id2}: checks if first set is subset of second set
    5. union {id1} {id2} {id3}: writes the result of union beteween to sets to third set
    6. intersection {id1} {id2} {id3}: writes the result of intersection beteween to sets to third set
    7. difference {id1} {id2} {id3}: writes the result of difference beteween to sets to third set
    8. size {id}: shows size of give set
    9. contains {id} {number}: checks if number belong to set
    10. help: shows this menu
    11. quit: quits program

""")
    else:
        print("'", name, "' is not a command.")
        print("To see list of commnds write 'help'")


    operation = input(">")

