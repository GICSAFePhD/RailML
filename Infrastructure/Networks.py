#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import Network
from typing import List

class Networks(object):
	@property
	def Network(self) -> Network:
		return self.___network
	
	@Network.setter
	def Network(self, aNetwork : Network):
		self.___network = aNetwork

	def create_Network(self):
		if self.Network == None:
			self.Network = []
		self.Network.append(Network.Network())

	def __init__(self):
		self.___network : Network = None
		# @AssociationType Infrastructure.Network*
		# @AssociationMultiplicity 1..*

