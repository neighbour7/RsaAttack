import gmpy2
from Crypto.Util.number import long_to_bytes

c = 2044619806634581710230401748541393297937319
n = 92164540447138944597127069158431585971338721360079328713704210939368383094265948407248342716209676429509660101179587761913570951794712775006017595393099131542462929920832865544705879355440749903797967940767833598657143883346150948256232023103001435628434505839331854097791025034667912357133996133877280328143
e = 3
def RsaLowE(e,n,c):
    i = 0
    while True:
        m = gmpy2.iroot(c+i*n,e)

        if m[1]:
            print(m[0])
            return m[0]
        else:
            i += 1
m = RsaLowE(e,n,c)

mm = long_to_bytes(m)
print(mm)






