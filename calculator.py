

initialDate = []
initialDate = input("enter the starting date [dd-mm-yyyy]").split("-")
print(initialDate)
finalDate = []
finalDate = input("enter the final date [dd-mm-yyyy]").split("-")
print(finalDate)
det = []
det = input("enter amount-rate").split("-")

initialMonth = int(initialDate[1])
finalMonth = int(finalDate[1])
month = initialMonth

initialYear = int(initialDate[2])
finalYear = int(finalDate[2])
year = initialYear

# print(7-


# print(2020-2022)
amount = int(det[0])
rateOfIntrest = int(det[1])


# initial
def findingMonths():
    noOfMonths = 12 - initialMonth
    noOfYear = (finalYear - initialYear) - 1
    noOfMonths = noOfMonths + (noOfYear * 12)
    noOfMonths = noOfMonths + finalMonth
    # print(noOfMonths)
    return noOfMonths

months = findingMonths()
class intrest:

    # first year

    def simpleIntrest(self,months,amount,rateOfIntrest):
        self.months = months
        self.amount = amount
        self.rateOfIntrest = rateOfIntrest

        si = (amount * months * rateOfIntrest) / 100
        print(f"months = {months} and rate of intrest = {rateOfIntrest} and final amount = {si}")
        return si

avi = intrest.simpleIntrest(months,amount,rateOfIntrest);
# print(intrest.findingMonths())
print(avi)
