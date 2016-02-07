import matplotlib.pyplot as plt

plt.close('all')
fig=plt.figure()
ax=fig.add_subplot(1, 1,1)
ax.plot(range(10))
#fig.savefig('./.png',dpi=300)
#fig.savefig('./.pdf',format='pdf')
# plt.show()
#add two dirs up to path

import sys,os
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
import imgtrkr as it
it.AddTrkr('/home/chris/imgtrkr/examples/testtwo.png',{},cpath=os.path.realpath(__file__))

