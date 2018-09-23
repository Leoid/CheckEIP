#!/usr/bin/python

from pydbg import *
from pydbg.defines import *
import sys

def check(dbg):
    if dbg.dbg.u.Exception.dwFirstChance:
        return DBG_EXCEPTION_NOT_HANDLED
    print "Access Violation!"
    print "EIP: %0X"% dbg.Context.Eip

    return DBG_EXCEPTION_NOT_HANDLED

dbg = pydbg()

pid = int(sys.argv[1])

dbg.attach(pid)

dbg.set_callback(EXCEPTION_ACCESS_VIOLATION,check)

dbg.run()
