#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class tExtentOfControl(object):
	"""The Extent of Control is one of full control, steering only, notification only or none.
	Full control implies that the IL controls the element AND reads the element feedback to check the execution of the control. 
	Notification only means that the IL only reads the status of the object in terms of switch position left, controlled or boolean 1 or derailer engaged.
	Steering only means that the IL emits the control signal without checking for feedback.
	Note that LoC=none suggests that the IL has no relation at all with the track asset, indicating a modelling error that merits further investigation and/or explanation."""
	pass
