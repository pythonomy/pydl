#
#
#
def flegendre(x,m):
    import numpy as np
    from scipy.special import legendre
    if isinstance(x,np.ndarray):
        n = x.size
    else:
        n = 1
    if m < 1:
        raise ValueError('Order of Legendre polynomial must be at least 1.')
    leg = np.ones((m,n),dtype='d')
    if m >= 2:
        leg[1,:] = x
    if m >= 3:
        for k in range(2,m):
            leg[k,:] = np.polyval(legendre(k),x)
    return leg

