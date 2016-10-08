#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch02_p67.py
#   Description : - Matching Geotagged Image
#   Author      : CHLEE / 2016. 8. 29 (월)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 02. Local Image Descriptors
#######################################################################

import pydot

g = pydot.Dot(graph_type='graph')
print "Pos 010 (g)=", g

g.add_node(pydot.Node(str(0), fontcolor='transparent'))
for i in range(5):
   g.add_node(pydot.Node(str(i+1)))
   g.add_edge(pydot.Edge(str(0), str(i+1)))
   for j in range(5):
      g.add_node(pydot.Node(str(j+1)+'-'+str(i+1)))
      g.add_edge(pydot.Edge(str(j+1)+'-'+str(i+1), str(j+1)))

print "Pos 020 (g)=", g

g.write_png('graph.jpg', prog='neato.bat')
