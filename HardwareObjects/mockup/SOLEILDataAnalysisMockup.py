import logging
import gevent.event

from HardwareRepository.HardwareObjects import edna_test_data
from HardwareRepository.BaseHardwareObjects import HardwareObject
from HardwareRepository.HardwareObjects.abstract.AbstractDataAnalysis import (
    AbstractDataAnalysis
)

from HardwareRepository.HardwareObjects.XSDataMXCuBEv1_3 import XSDataResultMXCuBE



class SOLEILDataAnalysisMockup(
    AbstractDataAnalysis, HardwareObject
):
    def __init__(self, name):
        HardwareObject.__init__(self, name)
        self.processing_done_event = gevent.event.Event()

    def get_html_report(self, edna_result):
        html_report = "/home/blissadm/mxcube/extras/result.html"
        return html_report

    def execute_command(self, command_name, *args, **kwargs):
        wait = kwargs.get("wait", True)
        cmd_obj = self.get_command_object(command_name)
        return cmd_obj(*args, wait=wait)

    def get_beam_size(self):
        return (10, 5)

    def from_params(self, data_collection, char_params):
        return char_params

    def characterise(self, edna_input):
        msg = "Starting MOCKUP Analisys"
        logging.getLogger("queue_exec").info(msg)

        self.processing_done_event.set()
        self.result = XSDataResultMXCuBE.parseString(edna_test_data.EDNA_RESULT_DATA)

        return self.result

    def is_running(self):
        return not self.processing_done_event.is_set()
