from scipy import stats
from cactpot_y_total_analysis import scountdict as sd_y
from cactpot_total_analysis import scountdict as sd

#print(sd_y)

def chi_square(d1,d2):
    csum = 0
    df = len(d1.keys()) - 1
    for k in d1.keys():
        c1 = d1[k]
        c2 = d2[k]
        csum += (c1 - c2)**2 / (c1+c2)
        #print(c1)
        #print(c2)
        #print(csum)
    p_value = 1 - stats.chi2.cdf(csum , df)
    return p_value

print(chi_square(sd,sd_y))
