#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import IsValid
from RailML.RailTopoModel import RTM_NamedResource
from typing import List

class RTM_NetworkResource(RTM_NamedResource.RTM_NamedResource):
	@property
	def IsValid(self) -> IsValid:
		return self.___isValid

	@IsValid.setter
	def IsValid(self, aIsValid : IsValid):
		self.___isValid = aIsValid

	def __init__(self):
		super().__init__()
		self.___isValid : IsValid = None
		# @AssociationType Infrastructure.RTM.RTM_Validity*
		# @AssociationMultiplicity 0..*