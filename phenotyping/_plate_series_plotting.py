import matplotlib.pyplot as plt

from ._plate_series_change_over_time import PlateSeriesChangeOverTime

# TODO: Add module logging

class PlateSeriesPlotting(PlateSeriesChangeOverTime):
    def plot_plate_unfiltered(self, plate_idx, fontsize=34):
        fig, ax = self.plates[plate_idx].plot_unfiltered()
        fig.suptitle(f"{self.sample_name}_plate({plate_idx})", fontsize=fontsize)
        return fig, ax

    def plot_plate_analysis(self, plate_idx, fontsize=34):
        fig, ax = self.plates[plate_idx].plot_analysis()
        fig.suptitle(f"{self.sample_name}_plate({plate_idx})", fontsize=fontsize)
        return fig, ax

    def plot_plate_segmentation(self, plate_idx, figsize=(18, 10)):
        fig, ax = self.plates[plate_idx].plot_analysis_segmentation(
            figsize=figsize
        )
        return fig, ax

    def plot_plate_colony_segmentation(self, plate_idx, figsize=(18, 10)):
        fig, ax = self.plates[plate_idx].plot_colony_segmentation(
            figsize=figsize
        )
        return fig, ax


