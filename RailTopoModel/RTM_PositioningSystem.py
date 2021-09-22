#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import IsValid
from RailML.RailTopoModel import RTM_NamedResource
from typing import List

class RTM_PositioningSystem(RTM_NamedResource.RTM_NamedResource):
	def __init__(self):
		self._isValid : IsValid = None
		# @AssociationType Infrastructure.RTM.RTM_Validity*
		# @AssociationMultiplicity 1..*

