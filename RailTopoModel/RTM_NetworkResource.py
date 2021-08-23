#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import Validity
from RailML.RailTopoModel import RTM_NamedResource
from typing import List

class RTM_NetworkResource(RTM_NamedResource.RTM_NamedResource):
	def __init__(self):
		self._isValid : Validity = None
		# @AssociationType Infrastructure.RTM.RTM_Validity*
		# @AssociationMultiplicity 0..*

