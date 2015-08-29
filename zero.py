# -*- coding: UTF-8 -*-
from optparse import OptionParser
from cvxopt.base import matrix, mul, sin, cos
from numpy import linspace
import sys
import matplotlib.pyplot as pyplot


class base():
    """base class for functions"""
    
    def __init__(self):
        self.params = {}
        self.n = 0
    
    def setup(self):
        for key in self.params.keys():
            self.__dict__[key] = []
    
    def list2matrix(self):
        for key in self.params.keys():
            self.__dict__[key] = matrix(self.__dict__[key], (self.n, 1), 'd')
    
    def add(self, **kwargs):
        self.n += 1
        keys = self.params.keys()
        
        for key in keys:
            self.__dict__[key].append(self.params[key])
        
        for key, val in kwargs.iteritems():
            if not key in keys: continue
            self.__dict__[key][-1] = val
    
    def fcall(self, x):
        return 0
    
    def dfcall(self, x):
        return 0
        
class poly(base):
    """polynomial class"""
        
    def __init__(self):
        base.__init__(self)
        self.params = {'a':0.0, 'b':0.0, 'c':0.0}
        self.setup()
        
    def fcall(self, x):
        fvec = self.c + x*(self.b + x*self.a)
        return sum(fvec)
        
    def dfcall(self, x):
        dfvec = self.b + 2.0*x*self.a
        return sum(dfvec)
        
class sine(base):
    """sine function class"""
    def __init__(self):
        base.__init__(self)
        self.params = {'A':0.0, 'omega':0.0, 'phi':0.0}
        self.setup()
        
    def fcall(self, x):
        fvec = mul(self.A, sin(self.omega*x + self.phi))
        return sum(fvec)
        
    def dfcall(self, x):
        dfvec = mul(mul(self.A, self.omega),
        cos(self.omega*x + self.phi))
        return sum(dfvec)

class function():
    """interface for all specific function classes"""
    def __init__(self, flist):
        self.flist = flist
        for item in self.flist:
            self.__dict__[item] = eval(item + '()')
    
    def setup(self):
        for item in self.flist:
            if self.__dict__[item].n:
                self.__dict__[item].list2matrix()
                
    def fcall(self, x):
        f = 0
        for item in self.flist:
            if self.__dict__[item].n:
                f += self.__dict__[item].fcall(x)
        return f
        
    def dfcall(self, x):
        df = 0
        for item in self.flist:
            if self.__dict__[item].n:
                df += self.__dict__[item].dfcall(x)
        return df
        
flist = ['poly', 'sine']
Function = function(flist)

def run(datafile, x0=0.0, plot=True, imax=20, tol=1e-5):
    """initialize function and run appropriate routines"""
    
    if not datafile:
        print '* Error: A data file must be defined!'
        print '* Type "dome -h" for help.'
        sys.exit(1)
    
    read(datafile)
    Function.setup()
    solve(x0, imax, tol)
    if plot: fplot(x0)

def read(datafile):
    """parse input data in plain text format"""
    
    fid = open(datafile, 'rt')
    for line in fid:
        data = line.split()
        if not len(data): continue
        if data[0] == 'Poly':
            Function.poly.add(a = float(data[1]),
                                b = float(data[2]),
                                c = float(data[3]))
        elif data[0] == 'Sine':
            Function.sine.add(A = float(data[1]),
                                omega = float(data[2]),
                                phi = float(data[3]))
    fid.close()

def solve(x0 = 0.0, imax = 20, tol = 1e-5):
    """simple Newton's method"""
    
    f = 1.0
    iteration = 0
    x = x0
    
    while abs(f) > tol:
        if iteration > imax: break
        f = Function.fcall(x)
        df = Function.dfcall(x)
        inc = f/df
        print 'Convergence error: %.8f' % inc
        x -= inc
        iteration += 1
    if iteration <= imax:
        print 'The solution is x = %.5f' % x
    else:
        print 'Reached maximum number of iterations'
        
def fplot(x0):
    """plot f(x) in the neighborhood of the initial guess"""
    # build x and f vectors
    points = 200
    xmin = x0 - 5.0
    xmax = x0 + 5.0
    xvec = linspace(xmin, xmax, num = points, endpoint = True)
    fvec = matrix(0, (points, 1), 'd')
    for item, x in enumerate(xvec):
        fvec[item] = Function.fcall(x)
    
    # graphical commands
    fig = pyplot.figure()
    pyplot.hold(True)
    pyplot.plot(xvec, fvec, 'k')
    pyplot.axhline(linestyle = ':', color = 'k')
    pyplot.axvline(linestyle = ':', color = 'k')
    pyplot.xlabel('$x$')
    pyplot.ylabel('$f(x)$')
    pyplot.savefig('zeroplot.eps', format='eps')
    pyplot.show()
    
def main():
    """parse settings and launch solver"""
    
    parser = OptionParser(version=' ')
    parser.add_option('-x', '--x0', dest='x0',
                        default=0.0, help='Initial guess')
    parser.add_option('-p', '--plot', dest='plot',
                        action='store_true', default=False,
                        help='Plot f(x) around x0.')
    parser.add_option('-n', '--iterations', dest='imax',
                        help='Maximum number of iterations.',
                        default=20)
    parser.add_option('-t', '--tolerance', dest='tol',
                        help='Convergence tolerance.',
                        default=1e-5)
    
    options, args = parser.parse_args(sys.argv[1:])
    
#    print sys.argv[1:]
#    print options, args
    
    datafile = args[0]
    
    run(datafile,
        x0 = float(options.x0),
        plot = options.plot,
        imax = int(options.imax),
        tol = float(options.tol))

# command line usage
if __name__ == "__main__": main()