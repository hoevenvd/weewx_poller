#
#    Copyright (c) 2012 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#
#    $Revision: 792 $
#    $Author: tkeffer $
#    $Date: 2013-01-03 13:53:58 -0800 (Thu, 03 Jan 2013) $
#
"""Abstract base class for station hardware."""

class AbstractStation(object):
    """Station drivers should inherit from this class."""    

    @property
    def hardware_name(self):
        raise NotImplementedError("Property 'hardware_name' not implemented")
    
    @property
    def archive_interval(self):
        raise NotImplementedError("Property 'archive_interval' not implemented")
    
    def genLoopPackets(self):
        raise NotImplementedError("Method 'genLoopPackets' not implemented")
    
    def genArchiveRecords(self, lastgood_ts):
        raise NotImplementedError("Method 'genArchiveRecords' not implemented")
        
    def getTime(self):
        raise NotImplementedError("Method 'getTime' not implemented")
    
    def setTime(self, newtime_ts):
        raise NotImplementedError("Method 'setTime' not implemented")
    
    def closePort(self):
        pass
