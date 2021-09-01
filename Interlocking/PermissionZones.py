#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import PermissionZone
from typing import List

class PermissionZones(object):
	@property
	def PermissionZone(self) -> PermissionZone:
		return self.___permissionZone
	
	@PermissionZone.setter
	def PermissionZone(self, *aPermissionZone : PermissionZone):
		self.___permissionZone = aPermissionZone

	def __init__(self):
		self.___permissionZone : PermissionZone = None
		# @AssociationType Interlocking.PermissionZone*
		# @AssociationMultiplicity 1..*
		# """A set of track assets inside a station which can have different operating permissions (being controlled from a different controller) as the rest of the station"""