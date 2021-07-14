#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tRef import tRef
from RailML.Infrastructure.RTM_IntrinsicCoordinate import RTM_IntrinsicCoordinate
from RailML.Infrastructure.RTM_Validity import RTM_Validity
from RailML.Infrastructure.RTM_BaseObject import RTM_BaseObject
from typing import List

class RTM_AssociatedPositioningSystem(RTM_BaseObject):
	def __init__(self):
		self.___positioningSystemRef : tRef = None
		# @AssociationType Common.tRef
		self._intrinsicCoordinate : RTM_IntrinsicCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_IntrinsicCoordinate*
		# @AssociationMultiplicity 1..*
		self._isValid : RTM_Validity = None
		# @AssociationType Infrastructure.RTM.RTM_Validity*
		# @AssociationMultiplicity 0..*

