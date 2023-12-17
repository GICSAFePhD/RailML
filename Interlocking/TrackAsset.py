#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityIL
from typing import List

class TrackAsset(EntityIL.EntityIL):
	"""A track element (e.g. signal, switch, TVD section), as defined in the IL namespace that is controlled or read by interlocking systems."""

	def __init__(self):
		super().__init__()