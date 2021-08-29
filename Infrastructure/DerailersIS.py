#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import DerailerIS
from typing import List

class DerailersIS(object):
	@property
	def DerailerIS(self) -> DerailerIS:
		return self.___derailerIS
	
	@DerailerIS.setter
	def DerailerIS(self, aDerailerIS : DerailerIS):
		self.___derailerIS = aDerailerIS

	def create_DerailerIS(self):
		if self.DerailerIS == None:
			self.DerailerIS = []
		self.DerailerIS.append(DerailerIS.DerailerIS())

	def __init__(self):
		self.___derailerIS : DerailerIS = None
		# @AssociationType Infrastructure.DerailerIS*
		# @AssociationMultiplicity 1..*

