from generate_cactpot import tinput,tinput2,tinput3,tinput4,tinput5
from perfect_cactpot import play_board_Y

routlist = []
soutlist = []

for d in tinput:
    rs = d[0]
    s = d[1]
    rn = d[2]
    tf = d[3]
    #print(s,rs,rn,tf)
    rout, sout = play_board_Y(s, rs, rn, tf)
    routlist.append(rout)
    soutlist.append(sout)

#print(inputdata)

routfile = open("rewards_output_y.txt", "w")
for r in routlist:
    routfile.write(str(r) + " ")
routfile.close()

soutfile = open("sums_output_y.txt", "w")
for n in soutlist:
    soutfile.write(str(n) + " ")
soutfile.close()

routlist = []
soutlist = []

#print("made it past first tinput")

for d in tinput2:
    rs = d[0]
    s = d[1]
    rn = d[2]
    tf = d[3]
    #print(s,rs,rn,tf)
    rout, sout = play_board_Y(s, rs, rn, tf)
    routlist.append(rout)
    soutlist.append(sout)

#print(inputdata)

routfile = open("rewards_output_y2.txt", "w")
for r in routlist:
    routfile.write(str(r) + " ")
routfile.close()

soutfile = open("sums_output_y2.txt", "w")
for n in soutlist:
    soutfile.write(str(n) + " ")
soutfile.close()

routlist = []
soutlist = []

for d in tinput3:
    rs = d[0]
    s = d[1]
    rn = d[2]
    tf = d[3]
    #print(s,rs,rn,tf)
    rout, sout = play_board_Y(s, rs, rn, tf)
    routlist.append(rout)
    soutlist.append(sout)

#print(inputdata)

routfile = open("rewards_output_y3.txt", "w")
for r in routlist:
    routfile.write(str(r) + " ")
routfile.close()

soutfile = open("sums_output_y3.txt", "w")
for n in soutlist:
    soutfile.write(str(n) + " ")
soutfile.close()

routlist = []
soutlist = []

for d in tinput4:
    rs = d[0]
    s = d[1]
    rn = d[2]
    tf = d[3]
    #print(s,rs,rn,tf)
    rout, sout = play_board_Y(s, rs, rn, tf)
    routlist.append(rout)
    soutlist.append(sout)

#print(inputdata)

routfile = open("rewards_output_y4.txt", "w")
for r in routlist:
    routfile.write(str(r) + " ")
routfile.close()

soutfile = open("sums_output_y4.txt", "w")
for n in soutlist:
    soutfile.write(str(n) + " ")
soutfile.close()

routlist = []
soutlist = []

for d in tinput5:
    rs = d[0]
    s = d[1]
    rn = d[2]
    tf = d[3]
    #print(s,rs,rn,tf)
    rout, sout = play_board_Y(s, rs, rn, tf)
    routlist.append(rout)
    soutlist.append(sout)

#print(inputdata)

routfile = open("rewards_output_y5.txt", "w")
for r in routlist:
    routfile.write(str(r) + " ")
routfile.close()

soutfile = open("sums_output_y5.txt", "w")
for n in soutlist:
    soutfile.write(str(n) + " ")
soutfile.close()
