import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import time

from sphero_sdk import ObserverSpheroRvr
from sphero_sdk import InfraredCodes

rvr = ObserverSpheroRvr()


def main():
    """ This program has another robot capable of infrared communication, e.g. BOLT, follow RVR.

        To try this out, write a script for your other robot that has it follow on the corresponding channel
        that RVR broadcasts on [in this case channel 0 and 1].
        Place your other robot behind RVR and run its script.
        Upon running this program RVR drives forward and the other robot follows it.
    """
    rvr.wake()

    # Broadcast on channels 0 and 1. We specify the channels with the InfraredCodes enumeration
    near_code = InfraredCodes.zero
    far_code = InfraredCodes.one
    rvr.start_robot_to_robot_infrared_broadcasting(near_code.value, far_code.value)

    # Drive forward at speed 64 for two seconds
    rvr.raw_motors(1, 64, 1, 64)
    time.sleep(2)

    rvr.stop_robot_to_robot_infrared_broadcasting()

    rvr.close()


main()
