def branch_and_bound(sodinh, adj, h, start, stop):
  OPEN=[start]
  
  g=[float('inf')] * sodinh
  g[start]=0
  
  f=[float('inf')] * sodinh
  f[start] = h[start]
  
  CLOSE=[]
  CHA=[-1] * sodinh
  
  fmin = float('inf')
    
  while(len(OPEN) > 0):
    n = OPEN.pop(0)    
    print(f"n={n}")
                
    CLOSE.append(n)
    print(f"CLOSE={CLOSE}")
    
    if n == stop:
      if f[n] < fmin:
        print(f"cap nhat fmin {f[n]} < {fmin}")
        fmin = f[n]
      
      print(f"ko cap nhat fmin {f[n]} >= {fmin}")
      print()
      continue
        
    if f[n] >= fmin:
      print(f"Xem tia {f[n]} > {fmin}")
      print()
      continue
        
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
          continue
          
        if i in CLOSE: # thuoc CLOSE
          if fi < f[i]:
            g[i] = gi
            f[i] = fi
            CHA[i] = n
            Tn.append(i)
          continue
          
        if i in OPEN: # thuoc OPEN
          if fi < f[i]:
            g[i] = gi
            f[i] = fi
            CHA[i]=n
          continue
        
        if fi < f[i]: # thuoc OPEN && CLOSE
          g[i] = gi
          f[i] = fi
                           
    Tn.sort(key=lambda x:f[x])
                                 
    print(f"T[{n}]={Tn}")
         
    OPEN = Tn + OPEN
        
    print(f"OPEN={OPEN}")
    print(f"CHA={CHA}")
    print()
  
  print(f"Tim thay duong di tu {start} - {stop} f={fmin}")
  i=stop
  while i != -1:
    if CHA[i] == -1:
      print(i)
    else:
      print(i, end="<==")
    i=CHA[i]