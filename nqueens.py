def queens(n):
    chessBoard = [["."]*n for i in range(n)]
    res = []
    col = set()
    posD = set()
    negD = set()
    def bt (r):
        if r == n:
            res.append(["".join(row) for row in chessBoard])
            return
        for c in range(n):
            if(c in col or (r-c) in posD or (r+c) in negD):
                continue    
            col.add(c)
            posD.add(r-c)
            negD.add(r+c)
            chessBoard[r][c]="Q"

            bt(r+1)
            
            col.remove(c)
            posD.remove(r-c)
            negD.remove(r+c)
            chessBoard[r][c]="."
            
    bt(0)
    return res
n = int(input("Enter the value of n: "))
print(queens(n))
    