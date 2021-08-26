#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithIDref
from RailML.RailTopoModel import RTM_ElementPartCollection
from typing import List

class RTM_OrderedCollection(RTM_ElementPartCollection.RTM_ElementPartCollection):
	@property
	def Sequence(self) -> int:
		return self.___sequence
	@property
	def ElementPart(self) -> tElementWithIDref:
		return self.___elementPart
    
	@Sequence.setter
	def Sequence(self, aSequence : int):
		self.___sequence = aSequence
	@ElementPart.setter
	def ElementPart(self, aElementPart : tElementWithIDref):
		self.___elementPart = aElementPart

	def create_ElementPart(self):
		if self.ElementPart == None:
			self.ElementPart = []
		self.ElementPart.append(tElementWithIDref.tElementWithIDref())

	def __init__(self):
		self.___sequence : int = None
		self.___elementPart : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 1..*

