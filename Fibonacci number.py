# A program that computes the nth Fibonacci number were n is a value input given by the user.

def fibo(n):
    cur,prev = 1,1
    for i in range(n-2):
        cur,prev = cur+prev, cur
        
    return cur

def main():
    n = eval(input("Enter the nth value :"))
    print("The nth nnumber of the Fibonacci series is", fibo(n))
main()
