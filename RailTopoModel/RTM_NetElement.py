#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithIDref
from RailML.RailTopoModel import RTM_NetworkResource, Relation
from typing import List

class RTM_NetElement(RTM_NetworkResource.RTM_NetworkResource):
    
	@property
	def Relation(self) -> Relation:
		return self.___relation

	@Relation.setter
	def Relation(self, aRelation : Relation):
		self.___relation = aRelation

	def create_Relation(self):
		if self.Relation == None:
			self.Relation = []
		self.Relation.append(Relation.Relation())

	def __init__(self):
		super().__init__()
		self.___relation : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*

