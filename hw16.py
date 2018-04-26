def union(a, b):
    return a + [val1 for val1 in b if val1 not in a]

def intersect(a, b):
    return [val1 for val1 in a if val1 in b]

def setdiff(a, b):
    return [val1 for val1 in a if val1 not in b]

def symdiff(a,b):
    return setdiff(union(a,b), intersect(a,b))

def cartproduct(a,b):
    return [(val1, val2) for val1 in a for val2 in b]

print "sets [1,2,3,4 and [3,4,5]"
print "union: " + str(union([1,2,3,4],[3,4,5]))
print "intersect: " + str(intersect([1,2,3,4],[3,4,5]))
print "set diff: " + str(setdiff([1,2,3,4],[3,4,5]))
print "set diff 2: " + str(setdiff([3,4,5],[1,2,3,4]))
print "sym diff: " + str(symdiff([1,2,3,4],[3,4,5]))
print "cart product: " + str(cartproduct([1,2,3,4],[3,4,5]))

