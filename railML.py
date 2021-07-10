#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import Metadata
from Common import Common
from Infrastructure import Infrastructure
from Interlocking import Interlocking
import aRailML
from typing import List

class railML(object):
	"""This is the root element of any railML file."""
	def setMetadata(self, aMetadata : Metadata):
		self._metadata = aMetadata

	def getMetadata(self) -> Metadata:
		return self._metadata

	def setCommon(self, aCommon : Common):
		self._common = aCommon

	def getCommon(self) -> Common:
		return self._common

	def setInfrastructure(self, aInfrastructure : Infrastructure):
		self._infrastructure = aInfrastructure

	def getInfrastructure(self) -> Infrastructure:
		return self._infrastructure

	def setInterlocking(self, aInterlocking : Interlocking):
		self._interlocking = aInterlocking

	def getInterlocking(self) -> Interlocking:
		return self._interlocking

	def __init__(self):
		self._metadata : Metadata = None
		# @AssociationType Common.Metadata
		# @AssociationMultiplicity 0..1
		self._common : Common = None
		# @AssociationType Common.Common
		# @AssociationMultiplicity 0..1
		# """root element for railML3 common model"""
		self._infrastructure : Infrastructure = None
		# @AssociationType Infrastructure.Infrastructure
		# @AssociationMultiplicity 0..1
		# """root element for railML3 infrastructure model"""
		self._interlocking : Interlocking = None
		# @AssociationType Interlocking.Interlocking
		# @AssociationMultiplicity 0..1
		# """root element for railML3 interlocking model"""
		self.___rail3_aRailML : aRailML = None
		"""# @AssociationKind Aggregation"""

