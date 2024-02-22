"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time


class BinaryNumber:
  """ done """

  def __init__(self, n):
    self.decimal_val = n
    self.binary_vec = list('{0:b}'.format(n))

  def __repr__(self):
    return ('decimal=%d binary=%s' %
            (self.decimal_val, ''.join(self.binary_vec)))


## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.


def binary2int(binary_vec):
  if len(binary_vec) == 0:
    return BinaryNumber(0)
  return BinaryNumber(int(''.join(binary_vec), 2))


def split_number(vec):
  return (binary2int(vec[:len(vec) // 2]), binary2int(vec[len(vec) // 2:]))


def bit_shift(number, n):
  # append n 0s to this number's binary string
  return binary2int(number.binary_vec + ['0'] * n)




def pad(x, y):
  # pad with leading 0 if x/y have different number of bits
  # e.g., [1,0] vs [1]
  if len(x) < len(y):
    x = ['0'] * (len(y) - len(x)) + x
  elif len(y) < len(x):
    y = ['0'] * (len(x) - len(y)) + y
  # pad with leading 0 if not even number of bits
  if len(x) % 2 != 0:
    x = ['0'] + x
    y = ['0'] + y
  return x, y


def quadratic_multiply(x, y):
  # this just converts the result from a BinaryNumber to a regular int
  return _quadratic_multiply(x, y).decimal_val


def _quadratic_multiply(x, y):
  xvec = x.binary_vec
  yvec = y.binary_vec
  
  if x.decimal_val <= 1 and y.decimal_val <= 1:
    return BinaryNumber(x.decimal_val * y.decimal_val)

  else:
    xvec, yvec = pad(xvec, yvec)
    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)
    m1 = _quadratic_multiply(x_left, y_left)
    m1 = bit_shift(m1, len(xvec))
    m2 = _quadratic_multiply(x_left, y_right)
    m2 =bit_shift(m2, len(xvec)//2)
    m3 = _quadratic_multiply(x_right, y_left)
    m3 = bit_shift(m3, len(xvec)//2)
    m4 = _quadratic_multiply(x_right, y_right)
    

    return BinaryNumber(m1.decimal_val + m2.decimal_val + m3.decimal_val + m4.decimal_val)
 

#was told to comment out this portion by Professor Ding due to an error, but all code runs and returns the timing of the function, we added the timing under 8 in recitation-03.md
#  def test_quadratic_multiply(x, y, f):
 #   start = time.time()
    # multiply two numbers x, y using function f
#    f(x, y)
 #   return (time.time() - start) * 1000

#pass
#print(test_quadratic_multiply(BinaryNumber(20), BinaryNumber(20), quadratic_multiply))