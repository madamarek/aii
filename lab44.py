def generate_triangles():
    n = 0
    total = 0
    while True:
        total += n
        n += 1
        yield total
        
def test_operator():
    print(operator.add(2,3))
    print(operator.mul(3, 8))
    print(operator.pow(3, 4))
    print(operator.itemgetter(1)([2, 3, 4]))
        
def test_ord():
    words = ['pear', 'cabbage', 'apple', 'bananas']
    print(min(words))  
    words.sort(key=lambda s: s[-1])  
    print(words) 
    print(max(words, key=len))
    print(min(words, key=lambda s: s[1::2]))
