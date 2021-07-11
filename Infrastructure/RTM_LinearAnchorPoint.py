#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure.RTM import RTM_BaseObject
from typing import List

class RTM_LinearAnchorPoint(RTM_BaseObject):
	def __init__(self):
		self.___anchorName : str = None
		self.___measure : complex = None
		self.___measureToNext : complex = None

