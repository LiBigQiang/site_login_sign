import sys


def logging(func):
    def wrapper(*args, **kwargs):
        system = sys.platform
        if 'win' in system:
            path = r'F:/pyapp/log/{}.log'.format(sys.argv[0][:-3].split('/')[-1])
        else:
            path = r'/home/pi/pyapp/log/{}.log'.format(sys.argv[0][:-3].split('/')[-1])
        with open(path, 'a') as fp:
            sys.stdout = fp
            func(*args, **kwargs)
    return wrapper
