def DFS(sodinh, adj, start, stop):
    OPEN=[start]
    CLOSE=[]
    CHA= [-1] * sodinh
    while(len(OPEN) > 0):
        n = OPEN.pop(0)
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
            if adj[n][i] == 1 and i not in OPEN and i not in CLOSE:
                CHA[i] = n
                Tn.append(i)
                
        print(f"T[{n}]={Tn}")
        
        OPEN = Tn + OPEN
        print(f"OPEN={OPEN}")
        print(f"CHA={CHA}")
        print()

        
    print(f"Ko tim thay duong di tu {start} - {stop}")
    return False    
    