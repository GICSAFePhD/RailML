#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import MaxTrainCurrent
from typing import List

class EnergyCatenary(object):
	def setAllowsRegenerativeBraking(self, aAllowsRegenerativeBraking : long):
		self.___allowsRegenerativeBraking = aAllowsRegenerativeBraking

	def getAllowsRegenerativeBraking(self) -> long:
		return self.___allowsRegenerativeBraking

	def setMaxTrainCurrent(self, *aMaxTrainCurrent : MaxTrainCurrent*):
		self._maxTrainCurrent = aMaxTrainCurrent

	def getMaxTrainCurrent(self) -> MaxTrainCurrent*:
		return self._maxTrainCurrent

	def __init__(self):
		self.___allowsRegenerativeBraking : long = None
		"""flag, whether the use of regenerative braking is allowed"""
		self._maxTrainCurrent : MaxTrainCurrent = None
		# @AssociationType Infrastructure.MaxTrainCurrent*
		# @AssociationMultiplicity 0..*
		# """maximum current that can be accessed in the described electrification section"""

