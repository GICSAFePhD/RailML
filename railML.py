#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append('.')
from RailML.Common.Metadata import Metadata
from RailML.Common.Common import Common
#from RailML.Infrastructure import Infrastructure
#from RailML.Interlocking import Interlocking
#import aRailML
#from typing import List

class railML():
	"""This is the root element of any railML file."""
	@property
	def Metadata(self):
		return self.___metadata
	@property
	def Common(self):
		return self.___common

	@Metadata.setter
	def Metadata(self, aMetadata : Metadata):
		self.___metadata = aMetadata
	@Common.setter
	def Common(self, aCommon : Common):
		self.___common = aCommon

	#def setCommon(self, aCommon : Common):
	#	self._common = aCommon

	#def getCommon(self) -> Common:
	#	return self._common

	# def setInfrastructure(self, aInfrastructure : Infrastructure):
	# 	self._infrastructure = aInfrastructure

	# def getInfrastructure(self) -> Infrastructure:
	# 	return self._infrastructure

	# def setInterlocking(self, aInterlocking : Interlocking):
	# 	self._interlocking = aInterlocking

	# def getInterlocking(self) -> Interlocking:
	# 	return self._interlocking

	def __init__(self):
		self.___metadata : Metadata = None
		# @AssociationType Common.Metadata
		# @AssociationMultiplicity 0..1
		self.___common : Common = None
		# @AssociationType Common.Common
		# @AssociationMultiplicity 0..1
		# """root element for railML3 common model"""
		#self._infrastructure : Infrastructure = None
		# @AssociationType Infrastructure.Infrastructure
		# @AssociationMultiplicity 0..1
		# """root element for railML3 infrastructure model"""
		#self._interlocking : Interlocking = None
		# @AssociationType Interlocking.Interlocking
		# @AssociationMultiplicity 0..1
		# """root element for railML3 interlocking model"""
		#self.___rail3_aRailML : aRailML = None
		"""# @AssociationKind Aggregation"""


RML = railML()
metadata = Metadata()
common = Common()

RML.Metadata = metadata
RML.Common = common