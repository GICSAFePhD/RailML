#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import Validity
from RailML.RailTopoModel import RTM_NamedResource
from typing import List

class RTM_NetworkResource(RTM_NamedResource.RTM_NamedResource):
	@property
	def IsValid(self) -> Validity:
		return self.___isValid

	@IsValid.setter
	def IsValid(self, aIsValid : Validity):
		self.___isValid = aIsValid

	def __init__(self):
		super().__init__()
		self.___isValid : Validity = None
		# @AssociationType Infrastructure.RTM.RTM_Validity*
		# @AssociationMultiplicity 0..*

