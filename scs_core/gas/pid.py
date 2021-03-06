"""
Created on 30 Sep 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

# import sys

from scs_core.gas.pid_calib import PIDCalib
from scs_core.gas.pid_datum import PIDDatum
from scs_core.gas.pid_temp_comp import PIDTempComp

from scs_core.gas.sensor import Sensor


# --------------------------------------------------------------------------------------------------------------------

class PID(Sensor):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def init(cls):
        cls.SENSORS[cls.CODE_VOC_PPB] = PID(cls.CODE_VOC_PPB,  'VOC',  4, 50, 30.0)
        cls.SENSORS[cls.CODE_VOC_PPM] = PID(cls.CODE_VOC_PPM,  'VOC',  4, 50, 0.300)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, sensor_code, gas_name, adc_gain_index, default_elc_mv, default_sens_mv):
        """
        Constructor
        """
        Sensor.__init__(self, sensor_code, gas_name, adc_gain_index)

        self.__default_elc_mv = default_elc_mv
        self.__default_sens_mv = default_sens_mv

        self.__tc = PIDTempComp.find(sensor_code)


    # ----------------------------------------------------------------------------------------------------------------

    def sample(self, afe, temp, sensor_index, no2_sample=None):
        we_v = afe.sample_raw_wrk(sensor_index, self.adc_gain_index)

        # print("PID.sample: %s" % self, file=sys.stderr)
        # print("-", file=sys.stderr)

        return PIDDatum.construct(self.calib, self.baseline, self.__tc, temp, we_v)


    def null_datum(self):
        return PIDDatum(None)


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def default_elc_mv(self):
        return self.__default_elc_mv


    @property
    def default_sens_mv(self):
        return self.__default_sens_mv


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def calib(self):
        return self.__calib


    @calib.setter
    def calib(self, calib):
        # replace missing values with defaults...
        pid_elc_mv = self.default_elc_mv if calib.pid_elc_mv is None else calib.pid_elc_mv
        pid_sens_mv = self.default_sens_mv if calib.pid_sens_mv is None else calib.pid_sens_mv

        # set calibration...
        self.__calib = PIDCalib(calib.serial_number, calib.sensor_type, pid_elc_mv, pid_sens_mv)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "PID:{sensor_code:%s, gas_name:%s, adc_gain_index:0x%04x, default_elc_mv:%s, default_sens_mv:%s, " \
               "calib:%s, baseline:%s}" %  \
               (self.sensor_code, self.gas_name, self.adc_gain_index, self.default_elc_mv, self.default_sens_mv,
                self.calib, self.baseline)
