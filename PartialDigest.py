# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:04:09 2018

@author: taro
"""

def PartialDegest(L):
    width = max(L)
    del(L[L.index(width)])
    X = [0, width]
    Place(L,X,width)

def Place(L,X,width):
    if len(L) == 0:
        print(X)
        return
    y = max(L)
    deltay = [abs(x-y) for x in X]
    if isin(deltay,L):
        rem(deltay,L)
        X.append(y)
        Place(L,X,width)
        L.extend(deltay)
        del(X[X.index(y)])
    deltaw = [abs(x-(width-y)) for x in X]
    if isin(deltaw,L):
        rem(deltaw,L)
        X.append(width-y)
        Place(L,X,width)
        L.extend(deltaw)
        del(X[X.index(width-y)])
    return

def isin(a,b):
    for x in a:
        if a.count(x) > b.count(x):
            return False
    return True


def rem(a,b):
    for x in a:
        del(b[b.index(x)])
    return
