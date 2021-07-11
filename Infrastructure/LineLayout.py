#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tGradientPerMille, tLengthM, any, anyAttribute
from RailML.Infrastructure import tNumberOfTracks
from typing import List

class LineLayout(object):
	def setMaxGradient(self, aMaxGradient : tGradientPerMille):
		self.___maxGradient = aMaxGradient

	def getMaxGradient(self) -> tGradientPerMille:
		return self.___maxGradient

	def setNumberOfTracks(self, aNumberOfTracks : tNumberOfTracks):
		self.___numberOfTracks = aNumberOfTracks

	def getNumberOfTracks(self) -> tNumberOfTracks:
		return self.___numberOfTracks

	def setMinRadius(self, aMinRadius : tLengthM):
		self.___minRadius = aMinRadius

	def getMinRadius(self) -> tLengthM:
		return self.___minRadius

	def __init__(self):
		self.___maxGradient : tGradientPerMille = None
		# @AssociationType Common.tGradientPerMille
		# """maximum gradient in per million that occurs along the line (section)"""
		self.___numberOfTracks : tNumberOfTracks = None
		# @AssociationType Infrastructure.tNumberOfTracks
		# """use this parameter to specify the line being a double or single (or mixed) track line"""
		self.___minRadius : tLengthM = None
		# @AssociationType Common.tLengthM
		# """minimum horizontal curve radius that occurs along the line (section); in meters"""
		self._unnamed_any_ : any = None
		self.___rail3_anyAttribute : anyAttribute = None
		"""# @AssociationKind Aggregation"""

