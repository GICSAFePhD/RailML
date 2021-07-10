#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import tCrossedElementTypeExt
from Common import tRef
from Common import tElementWithIDandName
from typing import List

class CrossedElement(tElementWithIDandName):
	def setType(self, aType : tCrossedElementTypeExt):
		self.___type = aType

	def getType(self) -> tCrossedElementTypeExt:
		return self.___type

	def setRef(self, aRef : tRef):
		self.___ref = aRef

	def getRef(self) -> tRef:
		return self.___ref

	def __init__(self):
		self.___type : tCrossedElementTypeExt = None
		# @AssociationType Infrastructure.tCrossedElementTypeExt
		# """type of the element that is crossed by the over/under/level crossing"""
		self.___ref : tRef = None
		# @AssociationType Common.tRef
		# """reference to the ID of an element that is also part of the railway infrastructure. Use this attribute e.g. when your railway line is crossing itself (not on same level!)."""

