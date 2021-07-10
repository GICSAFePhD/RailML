#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import NetElement
from typing import List

class NetElements(object):
	def setNetElement(self, *aNetElement : NetElement*):
		self._netElement = aNetElement

	def getNetElement(self) -> NetElement*:
		return self._netElement

	def __init__(self):
		self._netElement : NetElement = None
		# @AssociationType Infrastructure.NetElement*
		# @AssociationMultiplicity 1..*

