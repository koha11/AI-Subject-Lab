def CMS(sodinh, adj, start, stop):
  OPEN=[start]
  g=[float('inf')] * sodinh
  g[start]=0
  CLOSE=[]
  CHA=[-1] * sodinh
  
  while(len(OPEN) > 0):
    print(f"g = {g}")
    n = min(OPEN, key=lambda x: g[x]) 
    
    # thop co nhieu dinh trong OPEN == min, co chua stop trong do
    min_list = [i for i, x in enumerate(g) if x == g[n]]        
    if stop in min_list and stop in OPEN: 
      n = stop

    OPEN.remove(n)
    
    print(f"n={n}")
    CLOSE.append(n)
    print(f"CLOSE={CLOSE}")
    
    if n == stop:
      print(f"Tim thay duong di tu {start} - {stop}")
      i=stop
      while i != -1:
        if CHA[i] == -1:
          print(i)
        else:
          print(i, end="<==")                
        i=CHA[i]
          
      return True
        
    Tn = []
    
    for i in range(sodinh):
      if adj[n][i] > 0 and i not in OPEN and i not in CLOSE: # ko thuoc CLOSE && OPEN
        CHA[i] = n
        Tn.append(i)
        g[i] = g[n] + adj[n][i]
        
      if adj[n][i] > 0 and i in OPEN: # thuoc OPEN
        gnew = g[n] + adj[n][i]
        
        if gnew < g[i]:
          CHA[i] = n
          g[i] = gnew
                    
    print(f"T[{n}]={Tn}")
    
    OPEN += Tn
    
    print(f"OPEN={OPEN}")
    print(f"CHA={CHA}")
    print()
  
  print(f"Ko tim thay duong di tu {start} - {stop}")
  return False