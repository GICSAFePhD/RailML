#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tDerailingPosition, MovableElement
from typing import List

class DerailerIL(MovableElement.MovableElement):
	"""The derailer or trap switch is an infrastructure element that either allows or disallows train passage. A derailer typically operates on one rail only; trap switch (points) have similar effect using both rails to literally derail the train for protection purpose. 
	Derailers that are locally and manually controlled are obviously not within the scope of an interlocking as the dispatcher will typically prevent trains from derailing by blocking signals leading towards such a device"""
	@property
	def PreferredPosition(self) -> tDerailingPosition:
		return self.___preferredPosition
	
	@PreferredPosition.setter
	def PreferredPosition(self, aPreferredPosition : tDerailingPosition):
		self.___preferredPosition = aPreferredPosition

	def __init__(self):
		self.___preferredPosition : tDerailingPosition = tDerailingPosition.tDerailingPosition()
		# @AssociationType Interlocking.tDerailingPosition
		# """This is the preferred position of the derailer which it is switched to when not in use."""

