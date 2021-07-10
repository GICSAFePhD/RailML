#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from Interlocking import Overlap
from Interlocking import EntityIL
from typing import List

class AssetAndState(EntityIL):
	"""The interlocking extensively uses assets with a state for securing routes. The AssetAndState class is a generic tupel of (Asset, State). These tupels can be used by more than one interlocking system and are therefore not a child of the Interlocking class but of the class NetworkAssets. AssetAndState extends BaseObject in order to inherit an identifier. This base class must be extended and contain a reference to a track asset; signal, section, switch, etc. plus the given status of that element. Eg. (id=xy, switch_18A, left) or (id=yz, signal S19, proceed)."""
	__metaclass__ = ABCMeta
	@classmethod
	def setIsNegated(self, aIsNegated : long):
		self.___isNegated = aIsNegated

	@classmethod
	def getIsNegated(self) -> long:
		return self.___isNegated

	@classmethod
	def __init__(self):
		self.___isNegated : long = None
		"""The exclusion of a particular state, i.e. everything else that this one."""
		self._unnamed_Overlap_ : Overlap = None

