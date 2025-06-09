# echowhisper
A Machine Learning-Based Analysis of Music Era Preferences Among Youth, Presented Through the EchoWhisper Web Platform.
## License

This project is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
# project overview
EchoWhisper is an Analytical Report Website that presents detailed findings from a study on music era preferences among the younger generation. The project aims to analyze and predict which music era—1990s, 2000s, or 2020s—is most preferred by individuals aged 15 to 25, based on their emotional states and moods.

Data for this project was collected through a Google Form survey targeted exclusively at this age group to better understand the listening behavior of young people. The collected data was then analyzed using machine learning techniques such as Random Forest and XGBoost, along with SHAP analysis and clustering methods to extract meaningful insights. EchoWhisper showcases the results of this backend analysis in a clear and concise format for easy interpretation.

#techniques used
The data collected from the Google Form was stored in an Excel CSV format, which allowed for easy handling and analysis using data science tools. Before applying any machine learning algorithms, the dataset underwent several preprocessing steps to ensure accuracy and quality of the analysis.

Data Preprocessing
Cleaning: Missing values and inconsistencies were identified and handled appropriately to maintain data integrity.

Normalization: Numerical features were scaled to a standard range to improve model performance.

Encoding: Categorical variables were converted into numerical form using techniques like one-hot encoding, enabling their use in machine learning algorithms.

Feature Selection: Relevant features impacting music preference were selected based on correlation analysis to reduce noise and improve model efficiency.

Machine Learning Algorithms and Analysis
Random Forest:
This ensemble learning method was used to classify and predict music era preferences. Random Forest builds multiple decision trees and merges their results for more accurate and stable predictions.

XGBoost:
An optimized gradient boosting algorithm that improves prediction accuracy by sequentially correcting errors from previous models. It is highly effective in handling structured data and was employed for robust classification tasks.

Hyperparameter Tuning (GridSearchCV):
To enhance model performance, hyperparameters of both Random Forest and XGBoost models were fine-tuned using GridSearchCV. This method performs exhaustive search over specified parameter values using cross-validation to find the best model settings.

Cross-Validation:
K-fold cross-validation was applied to validate the models’ generalizability by partitioning the dataset into training and testing subsets multiple times, reducing the chances of overfitting.

SHAP Analysis:
SHapley Additive exPlanations (SHAP) was used to interpret the model predictions by quantifying the contribution of each feature to the prediction, providing transparency and insights into what drives music era preferences.

Clustering and Correlation Analysis:
Unsupervised learning methods were used to group similar data points and identify patterns within the dataset. Correlation analysis helped in understanding relationships between features and guided feature selection.

This approach allowed us to thoroughly analyze the data and uncover significant patterns influencing the younger generation’s music preferences. The insights obtained from these techniques are presented through the EchoWhisper Analytical Report Website.

#results
The EchoWhisper Analytical Report Website showcases the comprehensive results obtained from the backend machine learning analysis. The key findings from the project include:

Model Accuracy:
The classification models demonstrated strong performance in predicting music era preferences:

Random Forest: Baseline accuracy of 72.62%, improved to 77.38% with GridSearchCV tuning.

XGBoost: Baseline accuracy of 76.19%, further improved to 78.57% after tuning.

Cluster Analysis: Achieved an accuracy of 80.95% with tuned Random Forest, and 77.38% with XGBoost.

Predominant Era Preference:
The analysis reveals that the 2000s era is the most preferred music era among individuals aged 15 to 25, reflecting the emotional resonance and listening trends within this group.

Emotional Influence:
The results highlight how different emotional states and moods significantly impact music preferences, showing strong correlations between emotions and the chosen era.

Feature Importance:
SHAP analysis identifies the most influential factors driving the model’s predictions, providing transparency into how various emotional and behavioral attributes affect music preferences.

Clustering Insights:
Clustering techniques uncovered distinct groups of listeners, indicating diverse behavioral patterns and music era affinities among young individuals.

The website presents these insights through clear visualizations such as charts and graphs, offering an accessible summary of the findings. While EchoWhisper does not stream music, it provides valuable understanding of how the younger generation connects emotionally with music from different eras.
