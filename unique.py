def unique(S, start, stop):
    print(s[start:stop])
    print(stop-start,stop,start)
    if stop - start <= 1: return True # at most one item
    elif not unique(S, start, stop-1): return False # first part has duplicate
    elif not unique(S, start+1, stop): return False # second part has duplicate
    else: return S[start] != S[stop-1]

start=0
s=[1,2,3]

print(unique(s,start,len(s)))