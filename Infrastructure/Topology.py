#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.NetElements import NetElements
from RailML.Infrastructure.NetRelations import NetRelations
from RailML.Infrastructure.Networks import Networks
from typing import List

class Topology(object):
	"""This is the top level element for railML3 topology model."""
	
	@property
	def NetElements(self) -> NetElements:
		return self.___netElements
	@property
	def NetRelations(self) -> NetRelations:
		return self.___netRelations
	@property
	def Networks(self) -> Networks:
		return self.___networks

	@NetElements.setter
	def NetElements(self, aNetElements : NetElements):
		self.___netElements = aNetElements
	@NetRelations.setter
	def NetRelations(self, aNetRelations : NetRelations):
		self.___netRelations = aNetRelations
	@Networks.setter
	def Networks(self, aNetworks : Networks):
		self.___networks = aNetworks

	def __init__(self):
		self.___netElements : NetElements = None
		# @AssociationType Infrastructure.NetElements
		# @AssociationMultiplicity 1
		# """container element for all netElement elements"""
		self.___netRelations : NetRelations =None
		# @AssociationType Infrastructure.NetRelations
		# @AssociationMultiplicity 0..1	#TODO 0...1
		# """container element for all netRelation elements"""
		self.___networks : Networks = None
		# @AssociationType Infrastructure.Networks
		# @AssociationMultiplicity 1
		# """container element for all network elements"""

