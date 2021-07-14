#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.Network import Network
from typing import List

class Networks(object):
	def setNetwork(self, aNetwork : Network):
		self._network = aNetwork

	def getNetwork(self) -> Network:
		return self._network

	def __init__(self):
		self._network : Network = None
		# @AssociationType Infrastructure.Network*
		# @AssociationMultiplicity 1..*

