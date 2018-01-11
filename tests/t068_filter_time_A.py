#!/usr/bin/env python

from runtest import TestBase

class TestCase(TestBase):
    def __init__(self):
        TestBase.__init__(self, 'sleep', result="""
# DURATION    TID     FUNCTION
            [23157] | main() {
            [23157] |   foo() {
            [23157] |     bar() {
   2.093 ms [23157] |       usleep(2000);
   2.095 ms [23157] |     } /* bar */
   2.106 ms [23157] |   } /* foo */
   2.107 ms [23157] | } /* main */
""")

    def build(self, name, cflags='', ldflags=''):
        # cygprof doesn't support return value now
        if cflags.find('-finstrument-functions') >= 0:
            return TestBase.TEST_SKIP

        return TestBase.build(self, name, cflags, ldflags)

    def runcmd(self):
        return '%s -t 1ms -R mem_alloc@retval -A mem_free@arg1 -A usleep@plt,arg1 %s' % \
            (TestBase.uftrace_cmd, 't-' + self.name)
