def solution(input):
    '''
    x="the brown fox jumped over the fence\nthe brown bear fell down the hill\n\bThe big lion chased the deer\nThe monkey ate the bananas\n\b"
    '''
    #break the stirng by \b split
    break_by_b = input.split('\b')
    res, break_by_n, join_reversed = [], [], []
    for elem in break_by_b: 
        tmp = elem.split('\n')
        for break_by_space in tmp:
            words = break_by_space.split()
            join_reversed.append(" ".join(reversed(words)))
        break_by_n = "\n".join(reversed(join_reversed))
        #print(break_by_n)
    res = "\b".join((break_by_n))  
    #print(res)
    return res
    #print(break_by_b)

x="the brown fox jumped over the fence\nthe brown bear fell down the hill\n\bThe big lion chased the deer\nThe monkey ate the bananas\n\b"
#solution(x)
print(solution(x))
