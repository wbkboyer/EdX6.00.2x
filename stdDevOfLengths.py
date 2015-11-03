__author__ = 'wbkboyer'

import unittest

def stdDevOfLengths(L):
    if not L:
        return float('NaN')
    else:
        mean = float(sum([len(x) for x in L]))/len(L)
        return (float(sum([(len(x)-mean)**2 for x in L]))/len(L))**0.5
        #return float("{0:.4f}".format((float(sum([(len(x)-mean)**2 for x in L]))/len(L))**0.5))

# class stdDevTest(unittest.TestCase):
#
#     # def testCase0(self):
#     #     self.assertEqual(stdDevOfLengths([]), float('NaN'))
#
#     def testCase1(self):
#         self.assertEqual(stdDevOfLengths(['a', 'z', 'p']), 0.0)
#
#     def testCase2(self):
#         self.assertEqual(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']), 1.8708)


if __name__ == '__main__':
    unittest.main()