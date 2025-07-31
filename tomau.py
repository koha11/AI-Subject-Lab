def tim_bac(n, adj, i):
  bac = 0
  
  for j in range(n):
    if(adj[i][j] == 1):
      bac += 1
      
  return bac

def to_mau(n, adj):
  color = [0] * n
  mau = 1
  
  bac = list(tim_bac(n,adj,i) for i in range(n))
  
  V = list(i for i in range(n))
  V.sort(key=lambda x: bac[x], reverse=True)
  
  print("so bac:")
  print(V)  
  print(bac)
  print()
  
  while len(V) > 0:
    color[V[0]] = mau
    currents = [V[0]]
    
    print(f"to mau {mau} cho dinh {V[0]}")
    for v in V:
      isToMau = True
      if(color[v] == 0):
        for j in currents:
          if(adj[v][j] == 1):
            isToMau = False
            break
        if isToMau:
          color[v] = mau
          currents.append(v)
          print(f"to mau {mau} cho dinh {v}")

    print(V)  
    
    for c in currents:
      V.remove(c)
    
    mau += 1
  
  colors = ["xanh bien","xanh la","do"]
  for i,c in enumerate(color):
    print(f"Dinh {i} to mau {colors[c-1]}")
  
  return 0