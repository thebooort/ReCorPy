#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_reorder.py
@Time    :   2022/06/25 23:07:13
@Author  :   Bart Ortiz 
@Version :   1.0
@Contact :   bortiz@ugr.es
@License :   CC-BY-SA or GPL3
@Desc    :   None
"""

# std import
import pytest
import pandas as pd
import numpy as np
import sys

sys.path.append(".")


# local import
from recorpy.reorder import ReorderCorr


@pytest.fixture(scope="module")
def global_data():
    """global_data fixture

    Returns:
        pandas.Dataframe: define matrix for calculations
    """

    np.random.seed(1)
    df = pd.DataFrame(np.random.rand(3, 3))
    return df


class Test_Utils:
    def setUp(self):
        # Aquí, opcionalmente, ejecuta lo que deberías ejecutar antes
        # de comenzar cada test.
        pass

    def test_ReorderCorr(self, global_data):
        """Test for ReorderCorr module

        Args:
            global_data ():
        """

        ordered_matrix = ReorderCorr(
            global_data,
            corr_threshold=0.8,
            corr_method="pearson",
            order="chain",
            manual_order=None,
        )

        assert ordered_matrix.columns.tolist() == [0, 1, 2]
