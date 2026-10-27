#class for 2x2 table for sens and spec calculations 

class cMatrix ():

    def __init__(self,sensitivity, specificity, prevalence, population = 100):
        diseased = prevalence*population
        non_diseased = (1-prevalence) * population
        self.truePositive = sensitivity*diseased
        self.trueNegative = specificity*non_diseased 
        self.falsePositive = (1-specificity)*non_diseased
        self.falseNegative = (1-sensitivity)*diseased

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

#"nan" will resolve as false

"""
def calculate_intermediates (prevalence, population = 100, sensitivity, specificity):
    diseased = population * prevalence
    non_diseased = population * (1-prevalence)
    truePositive = sensitivity*diseased
    trueNegative = specificity*non_diseased 
    falsePositive = (1-specificity)*non_diseased
    falseNegative = (1-sensitivity)*diseased

def calculate_PPV (truePositive, falsePositive):
    totalPositives = truePositive + falsePositive
    return truePositive/totalPositives

def calculcate_NPV (trueNegative,falseNegative):
    totalNegatives = trueNegative + falseNegative
    return trueNegative/totalNegatives
"""