# scikit-learn at PyData Chicago 2016 

Enhancing _Sebastian Raschka_ [codes](https://www.youtube.com/watch?v=9fOWryQq9J8) at PyData Chicago 2016 

## Tuning Attempts

- brain-weight vs head-size -> r-squared: %64
    - \+ dummy( gender_2) -> r-squared: %64
    - \+ outlier elimination (< 0.99 quantile) -> r-squared: %71 (predictive power increased!)
    - \+ outlier elimination (< 0.95 quantile) -> r-squared: %65
- log_brain-weight vs log_head-size -> r-squared: %65 (not added significant impact)
    - \+ dummy( gender_2) -> r-squared: %65, dummy variables
    - \+ dummy( gender_2, age-group_2) -> r-squared: %65, dummy variables
        - \+ outlier elimination (< 0.99 quantile) -> r-squared: %62
    - \+ outlier elimination (< 0.99 quantile) -> r-squared: %72
- seq_brain-weight vs seq_head-size -> r-squared: %63 (a bit worse)
- sqrt_brain-weight vs sqrt_head-size -> r-squared: %64