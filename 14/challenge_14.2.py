import md5
import copy

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
            #we only consider the first run of 3
            if mult == 3:
                break
        i = j
    return trips
    
#body
salt = "cuanljph"
m = md5.new(salt)
candidates = {}
indices = []
key_count = 0
close = -1

while True:
    for i in xrange(100000):
        current = m.copy()
        current.update(str(i))
        s = current.hexdigest()
        for x in xrange(2016):
            h = md5.new(s)
            s = h.hexdigest()
        trips = get_multiples(s, 3)
        quints = get_multiples(s, 5)
        for key in quints:
            if candidates.has_key(key):
                for index in candidates[key]:
                        if i - index <= 1000:
                            indices.append( index )
                            key_count += 1
                            if key_count == 64:
                                close = i
                candidates[key] = []
            if close > 0 and i - close > 1000:
                indices = sorted(indices)
                print indices[63]
                quit()
        for key in trips:
            if candidates.has_key(key):
                candidates[key].append(i)
            else:
                candidates[key] = [i]