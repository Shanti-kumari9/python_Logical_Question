a=["3","4",3,4,6,"10","12","rena"]
def count(a):
    i=0
    c=0
    while i<len(a):
        if type(a[i]) == str:
            c=c+1
        i=i+1
    return(c)
print(count(a))
# COUNT STRING...................................
# ====================================================================================================