#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import MaxTrainCurrent
from typing import List, NewType
Long = NewType("Long", int)

class EnergyCatenary(object):
	@property
	def AllowsRegenerativeBraking(self) -> Long:
		return self.___allowsRegenerativeBraking
	@property
	def MaxTrainCurrent(self) -> MaxTrainCurrent:
		return self.___maxTrainCurrent

	@AllowsRegenerativeBraking.setter
	def AllowsRegenerativeBraking(self, aGradientCurve : Long):
		self.___allowsRegenerativeBraking = aGradientCurve
	@MaxTrainCurrent.setter
	def MaxTrainCurrent(self, aMaxTrainCurrent : MaxTrainCurrent):
		self.___maxTrainCurrent = aMaxTrainCurrent

	def __init__(self):
		self.___allowsRegenerativeBraking : Long = 0
		"""flag, whether the use of regenerative braking is allowed"""
		self.___maxTrainCurrent : MaxTrainCurrent = MaxTrainCurrent.MaxTrainCurrent()
		# @AssociationType Infrastructure.MaxTrainCurrent*
		# @AssociationMultiplicity 0..*
		# """maximum current that can be accessed in the described electrification section"""

