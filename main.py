for i in range(1,10):

    for s in range(1,i):

        print(end="          ")

    for j in range(i,10):

        print(f"{i:2d}x{j:<2d}={i*j:2d}",end="  ")

        #print("%d*%d=%d"%(i,j,i*j),end=" ")

    print()



