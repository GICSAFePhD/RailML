#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tTiltingActuationType, tAngleDegQuadrant
from typing import List

class SpeedProfileTilting(object):
	@property
	def tTiltingActuationType(self) -> tTiltingActuationType:
		return self.___actuation
	@property
	def tAngleDegQuadrant(self) -> tAngleDegQuadrant:
		return self.___maxTiltingAngle

	@tTiltingActuationType.setter
	def tTiltingActuationType(self, atTiltingActuationType : tTiltingActuationType):
		self.___actuation = atTiltingActuationType
	@tAngleDegQuadrant.setter
	def tAngleDegQuadrant(self, atAngleDegQuadrant : tAngleDegQuadrant):
		self.___maxTiltingAngle = atAngleDegQuadrant

	def __init__(self):
		self.___actuation : tTiltingActuationType = tTiltingActuationType.tTiltingActuationType()
		# @AssociationType Common.tTiltingActuationType
		self.___maxTiltingAngle : tAngleDegQuadrant = tAngleDegQuadrant.tAngleDegQuadrant()
		# @AssociationType Common.tAngleDegQuadrant

