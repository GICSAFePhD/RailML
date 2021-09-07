#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import LocalOperationArea
from typing import List

class LocalOperationAreas(object):
	@property
	def LocalOperationArea(self) -> LocalOperationArea:
		return self.___gradientCurve
	
	@LocalOperationArea.setter
	def LocalOperationArea(self, *aLocalOperationArea : LocalOperationArea):
		self.___gradientCurve = aLocalOperationArea

	def create_LocalOperationArea(self):
		if self.LocalOperationArea == None:
			self.LocalOperationArea = []
		self.LocalOperationArea.append(LocalOperationArea.LocalOperationArea())

	def __init__(self):
		self.___localOperationArea : LocalOperationArea = None
		# @AssociationType Interlocking.LocalOperationArea*
		# @AssociationMultiplicity 1..*
		# """Area used for local shunting movements without routes. Movable elements within the area might be operated from onsite panels."""