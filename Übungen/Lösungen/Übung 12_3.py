from typing import Iterator

def getFirstElem(derIter:Iterator,default:any = None) -> any:
    try:
        return next(derIter)
    except StopIteration:
        return default

