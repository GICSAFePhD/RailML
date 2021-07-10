#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class tMustOrShould(object):
	"""Use this to distinguish hard or soft required states. E.g a called-for switch should be in the given position whilst a flank protection switch must be in the given position.
	The interlocking normally controls an element into a required position. The enforce-policy expresses what the interlocking must do with the element.
	enforce=must means that the condition is fulfilled only when the element acquires the given status, enforce=should means that this given status is the preferred status but no conditio sine qua non, finally enforce=none means that the interlocking is not given a desired status; in other words the IL can ignore the given status."""
	pass
