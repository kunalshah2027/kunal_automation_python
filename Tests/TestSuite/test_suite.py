import unittest


from Tests.TestCase.test_normal import Test_all


class Testsuite:
    TC1 = unittest.TestLoader().loadTestsFromTestCase(Test_all)
    smokeTest = unittest.TestSuite([TC1])
    unittest.TextTestRunner(verbosity=2).run(smokeTest)


