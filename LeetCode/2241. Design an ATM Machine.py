import copy

class ATM:
    def __init__(self):
        # [denomination]: amount
        self.banknotes = {20:0, 50:0, 100:0, 200:0, 500:0} 
        self.denominations = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        # take the index, get count for current denomination, add to banknotes
        # print('deposit')
        # print(banknotesCount)
        # print(self.denominations)
        # depo_total = 0
        # print('old banknotes', self.banknotes)
        for idx in range(len(banknotesCount)):
            cur_count = banknotesCount[idx]
            # print('cur_count', cur_count)
            cur_denom = self.denominations[idx]
            # print('cur_denom', cur_denom)
            self.banknotes[cur_denom] += cur_count
            # depo_total += cur_count*cur_denom
        # print('deposit total', depo_total)
        # print('new banknotes', self.banknotes)
        # temp_total = 0
        # for key, value in self.banknotes.items():
        #     temp_total += key*value
        # print('new balance', temp_total)
        # print()

    def withdraw(self, amount: int) -> List[int]:
        # amount is alwasy extracted from the larger denomination 
        # no optimal pick up wanted 
        
        # corner case: amount smaller than 20 cannot be withdrawed
        if amount < 20:
            return [-1]

        # use a temp copy of the balance, if ok to withdraw, overwrite, if no, drop
        # banknotes_copy = self.banknotes
        banknotes_copy = copy.deepcopy(self.banknotes)
        denom_rev = list(reversed(self.denominations))
        for denom in denom_rev:
            if banknotes_copy[denom] <= 0:
                continue
            else:
                wanted_count = amount // denom # get quantity of wanted denom
                if banknotes_copy[denom] < wanted_count: # in sufficient denom for wanted 
                    wanted_count -= banknotes_copy[denom]
                    amount -= banknotes_copy[denom] * denom
                    banknotes_copy[denom] = 0
                else: # sufficient denom for current wanted
                    banknotes_copy[denom] -= wanted_count
                    amount -= wanted_count*denom
        # after the iteration, if amount is not 0, return [-1]
        if amount:
            return [-1]
        else:
        # if amount is 0, return the quantity for each denom
            diff_list = []
            for denom in banknotes_copy:
                diff_list.append(self.banknotes[denom] - banknotes_copy[denom])
            
            self.banknotes = banknotes_copy
            return diff_list

        
                    


