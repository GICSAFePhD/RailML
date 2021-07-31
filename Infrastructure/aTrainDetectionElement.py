#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tTrainDetectionElementType, tDetectedObject, tDetectorMedium, tDetectorLayout, TrainDetectionElement	#TODO CIRCULAR!
from typing import List

class aTrainDetectionElement(object):
	@property
	def tTrainDetectionElementType(self) -> tTrainDetectionElementType:
		return self.___type
	@property
	def tDetectedObject(self) -> tDetectedObject:
		return self.___detectedObject
	@property
	def tDetectorMedium(self) -> tDetectorMedium:
		return self.___detectorMedium
	@property
	def tDetectorLayout(self) -> tDetectorLayout:
		return self.___layout
	@property
	def Unnamed_TrainDetectionElement(self) -> TrainDetectionElement:
		return self.___unnamed_TrainDetectionElement

	@tTrainDetectionElementType.setter
	def tTrainDetectionElementType(self, atTrainDetectionElementType : tTrainDetectionElementType):
		self.___type = atTrainDetectionElementType
	@tDetectedObject.setter
	def tDetectedObject(self, atDetectedObject : tDetectedObject):
		self.___detectedObject = atDetectedObject
	@tDetectorMedium.setter
	def tDetectorMedium(self, atDetectorMedium : tDetectorMedium):
		self.___detectorMedium = atDetectorMedium
	@tDetectorLayout.setter
	def tDetectorLayout(self, atDetectorLayout : tDetectorLayout):
		self.___layout = atDetectorLayout
	@Unnamed_TrainDetectionElement.setter
	def Unnamed_TrainDetectionElement(self, aUnnamed_TrainDetectionElement : TrainDetectionElement):
		self.___unnamed_TrainDetectionElement = aUnnamed_TrainDetectionElement

	def __init__(self):
		self.___type : tTrainDetectionElementType = tTrainDetectionElementType.tTrainDetectionElementType()
		# @AssociationType Infrastructure.tTrainDetectionElementType
		# """type of train detector"""
		self.___detectedObject : tDetectedObject = tDetectedObject.tDetectedObject()
		# @AssociationType Infrastructure.tDetectedObject
		# """object (usually component of the railway vehicle) that is detected by the train detector"""
		self.___detectorMedium : tDetectorMedium = tDetectorMedium.tDetectorMedium()
		# @AssociationType Infrastructure.tDetectorMedium
		# """medium (physical principle) that is used for detection by the train detection element"""
		self.___layout : tDetectorLayout = tDetectorLayout.tDetectorLayout()
		# @AssociationType Infrastructure.tDetectorLayout
		# """constructional layout of the train detection element"""
		#self.___unnamed_TrainDetectionElement : TrainDetectionElement = None	#TODO CIRCULAR!

