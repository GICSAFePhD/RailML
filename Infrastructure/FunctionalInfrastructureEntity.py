#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Common import Designator
from RailML.Common import External
from RailML.Infrastructure import EntityIS
from typing import List

class FunctionalInfrastructureEntity(EntityIS.EntityIS):
	@property
	def Designator(self) -> Designator:
		return self.___designator
	@property
	def External(self) -> External:
		return self.___external

	@Designator.setter
	def Designator(self, aDesignator : Designator):	#TODO *aDesignator
		self.___designator = aDesignator
	@External.setter
	def External(self, aExternal : External):		#TODO *aExternal
		self.___external = aExternal

	def create_Designator(self):
		if self.Designator == None:
			self.Designator = []
		self.Designator.append(Designator.Designator())
	def create_External(self):
		if self.External == None:
			self.External = []
		self.External.append(External.External())
    
	def __init__(self):
		super().__init__()
		self.___designator : Designator = None
		# @AssociationType Common.Designator*
		# @AssociationMultiplicity 0..*
		self.___external : External = None
		# @AssociationType Common.External*
		# @AssociationMultiplicity 0..*

