def solution(x):
    '''
    recursively to flatten the list
    x = [[4,5],[[1,2,3]],6,[]] -> [4,5,[1,2,3],6] -> [4,5,1,2,3,6]
    '''
    res = []
    for sub in x:
        if not isinstance(sub, list):
            res.append(sub)
        else:
            res.extend(solution(sub))
    return res
   
print(solution([[4,5],[[1,2,3]],6,[]]) )
