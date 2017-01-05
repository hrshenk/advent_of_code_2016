import md5
count = 0
i = 0
password = ""
while count < 8:
    string = "abc"+ str(i)
    m = md5.new(string)
    digest = m.hexdigest()
    if ( digest[0:5] == "00000" ):
        password += digest[5]
        count += 1
    i+=1
print password