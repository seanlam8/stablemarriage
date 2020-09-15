import sys
import utils
inFile = sys.argv[1]
preferences, people = utils.manipulate(inFile)
N = int(len(preferences) / 2)
def wPrefersM1OverM(prefer, w, m, m1): 
    for i in range(len(prefer[w])): 
        if (prefer[w][i] == m1): 
            return True
        if (prefer[w][i] == m): 
            return False

def stableMarriage(prefer):
    wPartner = [-1 for i in range(N)] 
    mFree = [False for i in range(N)] 
    freeCount = N 
    while (freeCount > 0): 
        m = 0
        while (m < N): 
            if (mFree[m] == False): 
                break
            m += 1
        i = 0
        while i < len(prefer[m]) and mFree[m] == False: 
            w = prefer[m][i] 
            if (wPartner[w - N] == -1): 
                wPartner[w - N] = m 
                mFree[m] = True
                freeCount -= 1
            else:  
                m1 = wPartner[w - N]
                if (wPrefersM1OverM(prefer, w, m, m1) == False): 
                    wPartner[w - N] = m 
                    mFree[m] = True
                    mFree[m1] = False
            i += 1    
    print("Woman ", " Man") 
    for i in range(N): 
        print(people[i + N], "\t", people[wPartner[i]]) 
  
stableMarriage(preferences)