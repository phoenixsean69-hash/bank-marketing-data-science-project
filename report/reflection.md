# Individual Reflection

This project helped me understand that a data science project is not only about building a model. A large part of the work involved planning, documenting decisions, checking data quality, managing risks and explaining why certain modelling choices were made.

One of the main things I learned was how misleading accuracy can be when working with an imbalanced dataset. At first, an accuracy value above 88% looked strong. However, the baseline model achieved this by predicting every customer as a non-subscriber. It completely failed to identify the customers who actually subscribed. This changed how I looked at model evaluation and made me pay more attention to recall, precision, F1-score and ROC-AUC.

Another important lesson was data leakage. The duration variable appeared useful, but it would only be known after a marketing call had already taken place. Since the project was supposed to support decisions before contacting customers, keeping this variable would have made the model look stronger than it would be in a realistic setting. Removing it made the project more credible.

The exploratory analysis also affected my thinking. Variables such as contact type, month and previous campaign outcome showed clear differences in subscription rates. However, I learned that these relationships should not automatically be treated as causes. They are useful for prediction, but they do not prove that changing one factor will directly change customer behaviour.

The comparison between Logistic Regression and Random Forest was also useful. Logistic Regression had better recall, while Random Forest had better precision, F1-score and ROC-AUC. This showed me that the best model depends partly on the business objective. If the main goal were to identify as many possible subscribers as possible, Logistic Regression could still be useful. For this project, Random Forest was selected because it gave the best overall balance.

During the project, some decisions changed after the real data was inspected. For example, accuracy was originally considered as one of the main measures, but the baseline results showed that this was not enough. The change log helped me record these decisions rather than pretending that the whole project followed the original plan without adjustment.

If I were to improve the project in a future iteration, I would spend more time on threshold tuning, model calibration and feature importance. I would also test the model on newer data and investigate fairness more deeply across different customer groups. In a real banking environment, I would want stronger privacy, governance and monitoring controls before the model was used operationally.

Overall, the project improved both my technical and project-management understanding. I learned that a useful data science solution should be reproducible, explainable, monitored and linked to a clear business need. The model itself is only one part of the final solution.
