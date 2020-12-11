n = int(input("enter number of nodes"))
mat = []
print("enter elements row wise")
for i in range(n):
  a=[]
  for j in range(n):
    a.append(int(input()))
  mat.append(a)

for i in range(n):
    for j in range(n):
        print(mat[i][j], end = " ") 
    print()
l=[]

for i in range(n):
  l.append(chr(i+65))
  
print(l)  
def belongs(v,Q):
  for i in Q:
    if v==i:
      return 1
  return 0

def extract_min(Q,d):
  min_pos=Q[0]
  for i in Q:
    if d[i]<d[min_pos]:
      min_pos=i
  return min_pos
  
def adj(u,v):
  if mat[u][v]>0 and mat[u][v]!=9999:
    return 1
  return 0

def Dijkstra(r):
  d = [9999]*n
  pi = [-1]*n
  d+
/[r]=0
  Q=[]
  for i in range(n):
    Q.append(i)

  while len(Q):

    u=extract_min(Q,d)
    for v in range(n):
      if adj(u,v) and belongs(v,Q):
        if d[v]>(d[u]+mat[u][v]):
          d[v]=d[u]+mat[u][v]
          pi[v]=u
    Q.remove(u)
  return d,pi

dist=[]
parent = []
for i in range(n):
  dist.append(Dijkstra(i)[0])
  parent.append(Dijkstra(i)[1])


for i in range (n):
    
    
    for j in range(n):
        
        if(parent[i][j]==-1 or parent[i][j]==i):
            parent[i][j]=-1
for i in range (n):
    print("This is the Routing Table for Vertex :",chr(i+65))
    print("To"+"\t"+"Cost"+"\t"+"Next")
    for j in range(n):
        
        print(l[j],"\t",dist[i][j],"\t",chr(parent[i][j]+65) if parent[i][j]!=-1 else '-',end="\n")
    print()
