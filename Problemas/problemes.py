# -*- coding: utf-8  -*-

import math
from numpy import *


def R(angle):
	
	a = array([(math.cos(angle), - math.sin(angle)), (math.sin(angle), math.cos(angle))])
	return a


#per al segon:

def Homo(**kwargs):
	
	if 'rot' in kwargs:	
		rot1 = kwargs['rot']
	else:
		rot1 = array([[1, 0],
			     [0, 1]])

	if 'desp' in kwargs:	
		desp1 = kwargs['desp']	
	else:
		desp1 = array([[0], [0]])

	rot = vstack((rot1, [0, 0]))
	desp = vstack((desp1, [1]))
	
	return hstack((rot, desp))

######
#rot1 = array([[1, 2], [3, 4]])
#desp1 = array([[9], [8]])
#Homo(rot=rot1, desp=desp1)

# per al tercer:


def Inv(homo):

	invrot = homo[:2, :2].transpose()
	invdesp = dot(invrot * -1, (homo[:2,2, newaxis]))
	return Homo(rot=invrot, desp=invdesp)


	

	
