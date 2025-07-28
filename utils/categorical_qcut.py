import pandas as pd
from typing import Tuple, Dict

## Categorical Terciles and Quartiles
# How to Form Terciles from Categorical Data

# If your categorical data has a natural order (ordinal data), you can divide it into terciles—three groups each containing approximately one-third of the observations—by following these steps:
# 1. List the Categories in Order
# Arrange your categories from lowest to highest based on their natural order.
# 2. Count Observations in Each Category
# Determine the number of observations in each category.
# 3. Calculate Cumulative Percentages
# For each category, calculate the cumulative percentage of observations up to and including that category.
# 4. Assign Tercile Groups:
# The first tercile includes categories up to the point where the cumulative percentage reaches or exceeds 33.3%.
# The second tercile includes categories up to the point where the cumulative percentage reaches or exceeds 66.7%.
# The third tercile includes the remaining categories.
# 6. A single Tercile muct never exceed 50% of the sample. If a Tercile exceeds 50% of the sample then it needs to be split up for the price of the Cumulative percentage being lower than 33.3% per Tercile.

# How to Form Quartiles from Categorical Data

# If your categorical data has a natural order (ordinal data), you can divide it into quartiles—three groups each containing approximately one-third of the observations—by following these steps:
# 1. List the Categories in Order
# Arrange your categories from lowest to highest based on their natural order.
# 2. Count Observations in Each Category
# Determine the number of observations in each category.
# 3. Calculate Cumulative Percentages
# For each category, calculate the cumulative percentage of observations up to and including that category.
# 4. Assign Quartile Groups:
# The first quartile includes categories up to the point where the cumulative percentage reaches or exceeds 25%.
# The second quartile includes categories up to the point where the cumulative percentage reaches or exceeds 50%.
# The third quartile includes categories up to the point where the cumulative percentage reaches or exceeds 75%.
# The fourth quartile includes the remaining categories.
# 6. A single Quartile muct never exceed 50% of the sample. If a Quartile exceeds 50% of the sample then it needs to be split up for the price of the Cumulative percentage being lower than 33.3% per Quartile.

def categorical_qcut(data: pd.Series, qcut: int = 4) -> Tuple[pd.Series, Dict]:
    categories = data.value_counts(normalize = True).sort_index()
    if len(categories) < qcut:
        raise ValueError("Not enough unique categories to divide into requested quantiles.")

    quantile_threshold = float(1/qcut)
    quantile_max = float(1 / (qcut - 1)) if qcut > 1 else 1.0

    quantile_dict = {}    
    cumulative_percent = 0.0
    quantile = 0

    for category in categories.index:
        cumulative_percent += categories[category]

        quantile_assigned = quantile

        if cumulative_percent > quantile_threshold and quantile < (qcut - 1):
            quantile += 1

            if cumulative_percent >= quantile_max:
                quantile_assigned = quantile
                cumulative_percent = categories[category]
            else:
                cumulative_percent = 0.0
            
        quantile_dict[category] = quantile_assigned


    return (data.map(quantile_dict), quantile_dict)


