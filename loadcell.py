class LoadCell:
    '''This is a loadcell class. The parameters of the loadcell are defined in this class as follow:
  sens --->> Sensitivity in mV/V .
  rateWeight --->> Rated weight in Kilograms. (i.e: Maximum weight a loadcell can weigh.)
  excitVolt --->> Excitation voltage in Volts. (i.e: The voltage reading at rated weight.)
Consequently there is derived parameter from the basic parameters above:
  rateWeightVoltage --->> Rated weight voltage in millivolts. (i.e: The voltage reading at rated weight.)
      rateWeightVoltage =  sens * excitVolt
'''
    def __init__(self,  sens,  rateWeight,  excitVolt):
        self.sens = sens
        self.rateWeight = rateWeight
        self.excitVolt = excitVolt
        self.rateWeightVoltage =  self.sens * self.excitVolt

    def getWeightFromVolt(self, measVolt):
        '''A method to get weight in Kilograms from measured value in millivolts.
measVolt --->> Measured value in millivolts.
'''
        return(measVolt * self.rateWeight / self.rateWeightVoltage)

    def getVoltFromWeight(self, weight):
        '''A method to get the calculated voltage in millivolts corresponding to expected or given weight in Kilograms.
'''
        return(self.rateWeightVoltage * weight/self.rateWeight)
