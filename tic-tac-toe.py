m=[[1,2,2],[2,1,1],[1,1,2]]
if((m[0][0]==m[0][1]) and (m[0][1]==m[0][2]) and (m[0][2]==m[0][0]) and m[0][0]==1):
    print("1 wins")
elif((m[0][0]==m[0][1]) and (m[0][1]==m[0][2]) and (m[0][2]==m[0][0]) and m[0][0]==2):
    print("2 wins")
elif((m[1][0]==m[1][1]) and (m[1][1]==m[1][2]) and (m[1][2]==m[1][0]) and m[1][0]==1):
    print("1 wins")
elif((m[1][0]==m[1][1]) and (m[1][1]==m[1][2]) and (m[1][2]==m[1][0]) and m[1][0]==2):
    print("2 wins")
elif((m[2][0]==m[2][1]) and (m[2][1]==m[2][2]) and (m[2][2]==m[2][0]) and m[2][0]==1):
    print("1 wins")
elif((m[2][0]==m[2][1]) and (m[2][1]==m[2][2]) and (m[2][2]==m[2][0]) and m[2][0]==2):
    print("2 wins")
elif((m[0][0]==m[1][0]) and (m[1][0]==m[2][0]) and (m[2][0]==m[0][0]) and m[0][0]==1):
    print("1 wins")
elif((m[0][0]==m[1][0]) and (m[1][0]==m[2][0]) and (m[2][0]==m[0][0]) and m[0][0]==2):
    print("2 wins")
elif((m[0][1]==m[1][1]) and (m[1][1]==m[2][1]) and (m[2][1]==m[0][1]) and m[0][1]==1):
    print("1 wins")
elif((m[0][1]==m[1][1]) and (m[1][1]==m[2][1]) and (m[2][1]==m[0][1]) and m[0][1]==2):
    print("2 wins")
elif((m[0][2]==m[1][2]) and (m[1][2]==m[2][2]) and (m[2][2]==m[0][2]) and m[0][2]==1):
    print("1 wins")
elif((m[0][2]==m[1][2]) and (m[1][2]==m[2][2]) and (m[2][2]==m[0][2]) and m[0][2]==2):
    print("2 wins")
elif((m[0][2]==m[1][1]) and (m[1][1]==m[2][0]) and (m[2][0]==m[0][2]) and m[0][2]==1 ):
    print("1 wins")
elif((m[0][2]==m[1][1]) and (m[1][1]==m[2][0]) and (m[2][0]==m[0][2]) and m[0][2]==2 ):
    print("2 wins")
else:
    print("draw")