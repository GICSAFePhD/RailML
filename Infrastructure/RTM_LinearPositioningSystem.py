#!/usr/bin/python
# -*- coding: UTF-8 -*-
from schemas.3.1 import tLrsMethod
from Infrastructure.RTM import RTM_LinearAnchorPoint
from Infrastructure.RTM import RTM_PositioningSystem
from typing import List

class RTM_LinearPositioningSystem(RTM_PositioningSystem):
	def __init__(self):
		self.___linearReferencingMethod : tLrsMethod = None
		# @AssociationType schemas.3.1.tLrsMethod
		self.___startMeasure : complex = None
		self.___endMeasure : complex = None
		self.___units : str = None
		"""use SI units (e.g. metres) whenever possible"""
		self._anchor : RTM_LinearAnchorPoint = None
		# @AssociationType Infrastructure.RTM.RTM_LinearAnchorPoint*
		# @AssociationMultiplicity 0..*

