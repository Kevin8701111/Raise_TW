import chartify
import pandas as pd

csvfile = '/home/kevin/py3invm/ChartifyK/raiseKK.csv'

data = pd.read_csv(csvfile, sep = ',')
print(data.head(9))

chart = chartify.Chart(x_axis_type = 'log')

chart.set_title('raise')
chart.set_subtitle('tickets & year')
chart.axes.set_xaxis_label('year')
chart.axes.set_yaxis_label('tickets')
chart.set_source_label('KK')

# chart.axes.set_yaxis_range(0, 4500000)

chart.plot.line(data_frame = data, x_column = 'age', y_column = 'tickets', color_column = 'from')
#line , scatter , area , bar_stacked , heatmap , lollipop
#stacked = True可堆疊顯示(area)
chart.set_legend_location('outside_bottom')
#移動分類圖例至下方

chart.show()