#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Infrastructure import CrossedElement
from RailML.Infrastructure import FunctionalInfrastructureEntity
from typing import List

class XCrossing(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def CrossedElement(self) -> CrossedElement:
		return self.___crossesElement
	@CrossedElement.setter
	def CrossedElement(self, aCrossedElement : CrossedElement):		#TODO *aCrossesElement
		self.___crossesElement = aCrossedElement

	def create_CrossedElement(self):
		if self.CrossedElement == None:
			self.CrossedElement = []
		self.CrossedElement.append(CrossedElement.CrossedElement())
	
	def __init__(self):
		super().__init__()
		self.___crossesElement : CrossedElement = None
		# @AssociationType Infrastructure.CrossedElement*
		# @AssociationMultiplicity 0..*