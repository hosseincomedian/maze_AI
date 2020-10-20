from BFSmaze import bfsmaze
from IDSmaze import idsmaze

stone_list = [(3,4),(3,5),(3,6),(5,2),(7,6),(7,7),(7,8)]  #list divar ha
end = (8,8)  # hadaf ghabel taghyir ast


while True:     # in while baraye check kardan in ast ke karbar khane i ra ke vojood nadarad vared naconad
    x = int(input('x?\t'))  # khaneye feli
    y = int(input('y?\t'))
    if (x > 8 or x < 1 or y >8 or y <1):
        print('adad kharej az range mojaz ast')
        continue
    elif ((x,y) in stone_list):
        print('khane divar ast')
        continue
    else:
        break


if ( end == (x,y) ): #check cardan inke az aval dar hadaf hast ya na
    print ('shoma dar hadaf gharar darid') 

#BFS
else:
    my_maze = bfsmaze( (x,y) ,end ,stone_list )
    my_maze.bfs(0) # in 0 sabet ast va bayad vared shavad va num adad maghsad ast 
    print('masir ba BFS:')   
    for i in range(1,len(my_maze.final_rout)):
        x1 = my_maze.final_rout[i-1][0][0]
        y1 = my_maze.final_rout[i-1][0][1]
        x2 = my_maze.final_rout[i][0][0]
        y2 = my_maze.final_rout[i][0][1]
        print(i+1,':\t', (x1,y1),'\t---->\t', (x2,y2))
#BFS


#IDS
    print('masir ba IDS:')   
    my_maze2 = idsmaze((x,y),end,stone_list)
    my_maze2.ids(0)
    for i in range(1,len(my_maze.final_rout)):
        x1 = my_maze.final_rout[i-1][0][0]
        y1 = my_maze.final_rout[i-1][0][1]
        x2 = my_maze.final_rout[i][0][0]
        y2 = my_maze.final_rout[i][0][1]
        print(i+1,'\t:\t', (x1,y1),'\t---->\t', (x2,y2))
#IDS