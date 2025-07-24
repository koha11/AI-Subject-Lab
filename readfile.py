def read_mtk(filename):
  
    with open(filename) as f:
        sodinh = int(f.readline())
        adj = []
        
        for i in range(sodinh):
            # TODO: write code...
            line=list(map(int, f.readline().strip().split()))
            adj.append(line)
         
    return sodinh, adj

def read_heuristic(filename):
  
    with open(filename) as f:        
        h = list(map(int, f.readline().strip().split()))
 
    return h