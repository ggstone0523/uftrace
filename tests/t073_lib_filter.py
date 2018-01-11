#!/usr/bin/env python

from runtest import TestBase

class TestCase(TestBase):
    def __init__(self):
        TestBase.__init__(self, 'lib', """
# DURATION    TID     FUNCTION
            [17456] | lib_b() {
   6.911 us [17456] |   lib_c();
   8.279 us [17456] | } /* lib_b */
""", sort='simple')

    def build(self, name, cflags='', ldflags=''):
        if TestBase.build_libabc(self, cflags, ldflags) != 0:
            return TestBase.TEST_BUILD_FAIL
        return TestBase.build_libmain(self, name, 's-libmain.c',
                                      ['libabc_test_lib.so'])

    def runcmd(self):
        return '%s --force -F lib_b@libabc_test %s' % (TestBase.uftrace_cmd, 't-' + self.name)
