def check_int_groove(D, d, L, H, R, database):
    lst = []
    #D = float(D)
    #d = float(d)
    #L = float(L)
    #H = float(H)
    #R = float(R)
    for i in database:
        if i.dmin <= d and \
                (D-d)/2 < i.ap and \
                (i.h -2*i.r) <= (H-2*R) and \
                i.h <= H and \
                i.r <= R and \
                L <= i.Lmax:
            dict_app = {
                "name": i.name,
                "dmin": i.dmin,
                "ap": i.ap,
                "h": i.h,
                "r": i.r,
                "Lmax": i.Lmax
            }
            lst.append(dict_app)
    return lst


def check_int_turning(D, d, L, a, database):
    lst = []
    #D = float(D)
    #d = float(d)
    #L = float(L)
    #a = float(a)
    for i in database:
        if i.dmin <= d and \
                (D - d) / 2 < i.ap and \
                a <= (180 - i.gugol - i.ugol -1) and \
                L <= i.Lmax:
            dict_app = {
                "name": i.name,
                "dmin": i.dmin,
                "ap": i.ap,
                "W": i.gugol,
                "Wp": i.ugol,
                "Lmax": i.Lmax
            }
            lst.append(dict_app)
    return lst


def check_name(name, database):
    check = 0
    for i in database:
        if name == i.name:
            check = 1
    return check


def password(password):
    check = 1
    if password == "spup":
        check = 0
    return check