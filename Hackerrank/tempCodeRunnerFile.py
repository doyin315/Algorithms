for x1,y1 in [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)]:
            if 0<=x1<len(arr) and 0<=y1<len(arr[0]) and not seen.get((x1,y1),False) and arr[x1][y1]==1:
                q.append((x1,y1))
                seen[(x1,y1)]=True
                print(q,counter)