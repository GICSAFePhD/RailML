#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tRef
from Infrastructure import ElementProjectionSymbol
from Infrastructure import VisualizationBaseElement
from typing import List

class ElementProjection(VisualizationBaseElement):
	def setRefersToElement(self, aRefersToElement : tRef):
		self.___refersToElement = aRefersToElement

	def getRefersToElement(self) -> tRef:
		return self.___refersToElement

	def setUsesSymbol(self, aUsesSymbol : ElementProjectionSymbol):
		self._usesSymbol = aUsesSymbol

	def getUsesSymbol(self) -> ElementProjectionSymbol:
		return self._usesSymbol

	def __init__(self):
		self.___refersToElement : tRef = None
		# @AssociationType Common.tRef
		# """reference to any element of infrastructure model"""
		self._usesSymbol : ElementProjectionSymbol = None
		# @AssociationType Infrastructure.ElementProjectionSymbol
		# @AssociationMultiplicity 0..1
		# """use an (external) symbol for element projection"""

