#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure.RTM import RTM_LinearCoordinate
from Infrastructure.RTM import RTM_GeometricCoordinate
from Infrastructure.RTM import RTM_BaseObject
from typing import List

class RTM_IntrinsicCoordinate(RTM_BaseObject):
	def __init__(self):
		self.___intrinsicCoord : complex = None
		self._linearCoordinate : RTM_LinearCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_LinearCoordinate*
		# @AssociationMultiplicity 0..*
		self._geometricCoordinate : RTM_GeometricCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_GeometricCoordinate*
		# @AssociationMultiplicity 0..*

