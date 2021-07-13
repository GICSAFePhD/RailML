#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.RTM_PositioningSystem import RTM_PositioningSystem
from typing import List

class RTM_GeometricPositioningSystem(RTM_PositioningSystem):
	def __init__(self):
		self.___crsDefinition : str = None

