#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tSpeed
from typing import List

class tSpeedKmPerHour(tSpeed.tSpeed):
	"""generic type for speed/velocity values measured in kilometres per hour"""
	def __init__(self):
		super().__init__()
