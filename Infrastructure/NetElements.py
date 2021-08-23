#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import NetElement
from typing import List

class NetElements(object):
	@property
	def NetElement(self) -> NetElement:
		return self.___netElement
	
	@NetElement.setter
	def NetElement(self, aNetElement : NetElement):
		self.___netElement = aNetElement

	def create_NetElement(self):
		if self.NetElement == None:
			self.NetElement = []
		self.NetElement.append(NetElement.NetElement())
    
	def __init__(self):
		self.___netElement : NetElement = None
		# @AssociationType Infrastructure.NetElement*
		# @AssociationMultiplicity 1..*	#TODO 1...*

