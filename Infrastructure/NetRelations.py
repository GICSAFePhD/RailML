#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import NetRelation
from typing import List

class NetRelations(object):
	@property
	def NetRelation(self) -> NetRelation:
		return self.___netRelation
	
	@NetRelation.setter
	def NetRelation(self, aNetRelation : NetRelation):
		self.___netRelation = aNetRelation

	def __init__(self):
		self.___netRelation : NetRelation = None#NetRelation.NetRelation()
		# @AssociationType Infrastructure.NetRelation*
		# @AssociationMultiplicity 1..*	#TODO 1..*

