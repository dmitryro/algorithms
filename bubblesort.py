 

# bubblesort.py

a = [4, 17, 6, 2, 19, 33, 77, 44, 21, 7, 5, 3]

print a

print range(len(a)-1, 0, -1) 

def bubblesort(a):

    for swap in range(len(a)-1, 0, -1):
        print swap
        for index in range(swap):

            if a[index] > a[index + 1]:

                a[index], a[index + 1] = a[index + 1], a[index]

    return a

 

a = bubblesort(a)

print a
