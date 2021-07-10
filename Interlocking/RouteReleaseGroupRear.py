#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import PartialRoute
from typing import List

class RouteReleaseGroupRear(PartialRoute):
	"""Ordered set of TVD sections in rear of the train.
	Partial route, i.e. a set of TVD sections in rear of the train that is released as a group if given safety conditions are fulfilled. Partial route release can be delayed to improve safety. Route release groups can be associated with several routes.
	Release can be retarded by a given delay.
	If a route that has one single route release group then the route is released as a whole. In this case, there is no need to explicitly define the TVD sections that are part of this release group."""
	pass
