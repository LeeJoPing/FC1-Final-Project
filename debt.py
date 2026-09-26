class Debt:
    id = 0
    def __init__(self, name, balance, apr):
        self.name = name
        self.balance = balance
        self.apr = apr
        self.id = Debt.id 
        Debt.id += 1

    def getName(self):
        return self.name

    def getBalance(self):
        return self.balance

    def getAPR(self):
        return self.apr

    def getID(self):
        return self.id

    def getMonthlyRate(self):
        return self.apr/ 12

    def accrueInterest(self):
        self.balance *= (1+self.getMonthlyRate())

    def makePayment(self, amount):
        self.balance = max(self.balance - amount, 0)

    def isPaidOff(self):
        return self.balance == 0

    def getMinPayment():
        raise NotImplementedError("getminpayment function not implemented yet")



    
