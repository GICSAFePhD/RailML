#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tGradientPerMille, tLengthM, any, anyAttribute
from RailML.Infrastructure import tNumberOfTracks
from typing import List

class LineLayout(object):
	@property
	def MaxGradient(self) -> tGradientPerMille:
		return self.___maxGradient
	@property
	def NumberOfTracks(self) -> tNumberOfTracks:
		return self.___numberOfTracks
	@property
	def MinRadius(self) -> tLengthM:
		return self.___minRadius
	@property
	def Unnamed_any(self) -> any:
		return self.___unnamed_any_
	@property
	def AnyAttribute(self) -> anyAttribute:
		return self.___rail3_anyAttribute

	@MaxGradient.setter
	def MaxGradient(self, aMaxGradient : tGradientPerMille):
		self.___maxGradient = aMaxGradient
	@NumberOfTracks.setter
	def NumberOfTracks(self, aNumberOfTracks : tNumberOfTracks):
		self.___numberOfTracks = aNumberOfTracks
	@MinRadius.setter
	def MinRadius(self, aMinRadius : tLengthM):
		self.___minRadius = aMinRadius
	@Unnamed_any.setter
	def Unnamed_any(self, aUnnamed_any : any):
		self.___unnamed_any_ = aUnnamed_any
	@AnyAttribute.setter
	def AnyAttribute(self, aAnyAttribute : anyAttribute):
		self.___rail3_anyAttribute = aAnyAttribute

	def __init__(self):
		self.___maxGradient : tGradientPerMille = tGradientPerMille.tGradientPerMille()
		# @AssociationType Common.tGradientPerMille
		# """maximum gradient in per million that occurs along the line (section)"""
		self.___numberOfTracks : tNumberOfTracks = tNumberOfTracks.tNumberOfTracks()
		# @AssociationType Infrastructure.tNumberOfTracks
		# """use this parameter to specify the line being a double or single (or mixed) track line"""
		self.___minRadius : tLengthM = tLengthM.tLengthM()
		# @AssociationType Common.tLengthM
		# """minimum horizontal curve radius that occurs along the line (section); in meters"""
		self.___unnamed_any_ : any = any.any()
		self.___rail3_anyAttribute : anyAttribute = anyAttribute.anyAttribute()
		"""# @AssociationKind Aggregation"""

