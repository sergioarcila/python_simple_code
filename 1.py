import sys

year_num = int(input("Number of Years:"))
start_year = int(input("Start Year(e.g 2012):"))
values = []
for i in range(year_num):
    val = float(input("Value of %s:" % (start_year + i)))
    values.append(val)

avg_change = 0
greatest_increase = -sys.maxsize
gi_year = start_year
smallest_increase = sys.maxsize
si_year = start_year
for i in range(len(values) - 1):
    change = values[i + 1] - values[i]
    avg_change += abs(change)
    if greatest_increase < change:
        greatest_increase = change
        gi_year = i + start_year
    if smallest_increase > change:
        smallest_increase = change
        ci_year = i + start_year
avg_change /= year_num

print('average change: %s' % avg_change)
print('greatest increase year: %s' % gi_year)
print('smallest increase year: %s' % ci_year)