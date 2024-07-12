
# your code here


# apuntes:
# age --> outliers -20 or 65+
# job --> 330 unknown
# marital --> 80 unkown, mostly married
# education --> 1730 unknown (4.2%) mostly university.degree and high.school
# default (IMBALANCE) --> 21% unkown, only 3 yes 
# housing --> 990 unknown, 52 yes 45 no
# loan (IMBALANCE) --> 990 unknown, 82% no
# contact --> relevant? 63 cellular, 37 telephone
# month (relevant?) --> missing jan/feb, most may, july, aug
# day_of_week (relevant?) --> very balanced, no weekends
# duration (relevant?) --> 258 mean, high std, outliers over 1000
# campaing(contactsmade)--> 69% under 3 contacts, 2.1% over 10
# pdays (delete) --> 96% is 999 days (overlimit)
# previous --> 97% under 2, more than 3-4 is outlier
# poutcome (IMBALANCE) --> nonexistant 86%, 3% sucess 10% failure
# emp.var.rate (quarterly)--> mean = 0.08 (max 1.4, min -3.4)
# cons.price.idx (monthly) --> okay
# cons.conf.idx (monthly) --> okay
# euribor3m (daily) --> okay
# number of employees (float?) --> min 4963, max 5228
# y (target) --> false 88.7%
