#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tCrossedElementTypeExt
from RailML.Common import tElementWithIDandName
from RailML.Common import tRef
from typing import List

class CrossesElement(tElementWithIDandName.tElementWithIDandName):
	def setType(self, aType : tCrossedElementTypeExt):
		self.___type = aType

	def getType(self) -> tCrossedElementTypeExt:
		return self.___type

	def setRef(self, aRef : tRef):
		self.___ref = aRef

	def getRef(self) -> tRef:
		return self.___ref

	def __init__(self):
		super().__init__()
		self.___type : tCrossedElementTypeExt = None
		# @AssociationType Infrastructure.tCrossedElementTypeExt
		# """type of the element that is crossed by the over/under/level crossing"""
		self.___ref : tRef = None
		# @AssociationType Common.tRef
		# """reference to the ID of an element that is also part of the railway infrastructure. Use this attribute e.g. when your railway line is crossing itself (not on same level!)."""

