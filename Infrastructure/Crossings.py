#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import Crossing
from typing import List

class Crossings(object):
	@property
	def Crossing(self) -> Crossing:
		return self.___crossing
	
	@Crossing.setter
	def Crossing(self, aCrossing : Crossing):
		self.___crossing = aCrossing

	def __init__(self):
		self.___crossing : Crossing = Crossing.Crossing()
		# @AssociationType Infrastructure.Crossing*
		# @AssociationMultiplicity 1..*

