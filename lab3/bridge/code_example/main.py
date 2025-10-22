from code_example.implementors import CSVDataSource, APIDataSource, DatabaseDataSource
from code_example.abstractions import BarChart, PieChart, LineChart


if __name__ == "__main__":
    csv_data = CSVDataSource()
    api_data = APIDataSource()
    db_data = DatabaseDataSource()

    bar_chart = BarChart(csv_data)
    bar_chart.display()

    bar_chart.set_data_source(api_data)
    bar_chart.display()

    pie_chart = PieChart(api_data)
    pie_chart.display()

    line_chart = LineChart(db_data)
    line_chart.display()