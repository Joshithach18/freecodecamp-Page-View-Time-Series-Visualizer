# main.py

from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

def main():
    # Generate the line plot
    line_fig = draw_line_plot()
    line_fig.show()

    # Generate the bar plot
    bar_fig = draw_bar_plot()
    bar_fig.show()

    # Generate the box plot
    box_fig = draw_box_plot()
    box_fig.show()

# Import and run tests from test_module.py
if __name__ == "__main__":
    main()
    import test_module
    test_module.run_tests()
