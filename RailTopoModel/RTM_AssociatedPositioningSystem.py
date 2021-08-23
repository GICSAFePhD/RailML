#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef
from RailML.RailTopoModel import RTM_IntrinsicCoordinate, RTM_BaseObject
from RailML.Infrastructure import Validity
from typing import List

class RTM_AssociatedPositioningSystem(RTM_BaseObject.RTM_BaseObject):
	def __init__(self):
		self.___positioningSystemRef : tRef = None
		# @AssociationType Common.tRef
		self._intrinsicCoordinate : RTM_IntrinsicCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_IntrinsicCoordinate*
		# @AssociationMultiplicity 1..*
		self._isValid : Validity = None
		# @AssociationType Infrastructure.RTM.RTM_Validity*
		# @AssociationMultiplicity 0..*

