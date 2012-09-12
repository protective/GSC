import sys ,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import traci 

"""
	getGreenSpans(int, int) -> [[int,int],[int,int],...]

	returns the timeframes of green lights for the next intersection
"""
def _getGreenSpans(vhId, maxtime):
	return [[0,0],[0,0]]
"""
	getGreenSpans(int) -> int

	returns the recommented speed to reach the green light for next intersection
"""
def getRecommentedSpeed(vhId):
	print traci.vehicle.getLaneID("0")
	return 0

"""
	getNextTraficLight(string) > string

	returns the next intersection
"""
def _getNextTraficLight(vhId):
	raise NotImplementedError
"""
	getNextTraficLight(string) > string

	returns the next intersection
"""
def _getDistanceNextTraficLight(vhId):
	raise NotImplementedError

