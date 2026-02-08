from collections import Counter

def solution(k, tangerine):
    cnt = Counter(tangerine)
    freqs = sorted(cnt.values(), reverse=True)
    
    
    kinds = 0
    for f in freqs:
        k -= f
        kinds += 1
        if k <= 0:
            break
    return kinds