# test_module.py

import unittest
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

class TestTimeSeriesVisualizer(unittest.TestCase):
    def test_line_plot(self):
        """Test that the line plot function returns a Matplotlib figure."""
        fig = draw_line_plot()
        self.assertIsNotNone(fig)

    def test_bar_plot(self):
        """Test that the bar plot function returns a Matplotlib figure."""
        fig = draw_bar_plot()
        self.assertIsNotNone(fig)

    def test_box_plot(self):
        """Test that the box plot function returns a Matplotlib figure."""
        fig = draw_box_plot()
        self.assertIsNotNone(fig)

def run_tests():
    unittest.main(exit=False)
