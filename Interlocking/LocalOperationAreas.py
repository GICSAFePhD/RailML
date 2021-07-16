#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.LocalOperationArea import LocalOperationArea
from typing import List

class LocalOperationAreas(object):
	def setLocalOperationArea(self, *aLocalOperationArea : LocalOperationArea):
		self._localOperationArea = aLocalOperationArea

	def getLocalOperationArea(self) -> LocalOperationArea:
		return self._localOperationArea

	def __init__(self):
		self._localOperationArea : LocalOperationArea = None
		# @AssociationType Interlocking.LocalOperationArea*
		# @AssociationMultiplicity 1..*
		# """Area used for local shunting movements without routes. Movable elements within the area might be operated from onsite panels."""

