#from numba import njit,jit

def add(tbl,val,index:int=-1) -> None:
    if not index>-1:tbl.append(val);return
    tbl[index]=val

#@njit
def delete(tbl,val) -> None:
    try:
        tbl.remove(val)
    except ValueError:
        tbl.pop(tbl.index(val))

#@njit
def deli(tbl,i:int=-1) -> None:
    del tbl[i]

#@njit
def count(tbl,val=None) -> int:
    if val==None:return len(tbl)
    amt = 0
    for value in tbl:
        if value==val:amt+=1
    return amt

#@njit
def all(tbl):
    return tbl

#@njit
def foreach(tbl,func) -> None:
    for element in tbl:
        func(element)

#@njit
def pairs(tbl):
    pass
