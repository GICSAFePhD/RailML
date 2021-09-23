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

	def create_Relation(self):
		if self.NetRelation == None:
			self.NetRelation = []
		self.NetRelation.append(NetRelation.NetRelation())

	def __init__(self):
		self.___netRelation : NetRelation = None
		# @AssociationType Infrastructure.NetRelation*
		# @AssociationMultiplicity 1..*	#TODO 1..*