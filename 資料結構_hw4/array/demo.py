import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import sys
import csv
import array_new
import time

#n=input()
#n=int(n)


def drawgraph():
    G=nx.Graph()
    color_map=[]
    row=[]
    col=[]
    
    weightArr = [[0]*n for i in range(n)]
    g=array_new.Graph(n) #做djikstra的複製

    #生四個city
    row.append(200)
    col.append(200)

    row.append(800)
    col.append(200)

    row.append(800)
    col.append(800)

    row.append(200)
    col.append(800)
    
    for i in range(0,4):
        G.add_node(i,pos=(row[i],col[i]))
        color_map.append("red")

    #City 互相連線    
    for i in range(0,4):
           if i!=3:
                dx=row[i]-row[i+1]
                dy=col[i]-col[i+1]
                s=dx*dx+dy*dy
                distance=int(math.sqrt(s))
                G.add_edge(i,i+1,weight=distance)
                weightArr[i][i+1]=distance #做djikstra會用到
                weightArr[i+1][i]=distance #做djikstra會用到
            
    dx=row[0]-row[3]
    dy=row[0]-col[3]
    s=dx*dx+dy*dy
    distance=int(math.sqrt(s))
    G.add_edge(0,3,weight=distance)
    weightArr[0][3]=distance #做djikstra會用到
    weightArr[3][0]=distance #做djikstra會用到
            

    #生其他點
    for i in range(4,n):
        x=random.randint(0,1000)
        y=random.randint(0,1000)
        row.append(x)
        col.append(y)
        G.add_node(i,pos=(x,y))
        color_map.append("blue")

        #City和dis連線
        for j in range(0,4):
            dx=row[i]-row[j]
            dy=col[i]-col[j]
            s=dx*dx+dy*dy
            distance=int(math.sqrt(s))
            
            
            if distance<=175:
                color_map[i]="gold"
                G.add_edge(i,j,weight=distance)
                weightArr[i][j]=distance #做djikstra會用到
                weightArr[j][i]=distance #做djikstra會用到

    
    #全部的點和其他點連線
    for i in range(0,n):
        for j in range(0,n):
            dx=row[i]-row[j]
            dy=col[i]-col[j]
            s=dx*dx+dy*dy
            distance=int(math.sqrt(s))
        
            if i!=j and distance>0 and distance<150:
                G.add_edge(i,j,weight=distance)
                weightArr[i][j]=distance #做djikstra會用到
                weightArr[j][i]=distance #做djikstra會用到
    

    g.graph=weightArr    
    spl=dict(nx.all_pairs_dijkstra_path_length(G))
    cn2=n*(n-1)/2
    total=0
    restart=0

    for node1 in spl:
        r_counter=0
        for node2 in spl[node1]:
            r_counter+=1
            total=total+spl[node1][node2]
#            print("Length between ",node1,"and", node2 ,"is",spl[node1][node2])
             
        if r_counter!=n:
            restart=1

    if restart==0:
        average=total//2//cn2
        average=round(average,2)
        
        start =time.time()
        g.dijkstra(0);
        end=time.time()
        Time=end-start
        print("n:",n," average:",average," Time:",Time)
        with open(filename, 'a') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow([n,average,Time])
        nx.draw(G,nx.get_node_attributes(G,'pos'),with_labels=True,node_size=300,node_color=color_map)
        plt.show()    
        
    
#    print("cn2:",cn2,"total:",total,"restart:",restart,"average:",average)
    
    
    return restart

num=sys.argv[1]
filename=sys.argv[2]
n=int(num)
n=n*10
x=drawgraph()
while(x==1):
    x=drawgraph()




#nx.draw_networkx_edge_labels(G, nx.get_node_attributes(G,'pos'),edge_labels=edge_labels)
#nx.draw(G,nx.get_node_attributes(G,'pos'),with_labels=True,node_size=300,node_color=color_map)
#plt.show()    



