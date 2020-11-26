from covid import Covid
import matplotlib.pyplot as pyplot

# country = input("Enter your country name: ")

covid = Covid()

cadr = {
    "confirmed": covid.get_total_confirmed_cases(),
    "active": covid.get_total_active_cases(),
    "deaths": covid.get_total_deaths(),
    "recovered": covid.get_total_recovered(),

}
n = list(cadr.keys())
v = list(cadr.values())
print(cadr)

# chart
pyplot.title("Corona Tracker Worldwide")
pyplot.bar(range(len(cadr)), v, tick_label=n)
pyplot.show()