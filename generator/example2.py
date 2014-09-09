# Write a range replacement (adjrange, short for "adjustable range"),
# which can be prodded with .send() to change the step.
#
# This could be useful e.g. in a numerical integration routine, where
# we want to increase the step size in boring areas, and decrease in
# areas of high variability.

def adjrange(start, stop, step):
    """A range()/xrange() replacement with adjustable step.

    >>> x = adjrange(0, 7, 1)
    >>> next(g)
    0
    >>> next(g)
    1
    >>> g.send(2)
    >>> next(g)
    3
    >>> next(g)
    5
    >>> next(g)                              # doctest: +ELLIPSIS
    Traceback:
        ...
    StopIteration: ...
    """
    pos = start
    while pos < stop:
        new_step = yield pos
        if new_step is not None: step = new_step
        pos += step

if __name__=="__main__":
    
    gen = adjrange(1,7,1)
    print next(gen)
    print next(gen)
    print gen.send(2)
    print next(gen)

# Bonus: fix the function so that adjrange(stop) works
