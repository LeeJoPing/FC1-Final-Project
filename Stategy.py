class Strategy:
    def __init__(self, debts, extraBudget):
        self.debts = debts
        self.extraBudget = extraBudget

    def chooseAllocation(self, debts, extraBudget):
        raise NotImplementedError("chooseAllocation function not implemented yet")


class SnowballStrategy(Strategy):
    def __init__(self, debts, extraBudget):
        super().__init__(self, debts, extraBudget)

    def chooseAllocation(self, debts, extraBudget):
        res = {}
        for d in debts:
            res[d.getName()] = 0
        
        sorted_debts = sorted(debts, key=lambda debt: (debt.balance, debt.id))
        
        while extraBudget > 0 and sorted_debts:
            d = sorted_debts[0]
            if d.balance > extraBudget:
                d.makePayment(extraBudget)
                res[d.getName()] = extraBudget
                extraBudget = 0

            else:
                extraBudget -= d.balance
                res[d.getName()] = d.balance
                d.makePayment(d.balance)
                sorted_debts.pop(0)

        return res 


class AvalancheStrategy(Strategy):
    def __init__(self, debts, extraBudget):
        super().__init__(self, debts, extraBudget)

    def chooseAllocation(self, debts, extraBudget):
        res = {}
        for d in debts:
            res[d.getName()] = 0
        
        sorted_debts = sorted(debts, key=lambda debt: (-debt.apr, debt.id))
        
        while extraBudget > 0 and sorted_debts:
            d = sorted_debts[0]
            if d.balance > extraBudget:
                d.makePayment(extraBudget)
                res[d.getName()] = extraBudget
                extraBudget = 0
            else:
                extraBudget -= d.balance
                res[d.getName()] = d.balance
                d.makePayment(d.balance)
                sorted_debts.pop(0)

        return res 