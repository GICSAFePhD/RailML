#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tDerailingPosition
from Interlocking import MovableElement
from typing import List

class DerailerIL(MovableElement):
	"""The derailer or trap switch is an infrastructure element that either allows or disallows train passage. A derailer typically operates on one rail only; trap switch (points) have similar effect using both rails to literally derail the train for protection purpose. 
	Derailers that are locally and manually controlled are obviously not within the scope of an interlocking as the dispatcher will typically prevent trains from derailing by blocking signals leading towards such a device"""
	def setPreferredPosition(self, aPreferredPosition : tDerailingPosition):
		self.___preferredPosition = aPreferredPosition

	def getPreferredPosition(self) -> tDerailingPosition:
		return self.___preferredPosition

	def __init__(self):
		self.___preferredPosition : tDerailingPosition = None
		# @AssociationType Interlocking.tDerailingPosition
		# """This is the preferred position of the derailer which it is switched to when not in use."""

