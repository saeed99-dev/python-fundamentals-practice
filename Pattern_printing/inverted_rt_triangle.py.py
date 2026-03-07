# for i in range(1,5):
#     for j in range(1,5+1-i):
#         print("*",end=" ")
#     print()


# for i in range(1,5):
#     for j in range(1,1+i):
#         print(j,end=" ")
#     print()


# for i in range(1,5):
#     for j in range(1,5+1-i):
#         print(j,end=" ")
#     print()


# for i in range(4):
#     for j in range(1+i):
#         print(2*j+1,end=" ")
#     print()


# for i in range(1,5):
#     for j in range(ord('A'),ord('E')):
#         print(chr(j),end=" ")
#     print()



# for i in range(1, 5):
#     for j in range(ord("A"), ord("A") + i):
#         print(chr(j), end=" ")
#     print()



# for i in range(1, 6):
#     for j in range(ord("A"), ord("A") + i):
#         if i%2!=0:
#             print(j-64, end=" ")
#         else:
#             print(chr(j), end=" ")
#     print()



for i in range(5):
    for j in range(5):
        if i==2 or j==2:
            print("*",end="")
        else:
            print(" ",end="")  # not getting it
    print()