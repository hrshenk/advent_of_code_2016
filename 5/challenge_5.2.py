import md5
count = 0
i = 0
password = ['g', 'g', 'g', 'g','g', 'g', 'g', 'g']
while count < 8:
    string = "ffykfhsq" + str(i)
    m = md5.new(string)
    digest = m.hexdigest()
    if ( digest[0:5] == "00000" ) and ( digest[5].isdigit() ):
        index = int(digest[5])
        if ( index < 8 ) and ( password[index] == 'g' ): 
            password[ index ] = digest[6]
            count += 1
    i+=1
print password