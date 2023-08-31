import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_values = [1000, 1500, 1200, 1800, 2000, 1600]

def create_bar_plot(months, sales_values):
    plt.figure(figsize=(10, 6)) 

    plt.bar(months, sales_values)

    plt.title('Monthly Sales Data')
    plt.xlabel('Month')
    plt.ylabel('Sales Value')
    plt.grid(True)

    plt.show()

create_bar_plot(months, sales_values)
