"""Output:
5
4
3
2
1
"""
def print_number(n):
    if n==0:
        return
    print(n)
    print_number(n-1)

if __name__=="__main__":
    print_number(5)