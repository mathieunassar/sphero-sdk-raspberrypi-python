#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x16-driving.json
# Device ID:          0x16
# Device Name:        drive
# Timestamp:          08/14/2019 @ 17:33:23.067229 (UTC)

from enum import IntEnum


__all__ = ['RawMotorModesEnum',
           'StabilizationIndexesEnum',
           'DriveFlagsBitMask']


class CommandsEnum(IntEnum): 
    raw_motors = 0x01
    reset_yaw = 0x06
    drive_with_heading = 0x07
    set_stabilization = 0x0C


class RawMotorModesEnum(IntEnum):
    ''' '''
    off = 0  #: 
    forward = 1  #: 
    reverse = 2  #: 


class StabilizationIndexesEnum(IntEnum):
    ''' '''
    no_control_system = 0  #: 
    full_control_system = 1  #: 
    pitch_control_system = 2  #: 
    roll_control_system = 3  #: 
    yaw_control_system = 4  #: 
    speed_and_yaw_control_system = 5  #: 


class DriveFlagsBitMask(IntEnum):
    ''' '''
    drive_reverse = 1 #: 
    boost = 2 #: 
    fast_turn = 4 #: 
    left_direction = 8 #: 
    right_direction = 16 #: 
    enable_drift = 32 #: 
