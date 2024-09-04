from typing import List

import numpy as np

from ._object_finder_base import ObjectFinderBase


class ObjectFinderMeasurementFilter(ObjectFinderBase):
    def __init__(self, img: np.ndarray,
                 boost_segmentation: bool = True,
                 **kwargs
                 ):
        super().__init__(img, boost_segmentation)
        self._max_eccentricity = kwargs.get("max_eccentricity", 0.85)

    def find_objects(self, threshold_method: str = "otsu",
                     measurements: str or List[str] = "basic",
                     **kwargs
                     ):
        super().find_objects(threshold_method=threshold_method,
                             measurements=measurements,
                             **kwargs)
        self.filter_objects()

    def filter_objects(self):
        self._eccentricity_filter()

    def _eccentricity_filter(self):
        self._table = self._table.loc[
                      self._table.loc[:, "eccentricity"] < self._max_eccentricity, :
                      ]
