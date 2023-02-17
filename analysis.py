rfile = open("rewards_output.txt","r")

rdata = rfile.readlines()

#print(rdata)

rlist = rdata[0].split(" ")

rlist = rlist[:2000]
#print(len(rlist))
#print(rlist)

rintlist = [int(i) for i in rlist]
print(sum(rintlist))

sum = 0
index = []
average = []
for i in range(2000):
    sum += rintlist[i]
    if (i+1) % 20 == 0:
        index.append(i+1)
        average.append(sum / (i+1))
