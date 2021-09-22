#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import RTM_NamedResource, RTM_PositioningSystem
from RailML.Common import Name
from RailML.Infrastructure import IsValid
from typing import List

class GeometricPositioningSystem(RTM_PositioningSystem.RTM_PositioningSystem):

	def __init__(self):
		super().__init__()