- 👋 Hi, I’m @Raghav0079
# Exploratory Data Analysis (EDA) and Data Manipulation with Pandas

This repository contains two Jupyter notebooks that demonstrate various data analysis, manipulation, and visualization techniques using Python libraries like Pandas, NumPy, Matplotlib, and Seaborn.

---

## Notebooks Overview

### 1. `pandas.ipynb`
This notebook focuses on data manipulation and analysis using Pandas and NumPy. It includes examples of creating DataFrames, performing operations, and generating plots.

#### Key Steps:
1. **DataFrame Creation**:
   - Demonstrates creating DataFrames from dictionaries, NumPy arrays, and random data.
   - Example:
     ```python
     df = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
     ```

2. **DataFrame Operations**:
   - Accessing rows and columns using `.loc` and `.iloc`.
   - Applying functions to DataFrames using `.apply()` and `.applymap()`.

3. **Data Visualization**:
   - **Scatter Plot**:
     - Created using Seaborn to visualize relationships between variables.
     - Example:
       ```python
       sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
       plt.show()
       ```
   - **Histogram**:
     - Displays the distribution of random data.
     - Example:
       ```python
       plt.hist(data, bins=30, edgecolor='black')
       plt.title('Histogram of Random Data')
       plt.show()
       ```
   - **Box Plot**:
     - Visualizes the distribution of data with quartiles.
     - Example:
       ```python
       plt.boxplot(data, vert=False, patch_artist=True)
       ```

4. **Reading and Writing Data**:
   - Reading CSV, JSON, and HTML files.
   - Writing DataFrames to CSV and JSON formats.

5. **Advanced Data Manipulation**:
   - Reindexing, renaming columns, and handling missing values.
   - Example:
     ```python
     df_reindexed = df.reindex(new_index)
     ```

---

### 2. `advanced python.ipynb`
This notebook demonstrates advanced Python concepts, including list comprehensions, functions, and logistic regression.

#### Key Steps:
1. **List Comprehensions**:
   - Examples of creating lists with conditions and transformations.
   - Example:
     ```python
     lst1 = [i * i for i in lst if i % 2 == 0]
     ```

2. **Functions**:
   - Demonstrates defining and using functions, including lambda functions.
   - Example:
     ```python
     add = lambda a, b: a + b
     ```

3. **Data Cleaning**:
   - Handling missing values and encoding categorical variables.
   - Example:
     ```python
     train = train.drop('Cabin', axis=1)
     ```

4. **Logistic Regression**:
   - Building a logistic regression model using Scikit-learn.
   - Example:
     ```python
     logmodel = LogisticRegression()
     logmodel.fit(X_train, y_train)
     ```

5. **Data Visualization**:
   - **Count Plot**:
     - Displays the count of categorical variables.
     - Example:
       ```python
       sns.countplot(x='Survived', data=train)
       ```
   - **Heatmap**:
     - Visualizes missing values in the dataset.
     - Example:
       ```python
       sns.heatmap(train.isnull(), cbar=True, cmap='viridis')
       ```
   - **Box Plot**:
     - Shows the distribution of age across passenger classes.
     - Example:
       ```python
       sns.boxplot(x='Pclass', y='Age', data=train)
       ```

---

## Plots Highlighted

### Scatter Plot
- **Notebook**: `pandas.ipynb`
- **Description**: Visualizes the relationship between `total_bill` and `tip` with hue based on `sex`.

### Histogram
- **Notebook**: `pandas.ipynb`
- **Description**: Displays the frequency distribution of random data.

### Box Plot
- **Notebook**: Both
- **Description**: Shows data distribution with quartiles.

### Count Plot
- **Notebook**: `advanced python.ipynb`
- **Description**: Displays the count of survivors in the Titanic dataset.

### Heatmap
- **Notebook**: `advanced python.ipynb`
- **Description**: Visualizes missing values in the Titanic dataset.

---

## Getting Started

To run these notebooks, you'll need the following libraries installed:
```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


