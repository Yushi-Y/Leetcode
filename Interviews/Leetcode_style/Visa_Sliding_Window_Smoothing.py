# sliding window approach for smoothing - O(N) computational complexity
def smooth(inlist, h):
    """
    This function performs a basic smoothing of inlist and returns the result (outlist).
    Both lists have the same length, N. Each item in inlist is assumed to have type 'float',
    and 'h' is assumed to be an integer. For each i, outlist[i] will be the average of inlist[k]
    over all k that satisfy i-h <= k <= i+h and 0 <= k <= N-1.
    """
    N = len(inlist)
    outlist = [0.0] * N

    if h == 0:
       return inlist

    if h >= N-1:
       # return the average of list entries
       avg = sum(inlist) / N
       outlist = [avg] * len(inlist)
       return outlist 

    if h+1 < N <= 2*h:
       for i in range(N):
           left = max(0, i-h)
           right = min(N, i+h)
           window = inlist[left:right+1]
           outlist[i] = sum(window) / len(window)
       return outlist

    # if N > 2*h
    # the first h elements
    for i in range(h+1):
        outlist[i] = sum(inlist[:h+i+1]) / (h+i+1)

    # the middle elements
    window = inlist[:2*h+1]
    for i in range(h+1, N-h):
        window.append(inlist[i+h])
        window.pop(0)
        outlist[i] = sum(window) / len(window)

    # the last h elements
    for i in range(N-h, N):
        window.pop(0)
        outlist[i] = sum(window) / len(window)

    return outlist


# test cases for smoothing, including edge cases
def test_smooth():
    # Test case 1: h = 0, N = 3
    inlist = [1, 2, 3]
    h = 0
    outlist = smooth(inlist, h)
    expected = [1, 2, 3]
    assert outlist == expected, f"Failed test case 1"

    # Test case 2: h = 10, N = 4 (h >= N-1)
    inlist = [1.0, 2.0, 3.0, 4.0]
    h = 10
    outlist = smooth(inlist, h)
    expected = [2.5, 2.5, 2.5, 2.5]
    assert outlist == expected, f"Failed test case 2"

    # Test case 3: h = 3, N = 5 (h+1 < N < 2h)
    inlist = [1, 2, 3, 4, 5]
    h = 3
    outlist = smooth(inlist, h)
    assert outlist == [2.5, 3, 3, 3, 3.5], f"Failed test case 3"

    # Test case 4: h = 2, N = 4 (N = 2h)
    inlist = [1, 2, 3, 4]
    h = 2
    outlist = smooth(inlist, h)
    assert outlist == [2, 2.5, 2.5, 3], f"Failed test case 4"
    
    # Test case 5: h = 2, N = 10 (N > 2h)
    inlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    h = 2
    outlist = smooth(inlist, h)
    expected = [2, 2.5, 3, 4, 5, 6, 7, 8, 8.5, 9]
    assert outlist == expected, f"Failed test case 5"
    
    print("All tests passed")


test_smooth()
