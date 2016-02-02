#example file using as a python package
import os
import sys
#add two dirs up to path
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
import imgtrkr as it

it.AddTrkr('/home/nfs/z3457920/hdrive/repos/imgtrkr/examples/test.png',{'Created with':os.path.realpath(__file__)})
it.RdTrkr('/home/nfs/z3457920/hdrive/repos/imgtrkr/examples/test.png')
