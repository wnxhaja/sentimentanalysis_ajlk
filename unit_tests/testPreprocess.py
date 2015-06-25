import unittest

#execfile("../preprocess.py", globals())
class TestPreprocess(unittest.TestCase):

    def testPrintTweet(self):
        self.assertEqual('hello', 'hello')

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestPreprocess))
unittest.TextTestRunner(verbosity=2).run(suite)
