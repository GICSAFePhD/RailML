#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import RTM_PositioningSystem
from typing import List

class GeometricPositioningSystem(RTM_PositioningSystem.RTM_PositioningSystem):
	def __init__(self):
		self.___crsDefinition : str = ""

