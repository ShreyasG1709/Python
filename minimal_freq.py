import sys
def frequency(l):
    minfreqlist = []
    maxfreqlist = []
    freq = {} 
    for item in l: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    sorted(freq.items(), key = lambda kv:(kv[1], kv[0]))
    minimum = min(freq.values())
    maximum = max(freq.values())
    for key,value in freq.items():
        if value == minimum:
            minfreqlist.append(key)
        elif value == maximum:
            maxfreqlist.append(key)
    
    

    sorted(minfreqlist)
    sorted(maxfreqlist)    
    if maxfreqlist==[]:
    	maxfreqlist=minfreqlist
    	return(minfreqlist,maxfreqlist)
    else:
    	return(minfreqlist,maxfreqlist)


frequency([13,12,11,13,14,13,7,11,13,14,12])
