# 🏏 IPL Player Recommendation System

A player recommendation system for IPL batsmen that identifies players with similar performance profiles using **feature analysis, data visualization, appropriate scaling techniques, vector representation, and cosine similarity**.

The objective is to compare players based on their statistical characteristics and identify players whose performance profiles are mathematically similar.

---

## 📌 Project Overview

The project follows a structured process to transform IPL player statistics into comparable numerical representations and measure similarity between players.

```text
IPL Player Statistics
        ↓
Data Cleaning & Transformation
        ↓
Exploratory Data Analysis
        ↓
Data Visualization
        ↓
Pearson Correlation
        ↓
Feature Selection
        ↓
Distribution & Outlier Analysis
        ↓
Feature Scaling
        ↓
Vector Representation
        ↓
Cosine Similarity
        ↓
Similarity Matrix
        ↓
Player Recommendations
```

---

## 🔬 Methodology

### 1. Data Cleaning and Transformation

The IPL player statistics were cleaned and transformed into a structured format suitable for numerical analysis.

The data preparation process included:

* Cleaning player statistics
* Handling the structure of the dataset
* Transforming variables into appropriate numerical formats
* Preparing features for statistical analysis and similarity calculation

---

### 2. Exploratory Data Analysis

Exploratory analysis was performed to understand the characteristics of the player statistics before applying feature selection and scaling.

The analysis focused on:

* Feature distributions
* Relationships between variables
* Outliers
* Feature ranges
* Correlations between numerical variables

---

### 3. Data Visualization

**Matplotlib** and **Seaborn** were used to visualize and investigate the dataset.

Visualizations were used to understand:

* Feature distributions
* Outliers
* Relationships between variables
* Correlation between features

Examples of visual analysis included distribution plots, box plots, and correlation heatmaps.

These visualizations helped determine how the features should be processed before calculating player similarity.

---

### 4. Feature Analysis Using Pearson Correlation

**Pearson correlation** was used to examine the linear relationships between numerical features.

The correlation coefficient ranges from:

```text
-1 → Strong negative linear relationship
 0 → No linear relationship
+1 → Strong positive linear relationship
```

Correlation analysis was used as part of the feature selection process to identify relationships between features and reduce unnecessary redundancy.

---

### 5. Distribution and Outlier Analysis

Before selecting a scaling method, the distribution and outlier characteristics of the features were examined.

This was important because different IPL statistics can have different:

* Numerical ranges
* Distributions
* Degrees of skewness
* Outlier patterns

The distribution of each feature was considered before deciding which scaling technique was appropriate.

---

### 6. Feature Scaling

Two scaling approaches were used depending on the characteristics of the features.

#### StandardScaler

**StandardScaler** was used where standardization was appropriate.

It transforms a feature using:

```text
z = (x - mean) / standard deviation
```

This places features on a comparable scale.

#### RobustScaler

**RobustScaler** was used for features where outliers could have a stronger influence.

RobustScaler uses the **median** and **interquartile range (IQR)**, making it less sensitive to extreme observations.

The scaling method was therefore selected based on the observed distribution and outlier characteristics rather than applying a single scaler to all features.

---

## 🔢 Vector Representation

After feature selection and scaling, each player was represented as a numerical vector.

A simplified representation could look like:

```text
Player A → [0.42, -0.18, 1.24, 0.67, -0.31]

Player B → [0.39, -0.12, 1.18, 0.71, -0.27]
```

Each vector represents a player's statistical profile across the selected features.

---

## 📐 Cosine Similarity

The scaled feature vectors were compared using **cosine similarity**.

Cosine similarity measures the angle between two vectors.

```text
cosine similarity = (A · B) / (||A|| ||B||)
```

A value closer to `1` indicates that the vectors have a more similar orientation, while a value closer to `0` indicates less similarity.

The cosine similarity was calculated between players to create a player-to-player similarity matrix.

---

## 🧮 Similarity Matrix

The resulting similarity matrix contains players on both the rows and columns.

Example:

| Player   | Player A | Player B | Player C |
| -------- | -------: | -------: | -------: |
| Player A |     1.00 |     0.94 |     0.71 |
| Player B |     0.94 |     1.00 |     0.76 |
| Player C |     0.71 |     0.76 |     1.00 |

The diagonal contains `1.00` because each player has maximum similarity with themselves.

For recommendations, the selected player's own similarity value is excluded.

The remaining players are sorted according to their cosine similarity values.

---

## 🎯 Recommendation Process

When a user selects an IPL batsman:

1. The application identifies the player.
2. The player's vector/similarity information is retrieved.
3. The player's own similarity score is removed.
4. The remaining players are sorted by cosine similarity.
5. The requested number of similar players is selected.
6. Similarity scores are displayed as percentages.

Example:

```text
Selected Player: Player A

Recommended Players

Player B       94.21%
Player C       88.73%
Player D       84.65%
```

The recommendations represent **statistical similarity based on the selected features**.

---

## 🖥️ Streamlit Application

A Streamlit application was developed to provide an interactive interface for the recommendation system.

The application allows users to:

* Search for an IPL player
* Handle approximate/fuzzy player-name matching
* Select the number of recommendations
* View similar players
* View cosine similarity scores

The application is located at:

```text
app/app.py
```

---

## 📂 Project Structure

```text
Data-science-main/
│
├── app/
│   └── app.py
│
├── data/
│   ├── cosine_similarity.parquet
│   └── Batsmen_Statistics_cleaned.parquet
│
├── Notebooks/
│   ├── 1_IPL_Period.ipynb
│   ├── 3_Bowler_Model.ipynb
│   ├── Batsmen_Data_Cleaning_Notebook.ipynb
│   ├── Batsmen_Data_Transformation_Notebook.ipynb
│   └── Feature_Selection.ipynb
│
├── raw/
│
├── requirements.txt
│
└── README.md
```

---

## 📓 Project Notebooks

### Batsmen Data Cleaning

`Batsmen_Data_Cleaning_Notebook.ipynb`

Contains the cleaning and preparation of the IPL batsmen statistics.

### Batsmen Data Transformation

`Batsmen_Data_Transformation_Notebook.ipynb`

Transforms the cleaned statistics into a structure suitable for further analysis.

### Feature Selection

`Feature_Selection.ipynb`

Contains the feature analysis, Pearson correlation analysis, distribution and outlier analysis, scaling, vector representation, and cosine similarity calculation.

### IPL Period

`1_IPL_Period.ipynb`

Contains IPL period-related analysis and processing.

### Bowler Model

`3_Bowler_Model.ipynb`

Contains work related to the IPL bowler analysis.

---

## 🛠️ Technologies Used

### Programming & Analysis

* Python
* Pandas
* NumPy
* PySpark

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning & Similarity

* Scikit-learn
* StandardScaler
* RobustScaler
* Cosine Similarity

### Application

* Streamlit

### Data & Development

* Parquet
* Databricks
* Jupyter Notebooks
* Git
* GitHub

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/shabeeradhnan/Data-science.git
```

Navigate to the project:

```bash
cd Data-science
```

Create a virtual environment:

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## ▶️ Run the Application

From the project root:

```bash
streamlit run app/app.py
```

The Streamlit application will open in your browser.

---

## 📊 Key Concepts

The main concepts implemented in this project are:

* Exploratory data analysis
* Data visualization
* Pearson correlation
* Feature selection
* Distribution analysis
* Outlier analysis
* StandardScaler
* RobustScaler
* Vector representation
* Cosine similarity
* Similarity matrix
* Player recommendation

---

## ⚠️ Interpretation

The recommendation system identifies players with similar **statistical profiles based on the selected features**.

A high cosine similarity indicates that two players have similar feature-vector orientations after preprocessing and scaling. It does not necessarily mean that they have identical playing styles, roles, or future performance.

---

## 🚀 Future Improvements

Potential extensions include:

* Adding more player-specific statistics
* Adding player profile information
* Including season-wise similarity
* Comparing players across different IPL periods
* Adding interactive player statistics
* Extending the recommendation system to bowlers
* Adding visual comparisons between recommended players
* Experimenting with alternative similarity measures
* Deploying the Streamlit application

---

## 👤 Author

**Edwin Victor**
**Shabeer Adhnan**

IPL Player Recommendation System
