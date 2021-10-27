import time
from pytest import mark


@mark.parallel
def test_results1():
    time.sleep(5)
    print('result 1 has completed')


@mark.parallel
def test_results2():
    time.sleep(5)
    print('result 2 has completed')


@mark.parallel
def test_results3():
    time.sleep(5)
    print('result 3 has completed')


@mark.parallel
def test_results4():
    time.sleep(5)
    print('result 4 has completed')
