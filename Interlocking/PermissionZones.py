#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import PermissionZone
from typing import List

class PermissionZones(object):
	def setPermissionZone(self, *aPermissionZone : PermissionZone*):
		self._permissionZone = aPermissionZone

	def getPermissionZone(self) -> PermissionZone*:
		return self._permissionZone

	def __init__(self):
		self._permissionZone : PermissionZone = None
		# @AssociationType Interlocking.PermissionZone*
		# @AssociationMultiplicity 1..*
		# """A set of track assets inside a station which can have different operating permissions (being controlled from a different controller) as the rest of the station"""

