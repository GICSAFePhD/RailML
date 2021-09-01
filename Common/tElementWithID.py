#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Common import tID
from typing import List

class tElementWithID(object):
	@property
	def ID(self) -> tID:
		return self.___id

	@ID.setter
	def ID(self, aID : tID):
		self.___id = aID

	def __init__(self):
		self.___id : tID = None
		# @AssociationType Common.tID
		# """unique identifier"""