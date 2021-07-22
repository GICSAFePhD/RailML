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

	def __init__(self):
		self.___derailerIS : DerailerIS = DerailerIS.DerailerIS()
		# @AssociationType Infrastructure.DerailerIS*
		# @AssociationMultiplicity 1..*

