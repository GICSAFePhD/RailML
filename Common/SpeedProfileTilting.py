#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tTiltingActuationType import tTiltingActuationType
from RailML.Common.tAngleDegQuadrant import tAngleDegQuadrant
from typing import List

class SpeedProfileTilting(object):
	def setActuation(self, aActuation : tTiltingActuationType):
		self.___actuation = aActuation

	def getActuation(self) -> tTiltingActuationType:
		return self.___actuation

	def setMaxTiltingAngle(self, aMaxTiltingAngle : tAngleDegQuadrant):
		self.___maxTiltingAngle = aMaxTiltingAngle

	def getMaxTiltingAngle(self) -> tAngleDegQuadrant:
		return self.___maxTiltingAngle

	def __init__(self):
		self.___actuation : tTiltingActuationType = None
		# @AssociationType Common.tTiltingActuationType
		self.___maxTiltingAngle : tAngleDegQuadrant = None
		# @AssociationType Common.tAngleDegQuadrant

