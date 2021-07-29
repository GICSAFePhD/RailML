#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tSpeedKmPerHour
from RailML.Infrastructure import tVMaxEnd

from typing import List

class tVMax(tVMaxEnd.tVMaxEnd, tSpeedKmPerHour.tSpeedKmPerHour):
	pass
