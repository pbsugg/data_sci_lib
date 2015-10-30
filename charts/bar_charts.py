from matplotlib import pyplot as bar_chart
from collections import Counter

grades = [55,75,90,91,33,47,83,77,22,55,33]
# break into deciles using this lambda function
decile = lambda grade: grade // 10 * 10
# Counter
histogram = Counter(decile(grade) for grade in grades)

# elements to plot the histogram
bar_chart.bar([x - 4 for x in histogram.keys()],
        histogram.values(),
        8)


bar_chart.axis([-5, 105 ,0 ,5])    # first values x axis, next two y

bar_chart.xticks([10 * i for i in range(11)])
bar_chart.xlabel("Decile")
bar_chart.ylabel("Number of students")
bar_chart.title("Distribution")
bar_chart.show()
