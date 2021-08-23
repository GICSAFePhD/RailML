#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.Validity import Validity
from RailML.Infrastructure.RTM_NamedResource import RTM_NamedResource
from typing import List

class RTM_PositioningSystem(RTM_NamedResource):
	def __init__(self):
		self._isValid : Validity = None
		# @AssociationType Infrastructure.RTM.RTM_Validity*
		# @AssociationMultiplicity 1..*

