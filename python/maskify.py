# return masked string
def maskify(cc):
    l = len(cc)
    for i in range(l-4):
        cc = cc.replace(cc[i],'#')
    return cc

def maskify_simpler(cc):
    return "#"*(len(cc)-4) + cc[-4:]

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

cc = maskify("Whats up ya'll?")