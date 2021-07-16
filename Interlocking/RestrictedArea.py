#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.TrackAsset import TrackAsset
from typing import List

class RestrictedArea(TrackAsset):
	"""The Restricted Area (RA) is an area of the yard that the interlocking can set aside from normal operation. Railway personnel typically take local control of a RA and the interlocking detects switches and signal such that regular trains cannot enter the RA. Typical Restricted Areas are local shunting areas, working area or possession areas. Local workers take over control of the RA from the interlocking. The type of RA defines the extent of control, i.e. what the interlocking allows local workers to do. E.g. regulations may allow local route setting in a shunting area but not in a working zone. Track workers may be allowed to operate individual switches in a working zone but they cannot set routes. Therefore, the interlocking must be aware of the RA type. This type datatype is abstract so the user is forced to specialize it."""
	__metaclass__ = ABCMeta
	@classmethod
	def setIsLimitedBy(self, *aIsLimitedBy : EntityILref):
		self._isLimitedBy = aIsLimitedBy

	@classmethod
	def getIsLimitedBy(self) -> EntityILref:
		return self._isLimitedBy

	@classmethod
	def __init__(self):
		self._isLimitedBy : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..*
		# """Reference to any asset in network forming the restricted area limits"""

