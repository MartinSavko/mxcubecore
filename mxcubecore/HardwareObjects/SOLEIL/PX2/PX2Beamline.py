# encoding: utf-8
#
#  Project name: MXCuBE
#  https://github.com/mxcube
#
#  This file is part of MXCuBE software.
#
#  MXCuBE is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  MXCuBE is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with MXCuBE. If not, see <http://www.gnu.org/licenses/>.

"""
This is a subclass of the Beamline class serving as singleton container for links to top-level HardwareObjects

The only thing we add is a thin layer of ability to communicate via a zmq based protocol (Majordomo)
"""

from speech import speech
from useful_routines import DEFAULT_BROKER_PORT

from mxcubecore.HardwareObjects.Beamline import Beamline

class PX2Beamline(Beamline, speech):

    def __init__(self, name):
        Beamline.__init__(self, name)
        speech.__init__(self, port=DEFAULT_BROKER_PORT, service="beamline", verbose=False)


