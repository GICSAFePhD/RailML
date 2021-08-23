#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import RTM_BaseObject
from typing import List

class RTM_LinearAnchorPoint(RTM_BaseObject.RTM_BaseObject):
	@property
	def AnchorName(self) -> str:
		return self.___anchorName
	@property
	def Measure(self) -> complex:
		return self.___measure
	@property
	def MeasureToNext(self) -> complex:
		return self.___measureToNext

	@AnchorName.setter
	def AnchorName(self, aAnchorName : str):
		self.___anchorName = aAnchorName
	@Measure.setter
	def Measure(self, aMeasure : complex):
		self.___measure = aMeasure
	@MeasureToNext.setter
	def MeasureToNext(self, aMeasureToNext : complex):
		self.___measureToNext = aMeasureToNext

	def __init__(self):
		self.___anchorName : str = ""
		self.___measure : complex = 0
		self.___measureToNext : complex = 0

