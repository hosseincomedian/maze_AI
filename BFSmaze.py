class bfsmaze: #jostojooye arz nolhost
    start = () #noghte aghaz
    stone_list = [] #divarha
    masir = [] # masir ba hefz pedar
    nodes = [] # serfan node haye moshahede shode
    end = () #noghte payan
    final_rout=[] #javab
    def __init__(self ,start ,end ,stone_l=()):
            self.start = start
            self.stone_list = stone_l
            self.masir.append((start,(-1,-1)))
            self.nodes.append(start)
            self.nodes.extend(stone_l)  # stone ha dalhel khane haye az ghabl rafte and pas dakhel An ha nemishavim
            self.end = end 
            self.final_rout=[]
    #do tabe zir baraye bfs ast 
        #sakht bfs
    def bfs(self,num) :
        x = self.masir[num][0][0]
        y = self.masir[num][0][1]
        if (self.masir[num][0]==self.end):
            self.nodes =[]
            self.bfs_rout(num)
            return 

        if ( 0< x+1 <9 and (x+1,y) not in self.nodes): #rast
            self.nodes.append ((x+1,y))
            self.masir.append (((x+1,y),(x,y)))

        if ( 0< y+1 <9 and (x,y+1) not in self.nodes): #bala
            self.nodes.append ((x,y+1))
            self.masir.append (((x,y+1),(x,y)))

        if ( 0< y-1 <9 and (x,y-1) not in self.nodes): #payin
            self.nodes.append ((x,y-1))
            self.masir.append (((x,y-1),(x,y)))

        if ( 0< x-1 <9 and (x-1,y) not in self.nodes): #chap
            self.nodes.append ((x-1,y))
            self.masir.append (((x-1,y),(x,y)))
        self.bfs(num+1)
        #masir bfs
    def bfs_rout(self,num): #yaftan masir az rooye algoritm
        self.final_rout.insert (0,self.masir[num])
        if (num == 1):
            if self.masir[num][0] == self.final_rout[0][1]:
                self.final_rout.insert (0,self.masir[num])
                num = num - 1
            self.final_rout.insert (0,self.masir[0])
            return
        for i in range (num-1,0,-1):
            if self.masir[num][1] == self.masir[i][0]:
                num = i
                break
        self.bfs_rout(num)