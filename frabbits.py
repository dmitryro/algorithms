def fib_rabbits(n):
   if  (n==1):
       print str(n) + ','
       return 1
   if  (n==2):
       print str(n) + ','  
       return 1
   else:
       print str(n) + ','
       return fib_rabbits(n-1)+fib_rabbits(n-2)


def main():
    f = fib_rabbits(10)
    print f


if __name__=='__main__':
    main()


