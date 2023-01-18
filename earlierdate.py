# I tried two methods on this problem, because I was trying to figure out whether an if/elif structure 
# was necessary. I realized it wasn't if the function returned the string if the comparison was True,
# so I rewrote the function with if/elif to see the difference.
def earlier(x:int,y:int,z:int,a:int,b:int,c:int):
    # takes two dates, format (mm, dd, yyyy, mm, dd, yyyy)
    if c > z:
        return "earlier"
    if c < z:
        return "after"
    if a > x:
        return "earlier"
    if a < x:
        return "after"
    if b > y:
        return "earlier"
    if b < y:
        return "after"
    return "same"

def earlier_try_two(x:int,y:int,z:int,a:int,b:int,c:int):
    # takes two dates, format (mm, dd, yyyy, mm, dd, yyyy)
    rtn = ""
    if c > z:
        rtn = "earlier"
    elif c < z:
        rtn = "after"
    elif a > x:
        rtn = "earlier"
    elif a < x:
        rtn = "after"
    elif b > y:
        rtn = "earlier"
    elif b < y:
        rtn = "after"
    else: 
        rtn = "same"
    return rtn

print (earlier(12, 1, 2005, 12, 1, 2005))
print (earlier_try_two(12, 10, 2004, 12, 1, 2005))

