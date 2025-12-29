def solution(ineq, eq, n, m):
    answer = 0
    
    if ineq==">":
        if eq=="=":
            return n>=m
        
    else:
        return 0
    

print(solution(">", "=", 1,1))
