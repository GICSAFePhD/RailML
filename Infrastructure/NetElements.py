#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.NetElement import NetElement
from typing import List

class NetElements(object):
	@property
	def NetElement(self) -> NetElement:
		return self.___netElement
	
	@NetElement.setter
	def Topology(self, aNetElement : NetElement):
		self.___netElement = aNetElement

	def __init__(self):
		self.___netElement : NetElement = NetElement()
		# @AssociationType Infrastructure.NetElement*
		# @AssociationMultiplicity 1..*	#TODO 1...*

