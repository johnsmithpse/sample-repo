#!/usr/bin/env python

from itertools import islice
from math import isclose
from matplotlib.testing.decorators import image_comparison
from matplotlib.pyplot import plot, title
from numpy import arange

from sample import fib, collatz
from sample import average, tail, variance

def test_average():
    f = islice(fib(), 1, 10)
    assert isclose(average(f), 15.777, rel_tol=1e-3) 

def test_variance():
    f = range(10)
    assert isclose(variance(f), 8.25, rel_tol=1e-3) 


@image_comparison(baseline_images=['average'], extensions=['png'])
def test_plot_average():
    xs = arange(1, 100)
    ys = [average(range(x)) for x in xs]
    title('average(range(x))')
    plot(xs, ys)

if __name__ == '__main__':
    from logging import getLogger, basicConfig, INFO
    logger = getLogger(__name__)
    basicConfig(level=INFO)

    for test in [test_average, test_plot_average]:
        logger.info(f'Running {test}')
        test()
