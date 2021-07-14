#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.RTM_LinearCoordinate import RTM_LinearCoordinate
from RailML.Infrastructure.RTM_GeometricCoordinate import RTM_GeometricCoordinate
from RailML.Infrastructure.RTM_BaseObject import RTM_BaseObject
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

