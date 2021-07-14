#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.NetRelation import NetRelation
from typing import List

class NetRelations(object):
	def setNetRelation(self, aNetRelation : NetRelation):
		self._netRelation = aNetRelation

	def getNetRelation(self) -> NetRelation:
		return self._netRelation

	def __init__(self):
		self._netRelation : NetRelation = None
		# @AssociationType Infrastructure.NetRelation*
		# @AssociationMultiplicity 1..*

