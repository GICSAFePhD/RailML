#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class TimeStamp(object):
	def setAt(self, aAt : dateTime):
		self.___at = aAt

	def getAt(self) -> dateTime:
		return self.___at

	def __init__(self):
		self.___at : dateTime = None

