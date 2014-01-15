'''
Created on Jan 14, 2014

@author: Sunhyung(Jason)
'''
from JCompareCore import JCompareCore

def doMain():
	srcPath = "Sample Source File Path"
	dstPath = "Sample Destination File Path"
	core = JCompareCore()
	
	f = open(srcPath, "r")
	while 1:
		line = f.readline()
		if not line: break
		core.addSourceLine(line)
	f.close()
	
	f = open(dstPath, "r")
	while 1:
		line = f.readline()
		if not line: break
		core.addDestinationLine(line)
	f.close()
	
	core.doCompare();
	for ce in core.compareResult:
		print "Source line : %d, Destination line : %d, Line count of same contents : %d" % (ce.srcStartIndex, ce.dstStartIndex, ce.lineCountOfSameContext)		

if __name__ == '__main__':
	doMain()
	pass
