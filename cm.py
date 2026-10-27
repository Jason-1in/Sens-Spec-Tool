#class for 2x2 table for sens and spec calculations 

"""helper function to check input is a fraction"""
def _check_fraction (value, name):
    if not 0 <= value <= 1:
        raise ValueError (f"{name} Must be between 0 and 1, got {value}")


class cMatrix ():
    """ 2 by 2 contingency table built from sensitivity, specificity and 
    prevalence, all three rates are in fractions between 0 and 1 """
    def __init__(self,sensitivity, specificity, prevalence, population = 1000):

    #Checks to ensure valid inputs
        _check_fraction(sensitivity, "Sensitivity")
        _check_fraction(specificity, "Specificity")
        _check_fraction(prevalence, "Prevalence")
        if population <= 0:
            raise ValueError(f"population must be positive, got {population}") #feature for later
        diseased = prevalence*population
        non_diseased = (1-prevalence) * population
        self.truePositive = sensitivity*diseased
        self.trueNegative = specificity*non_diseased 
        self.falsePositive = (1-specificity)*non_diseased
        self.falseNegative = (1-sensitivity)*diseased
        self.population = population

    def ppv(self):
        total = self.truePositive+self.falsePositive
        if total:
            return self.truePositive/(total)
        else:
            return float ("nan")

    def npv(self):
        total = self.trueNegative + self.falseNegative
        if total:
            return self.trueNegative/(total)
        else:
            return float ("nan")



