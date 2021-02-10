def mon_deco(fun):
    def wrap():
        print("decorator")
        fun()
    return wrap


@mon_deco
def deco():
    print('methode deco')


if __name__ == '__main__':
    deco()
