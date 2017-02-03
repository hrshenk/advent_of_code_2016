import md5

def get_multiples(string, mult):
    i = 0; count = 0; l = len(string)
    trips = {}
    while i < l:
        j = i
        while(j < l and string[i] == string[j]):
            j += 1
        count = j - i
        if count >= mult:
            trips[ string[i] ] = count
            break
        i = j
    return trips

#body
salt = "cuanljph"
#salt = "abc"
m = md5.new(salt)
candidates = {}
indices = []
key_count = 0

while key_count < 65:
    for i in xrange(100000):
        current = m.copy()
        current.update(str(i))
        s = current.hexdigest()
        trips = get_multiples(s, 3)
        for key in trips:
            in_candidates = candidates.has_key(key)
            if trips[key] >= 5:
                if in_candidates:
                    for index in candidates[key]:
                        if 0 < i-index and i - index <= 1000:
                            indices.append( index )
                            key_count +=1
                            if key_count == 64:
                                print max(indices)
                                quit()
                    candidates[key].append(i)
                else:
                    candidates[key] = [i]
            elif in_candidates:
                candidates[key].append(i)
            else:
                candidates[key] = [i]
            
                
                            
                    
    
    
    



