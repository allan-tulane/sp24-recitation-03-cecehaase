from main import *

## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(4)) == 3*4
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(3)) == 4*3
