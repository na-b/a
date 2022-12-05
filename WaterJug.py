from collections import defaultdict

jug1, jug2, aim = 14, 13, 12

visited = defaultdict(lambda: False)

def waterJugSolver(amt1, amt2):

	if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
		print(amt1, amt2)
		return True
	
	if visited[(amt1, amt2)] == False:
		print(amt1, amt2)
	
		visited[(amt1, amt2)] = True
	
		return (waterJugSolver(0, amt2) or
				waterJugSolver(amt1, 0) or
				waterJugSolver(jug1, amt2) or
				waterJugSolver(amt1, jug2) or
				waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
				amt2 - min(amt2, (jug1-amt1))) or
				waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
				amt2 + min(amt1, (jug2-amt2))))
	
	else:
		return False

print("Steps: ")

waterJugSolver(0, 0)

"""

OUTPUT
------
Steps: 
0 0
14 0
14 13
0 13
13 0
13 13
14 12
0 12
True

"""