def a_star(sodinh, adj, h, start, stop):
  OPEN=[start]
  
  g=[float('inf')] * sodinh
  g[start]=0
  
  f=[float('inf')] * sodinh
  f[start]=h[start]
  
  CLOSE=[]
  CHA=[-1] * sodinh
  
  while(len(OPEN) > 0):
    n = OPEN.pop(0)
    
    print(f"n={n}")
    
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
    
    CLOSE.append(n)
    print(f"CLOSE={CLOSE}")
        
    Tn = []
    
    for i in range(sodinh):
      if adj[n][i] > 0:
        gi = g[n] + adj[n][i]
        fi = gi + h[i]
        
        if i not in OPEN and i not in CLOSE: # ko thuoc OPEN && CLOSE
          CHA[i] = n
          Tn.append(i)
          g[i] = gi
          f[i] = fi
        else:
          if fi < f[i]:
            g[i] = gi
            f[i] = fi
                              
    print(f"T[{n}]={Tn}")
    
    
    OPEN += Tn
    
    OPEN.sort(key=lambda x : f[x])
    
    print(f"OPEN={OPEN}")
    print(f"CHA={CHA}")
    print()

  
  print(f"Ko tim thay duong di tu {start} - {stop}")
  return False