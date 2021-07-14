#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.NetElements import NetElements
from RailML.Infrastructure.NetRelations import NetRelations
from RailML.Infrastructure.Networks import Networks
from typing import List

class Topology(object):
	"""This is the top level element for railML3 topology model."""
	def setNetElements(self, aNetElements : NetElements):
		self._netElements = aNetElements

	def getNetElements(self) -> NetElements:
		return self._netElements

	def setNetRelations(self, aNetRelations : NetRelations):
		self._netRelations = aNetRelations

	def getNetRelations(self) -> NetRelations:
		return self._netRelations

	def setNetworks(self, aNetworks : Networks):
		self._networks = aNetworks

	def getNetworks(self) -> Networks:
		return self._networks

	def __init__(self):
		self._netElements : NetElements = None
		# @AssociationType Infrastructure.NetElements
		# @AssociationMultiplicity 1
		# """container element for all netElement elements"""
		self._netRelations : NetRelations = None
		# @AssociationType Infrastructure.NetRelations
		# @AssociationMultiplicity 0..1
		# """container element for all netRelation elements"""
		self._networks : Networks = None
		# @AssociationType Infrastructure.Networks
		# @AssociationMultiplicity 1
		# """container element for all network elements"""

