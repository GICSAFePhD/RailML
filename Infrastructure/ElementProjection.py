#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tRef import tRef
from RailML.Infrastructure.ElementProjectionSymbol import ElementProjectionSymbol
from RailML.Infrastructure.VisualizationBaseElement import VisualizationBaseElement
from typing import List

class ElementProjection(VisualizationBaseElement):
	@property
	def RefersToElement(self) -> tRef:
		return self.___refersToElement
	@property
	def UsesSymbol(self) -> ElementProjectionSymbol:
		return self.___usesSymbol

	@RefersToElement.setter
	def RefersToElement(self, aRefersToElement : tRef):
		self.___refersToElement = aRefersToElement
	@UsesSymbol.setter
	def UsesSymbol(self, aUsesSymbol : ElementProjectionSymbol):
		self.___usesSymbol = aUsesSymbol

	def create_UsesSymbol(self):
		if self.UsesSymbol == None:
			self.UsesSymbol = []
		self.UsesSymbol.append(ElementProjectionSymbol.ElementProjectionSymbol())

	def __init__(self):
		super().__init__()
		self.___refersToElement : tRef = None
		# @AssociationType Common.tRef
		# """reference to any element of infrastructure model"""
		self.___usesSymbol : ElementProjectionSymbol = None
		# @AssociationType Infrastructure.ElementProjectionSymbol
		# @AssociationMultiplicity 0..1
		# """use an (external) symbol for element projection"""

