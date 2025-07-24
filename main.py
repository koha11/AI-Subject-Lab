from bfs import BFS
from dfs import DFS
from hill_climbing_search import hill_climbing_search
from best_first_search import best_first_search
from at import AT
from cms import CMS
from a_star import a_star
from branch_and_bound import branch_and_bound


from readfile import read_mtk, read_heuristic

if __name__ == "__main__":
    # mtk_filename = "hcs.mtk"
    # h_filename = "hcs.heuristic"
    
    # mtk_filename = "best_first_search.mtk"
    # h_filename = "best_first_search.heuristic"
    
    # mtk_filename = "at.mtk"
    # h_filename = "at.heuristic"
    
    # mtk_filename = "cms.mtk"
    
    # mtk_filename = "a_star.mtk"
    # h_filename = "a_star.heuristic"
    
    mtk_filename = "branch_and_bound.mtk"
    h_filename = "branch_and_bound.heuristic"
    
    sodinh,adj = read_mtk(f"data/{mtk_filename}")
    h = read_heuristic(f"data/{h_filename}")

    # BFS(sodinh, adj, 0, 7)
    # DFS(sodinh, adj, 0, 4)
    # hill_climbing_search(sodinh,adj,h,0,8)
    # best_first_search(sodinh,adj,h,0,6)
    # AT(sodinh,adj,h,17,16)
    # CMS(sodinh, adj, 0, 9)
    # a_star(sodinh,adj,h,0,10)
    # branch_and_bound(sodinh,adj,h,0,7)

    

    

    
    
    
    