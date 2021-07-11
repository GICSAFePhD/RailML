#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure.RTM import RTM_Validity
from Infrastructure.RTM import RTM_NamedResource
from typing import List

class RTM_PositioningSystem(RTM_NamedResource):
	def __init__(self):
		self._isValid : RTM_Validity = None
		# @AssociationType Infrastructure.RTM.RTM_Validity*
		# @AssociationMultiplicity 1..*

