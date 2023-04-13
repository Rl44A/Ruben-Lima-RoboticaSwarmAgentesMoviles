# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 20:55:30 2022

@author: lima1
"""
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)