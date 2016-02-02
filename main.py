#!/usr/bin/env python 
#   Author: Christopher Bull. 
#   Affiliation: Climate Change Research Centre and ARC Centre of Excellence for Climate System Science.
#                Level 4, Mathews Building
#                University of New South Wales
#                Sydney, NSW, Australia, 2052
#   Contact: z3457920@student.unsw.edu.au
#   www:     christopherbull.com.au
#   Date created: Tue, 02 Feb 2016 16:02:13
#   Machine created on: ccrc165
#

#see: https://github.com/docopt/docopt
#round brackets mean required square are optional

#download docopt from...
#https://raw.githubusercontent.com/docopt/docopt/master/docopt.py

"""
Tiny python package to help save metadata to a file such that you know what script created the file!

Usage:
    main.py -h
    main.py PNGPATH...
Options:
    -h,--help          : show this help message
    PNGPATH            : path to pngfile(s) you want the metadata for
Examples:
    1] python main.py examples/test.png
    2] See examples/pyeg.py

"""
from PIL import Image
from PIL import PngImagePlugin
import os

class AddTrkr(object):
    """
    Class to add some image metadata too

    Parameters
    ----------
    pngpath: 
    metadata: 

    Returns
    -------
    
    Notes
    -------
    

    Example
    --------
    >>> import imgtrkr as it
    >>> it.AddTrkr('/home/nfs/z3457920/hdrive/repos/test.png',{'moogy':'sdfasdf'})
    """
    def __init__(self, pngpath,metadata):
        #super(AddTrkr, self).__init__()
        self.pngpath = pngpath 
        self.metadata = metadata 

        self.addmet()
        

    def addmet(self):
        """function that actually adds the metadata
        :returns: @todo
        """
    
        #f = "test.png"
        #METADATA = {"version":"1.0", "OP":"ihuston"}

        ## Create a sample image
        #import pylab as plt
        #import numpy as np
        #X = np.random.random((50,50))
        #plt.imshow(X)
        #plt.savefig(f)

        # Use PIL to save some image metadata

        im = Image.open(self.pngpath)
        meta = PngImagePlugin.PngInfo()

        for x in self.metadata:
            meta.add_text(x, self.metadata[x])
        im.save(self.pngpath, "png", pnginfo=meta)


class RdTrkr(object):
    """
    Class to add some image metadata too

    Parameters
    ----------
    pngpath: 
    metadata: 

    Returns
    -------
    
    Notes
    -------
    

    Example
    --------
    >>> import imgtrkr as it
    >>> it.RdTrkr('/home/nfs/z3457920/hdrive/repos/test.png')
    """
    def __init__(self, pngpath):
        self.pngpath = pngpath 
        im2 = Image.open(self.pngpath)
        #_lg.info(im2.info)
        # import pdb; pdb.set_trace()
        _lg.info("File: "+os.path.basename(self.pngpath)+" has metadata: "+str(im2.info))
        # print im2.info

if __name__ == "__main__": 
    from docopt import docopt
    arguments = docopt(__doc__)
    from _cblogger import _LogStart
    _lg=_LogStart().setup()
    #if using argpasser
    if len(arguments['PNGPATH'])==1:
        RdTrkr(arguments['PNGPATH'][0])
    elif len(arguments['PNGPATH'])>1:
        for pngp in arguments['PNGPATH']:
            RdTrkr(pngp)
else:
    from ._cblogger import _LogStart
    _lg=_LogStart().setup()

