#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   reorder.py
@Time    :   2022/06/24 10:41:13
@Author  :   Bart Ortiz 
@Version :   1.0
@Contact :   bortiz@ugr.es
@License :   CC-BY-SA or GPL3
@Desc    :   None
"""

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def ReorderCorr(
    df, corr_threshold=0.8, corr_method="pearson", order="chain", manual_order=None
):
    """ReorderCorr reorders the columns of a dataframe based on its correlation matrix
       to analyze clusters better. It is based on METHODS OF REORDERING THE
       CORRELATION MATRIX TO FACILITATE VISUAL INSPECTION AND PRELIMINARY CLUSTER ANALYSIS
       (1973) by John Edward Hunter and de corReorder package by David W. Gerbing
       (Portland State University; gerbing@pdx.edu)

    Args:
        df (pandas.DataFrame): Dataframe with data
        corr_threshold (float, optional): Correlation threshold to apply. Defaults to 0.8.
        corr_method (str, optional): Correlation method to apply. Defaults to 'pearson'.
        order (str, optional): Order to apply (manual, hclust,chain ). Defaults to 'chain'.
        manual_order (list, optional): List of columns to apply. Defaults to None.

    Returns:
        (pandas.DataFrame): reordered dataframe

    Example:
        >>> df = pd.DataFrame(np.random.rand(3,3))
        >>> ReorderCorr(df)

    """
    df_corr = df.corr(method=corr_method)
    columns = df.columns
    if order == "manual" and manual_order is not None:
        reordered_df = df.reindex(columns=manual_order)
    elif order == "manual" and manual_order is None:
        raise ValueError("manual_order is None and order is manual")
    if order == "chain":
        similarity_matrix = cosine_similarity(df_corr)
        new_order = [columns[0]]
        for i in range(0, len(columns) - 1):
            sim_section = similarity_matrix[new_order[i]]
            next_index = np.argmax(sim_section)
            while next_index in new_order:
                sim_section[next_index] = -1
                next_index = np.argmax(sim_section)
            # print(next_index)
            new_order.append(columns[next_index])
        reordered_df = df.reindex(columns=new_order)

    return reordered_df
