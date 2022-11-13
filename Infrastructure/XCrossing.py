#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Infrastructure import CrossesElement
from RailML.Infrastructure import FunctionalInfrastructureEntity
from typing import List

class XCrossing(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def CrossesElement(self) -> CrossesElement:
		return self.___crossesElement
	@CrossesElement.setter
	def CrossesElement(self, aCrossesElement : CrossesElement):		#TODO *aCrossesElement
		self.___crossesElement = aCrossesElement

	def create_CrossesElement(self):
		if self.CrossesElement == None:
			self.CrossesElement = []
		self.CrossesElement.append(CrossesElement.CrossesElement())
	
	def __init__(self):
		super().__init__()
		self.___crossesElement : CrossesElement = None
		# @AssociationType Infrastructure.CrossedElement*
		# @AssociationMultiplicity 0..*