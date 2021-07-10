#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import OpOperation
from typing import List

class OpOperations(object):
	def setOpOperation(self, *aOpOperation : OpOperation*):
		self._opOperation = aOpOperation

	def getOpOperation(self) -> OpOperation*:
		return self._opOperation

	def __init__(self):
		self._opOperation : OpOperation = None
		# @AssociationType Infrastructure.OpOperation*
		# @AssociationMultiplicity 1..*
		# """railway operation"""

