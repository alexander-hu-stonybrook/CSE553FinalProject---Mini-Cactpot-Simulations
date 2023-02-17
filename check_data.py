sfile = open("sums_output_y2.txt","r")
sdata = sfile.readlines()
slist = sdata[0].split(" ")

slist = slist[:2000]
print(len(rlist))
print(rlist)

sintlist = [int(i) for i in slist]

rfile = open("rewards_output_y2.txt","r")
rdata = rfile.readlines()

rlist = rdata[0].split(" ")
rlist = rlist[:3000]
#print(len(rlist))
#print(rlist)
rintlist = [int(i) for i in rlist]

sum = 0
index = []
average = []
for i in range(len(rintlist)):
    sum += rintlist[i]
    if (i+1) % 20 == 0:
        index.append(i+1)
        average.append(sum / (i+1))
