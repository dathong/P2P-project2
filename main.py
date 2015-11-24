import networkx as nx
import matplotlib.pyplot as plt
import json
import pjDrawGraph
import pjGraphType
import pjDiameter
import pjRepObj
import pjRdWalk
import pjKrandom
import pjGnutella
import util


n = 100
p = 0.04
popDense = 0.05


G = nx.erdos_renyi_graph(n,p)

print("a) Print the graph...")
util.drawGraph(G)

print("b) Graph type: ")
type = pjGraphType.graphConnectionType(G)

print("c) Diameter type: ")
diameter = pjDiameter.getDiameter(G,type)
print("diameter = ", diameter)

print("d)Replicas of objects:")


pjRepObj.placeReplicas(G,popDense,'object', 'A')
#pjDrawGraph.drawGraph1(G,'object','A')
pjRepObj.printReplicas(G,'object','A')

print("e)Search: ")
print("e-ii) Random Walk:")
pjRdWalk.randomwalk(G,1,'object','A')
pjRdWalk.rdWalkWithRep(G,1,'object','A')
pjRdWalk.biasedRandomWalk(G,1,'object','A')

print("e-ii) k-random Walk:")
pjKrandom.kRdWalk(3,G,1,'object','A')

print("e-i) Gnutella Flooding:")
print(pjGnutella.flooding(G,1,'object','A'))