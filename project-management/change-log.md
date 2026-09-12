# Change Log

This log records genuine changes and decisions made during the project.

| Change ID | Date | Change or Decision | Reason | Impact | Status |
|---|---|---|---|---|---|
| C001 | 10 September 2026 | Selected the UCI Bank Marketing dataset | It is free, public, large enough for the assignment and suitable for a classification problem | Makes the project reproducible without using private banking data | Approved |
| C002 | 10 September 2026 | Chose binary classification as the analytical approach | The target variable y records whether the customer subscribed to a term deposit | Determines the modelling and evaluation strategy | Approved |
| C003 | 10 September 2026 | Decided not to rely on accuracy as the main evaluation metric | The target is imbalanced: 88.3% 
o and 11.7% yes | Recall, precision, F1-score and ROC-AUC will also be evaluated | Approved |
| C004 | 10 September 2026 | Flagged duration for leakage review | Call duration is only known after the contact has taken place and may not be available at prediction time | The model will be tested without duration for realistic pre-contact prediction | Approved |

## Notes

Further changes will be added when genuine analytical decisions occur during preprocessing and modelling.

| C005 | 12 September 2026 | Retained contact, month and previous campaign outcome as candidate predictors | EDA showed clear differences in subscription rates across these variables | These variables will be included in preprocessing and model training | Approved |
| C006 | 12 September 2026 | Confirmed that model evaluation must include recall, precision, F1-score and ROC-AUC | The target distribution is 88.3% no and 11.7% yes | Prevents misleading evaluation using accuracy alone | Approved |

| C007 | 12 September 2026 | Rejected accuracy as the primary success metric after baseline evaluation | The baseline achieved 88.3% accuracy while detecting zero subscribers | F1-score, recall and ROC-AUC will receive greater emphasis when comparing models | Approved |

| C008 | 12 September 2026 | Retained balanced Logistic Regression as a valid improved model despite lower accuracy | It identified 62.38% of actual subscribers and achieved ROC-AUC 0.7722, while the higher-accuracy baseline detected none | Model selection will prioritise useful minority-class detection rather than raw accuracy | Approved |
| C009 | 12 September 2026 | Decided to evaluate another improved classifier before final model selection | Logistic Regression produced 1,819 false positives and precision of only 26.62% | A second model will be tested for a better precision-recall balance | Approved |

| C008 | 12 September 2026 | Retained balanced Logistic Regression as a valid improved model despite lower accuracy | It identified 62.38% of actual subscribers and achieved ROC-AUC 0.7722, while the higher-accuracy baseline detected none | Model selection will prioritise useful minority-class detection rather than raw accuracy | Approved |
| C009 | 12 September 2026 | Decided to evaluate another improved classifier before final model selection | Logistic Regression produced 1,819 false positives and precision of only 26.62% | A second model will be tested for a better precision-recall balance | Approved |

| C010 | 12 September 2026 | Selected Random Forest as the preferred final model | It achieved the highest F1-score (0.4378) and ROC-AUC (0.7936) while substantially improving precision over Logistic Regression | Random Forest will be used as the main model in the final report, while Logistic Regression will be retained as an alternative where higher recall is preferred | Approved |
