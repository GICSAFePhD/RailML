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

	def __init__(self):
		self.___network : Network = Network.Network()
		# @AssociationType Infrastructure.Network*
		# @AssociationMultiplicity 1..*	#TODO 1...*

