from collections import Counter
def MinSubStringWindow(str):
    N, K = str[0], str[1]
    need = Counter(K)
    left = 0
    min_substr = ""
    window_count = Counter()
    formed = 0
    min_len =  float('inf')
    for right in range(len(N)):
        window_count[N[right]] += 1
        if window_count[N[right]] == need[N[right]]:
            formed += 1
        while left < right and formed == len(need):
            if left + right - 1 < min_len:
                min_len = left + right - 1
                min_substr = N[left: right + 1]
            window_count[N[left]] -= 1
            if window_count[N[left]] < need[N[left]]:
                formed -=1
            left += 1      
    return min_substr