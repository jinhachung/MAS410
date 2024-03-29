from sage.all import *

#set constants
b = 21577236633894971537484068161493580978653461635808456328375618690187518276081138501282108229232874098981279696875052990503212770147375832417942657945768472013223510732212984205314554702023734777911256482113397530288018858643494359567586715590455633690169776558375843276684491191865183639024623613651969546268016865218478410556174021428664088354344121886797962238951191605778606175337520607970360179901283329618222780991947
n = 22263514210712520678896029026451706214047551443436483450888733752500628518827986719734660037921858914063800561684284925959080925640133498895083348619227276408326410506074294384686074604900978207069634364219339175184356570717306471261478123128898931993631618011944520716971784806292775527116907126449150116148054106623396925576836059904689929084908942782635352970890076294437346757361258569765601796234625253524246779461813
b_over_n = continued_fraction(b/n)
i = 0
# loop over convergents of the continued fraction of b/n to find t/a
while True:
    i += 1
    t_over_a = b_over_n.convergent(i)
    t = t_over_a.numerator()
    a = t_over_a.denominator()
    if ((t > 2) and (gcd(a * b-1, t)== t)):
        print("found convergent with length of continued fraction: ", i)
        phi_n = (a * b - 1)/t
        # n = pq, phi(n) = (p-1)(q-1) = pq-(p+q)+1 --> p+q = (n+1) - phi(n)
        # p,q are roots of the equation x^2 - (p+q)x + pq = x^2 - [(n+1) - phi(n)]x + n
        p_plus_q = n + 1 - phi_n
        p_times_q = n
        # check if determinant is an integer
        det = p_plus_q * p_plus_q - 4 * p_times_q
        if ((det >= 0) and (sqrt(det) in QQ)):
            print("determinant checks out")
        else:
            print("... but determinant is invalid...")
            print("looking for other convergents...")
            continue
        # compute p and q
        p = (p_plus_q + sqrt(det)) / 2
        q = (p_plus_q - sqrt(det)) / 2
        # check if p*q == n
        if (p * q == n):
            print("p times q equals n... Wiener's Low Decryption Exponent Attack Succeeds!")
            print("private keys a, p, q are:")
            print(a)
            print(p)
            print(q)
            break
        else:
            print("... but p times q does not equal n... looking for other convergents")
            continue
