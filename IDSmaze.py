class idsmaze: #jostojooye arz nolhost
    level = int() #omgh
    masir = [] # masir ba hefz pedar
    stone_list = [] #divarha
    nodes = [] # serfan node haye moshahede shode
    end = () #noghte payan
    start =()
    final_rout=[]
    def __init__(self ,start ,end ,stone_l=()):
        self.start = start
        self.stone_list = stone_l
        self.end = end 
        self.level = 0
        self.masir.append(((start[0],start[1],0),(-1,-1,-1)))
        self.nodes.append((start[0],start[1]))
        self.nodes.extend(stone_l)  # stone ha dalhel khane haye az ghabl rafte and pas dakhel An ha nemishavim
        self.final_rout = []

    def check_nodes(self,x,y,level): #agar masir behtari be jayi ke dar gozashte ba hazine bishtar raftim bashad jaygozin miconad
        for i in self.masir:
            if (i[0][0] == x and i[0][1] == y and i[0][2]>level):
                self.masir.remove(i)
                return True


    #do tabe zir baraye bfs ast 
        #sakht bfs
    def ids(self,num) :

        
        # if (num >= len(self.masir)):
        #     self.level = self.level+1
        #     self.masir =[]
        #     self.nodes =[]
        #     self.masir.append(((self.start[0],self.start[1],0),(-1,-1)))
        #     self.nodes.append(self.start)
        #     self.nodes.extend(self.stone_list)
        #     self.ids(0)
        x = self.masir[num][0][0]
        y = self.masir[num][0][1]
        level = self.masir[num][0][2]
        if ((x,y)== self.end):
            self.masir = self.masir[:num+1].copy()
            self.nodes =[]
            self.ids_rout(num)
            return 


        if (level+1 <= self.level and num < len(self.masir)):
            
            if ( 0< x-1 <9 and ((x-1,y) not in self.nodes or self.check_nodes(x-1,y,level+1)) ): #chap
                
                new_node = (x-1,y,level+1)
                self.nodes.append ((x-1,y))
                self.masir.insert (num+1,(new_node,(x,y,level)))


            if ( 0< y-1 <9 and ( (x,y-1) not in self.nodes or self.check_nodes(x-1,y,level+1))): #payin
                self.check_nodes(x-1,y,level+1)
                new_node=(x,y-1,level+1)
                self.nodes.append ((x,y-1))

                self.masir.insert (num+1,(new_node,(x,y,level)))

            if ( 0< y+1 <9 and  ( (x,y+1) not in self.nodes or self.check_nodes(x-1,y,level+1) )): #bala
                self.check_nodes(x-1,y,level+1)
                new_node =(x,y+1,level+1)
                self.nodes.append ((x,y+1))
                self.masir.insert (num+1,(new_node,(x,y,level)))
            
            if ( 0< x+1 <9 and ( (x+1,y) not in self.nodes or self.check_nodes(x-1,y,level+1) )): #rast
                self.check_nodes(x-1,y,level+1)
                new_node=(x+1,y,level+1)
                self.nodes.append ((x+1,y))
                self.masir.insert(num+1,(new_node,(x,y,level)))

            if (num+1 < len(self.masir)):
                self.ids(num+1)
            else :
                self.level = self.level+1
                self.masir =[]
                self.nodes =[]
                self.masir.append(((self.start[0],self.start[1],0),(-1,-1)))
                self.nodes.append(self.start)
                self.nodes.extend(self.stone_list)
                self.ids(0)
            
        else :

            if (num+1 >= len(self.masir)):
                self.level = self.level+1
                self.masir =[]
                self.nodes =[]
                self.masir.append(((self.start[0],self.start[1],0),(-1,-1)))
                self.nodes.append(self.start)
                self.nodes.extend(self.stone_list)
                self.ids(0)

            else:
                    self.ids(num+1)

        #masir ids

    def ids_rout(self,num): #yaftan masir az rooye algoritm
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
        self.ids_rout(num)


