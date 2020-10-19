# ERICS
This repository provides an implementation of the ERICS concept drift detection framework that is introduced in

*Johannes Haug and Gjergji Kasneci (2020). Learning Parameter Distributions to Detect Concept Drift in Data Streams.*

to be published in the Proceedings of the 25th International Conference on Pattern Recognition (ICPR) 2020.
An ArXiv-link to the paper will be added soon.

## Apply ERICS to Your Project
Here, we provide ERICS with a Probit model, as described in the paper.
Note that we adopted the optimization scheme of the [FIRES](https://github.com/haugjo/fires) feature selection framework [1].
After downloading/cloning the package you may use ERICS as follows:

```python
from skmultiflow.data import FileStream
from erics import ERICS

# Load data into scikit-multiflow FileStream
# NOTE: In order to use the default 'probit' model, data must be numeric.
# We suggest users to factorize/one-hot encode categorical variables and to normalize continuous ones.
stream = FileStream('./spambase.csv', target_idx=0)  
stream.prepare_for_use()

# Initialize ERICS
erics = ERICS(n_param=stream.n_features,    # Total no. of parameters
              window_mvg_average=50,        # Window Size for computation of moving average (i.e. M-parameter in the paper)
              window_drift_detect=50,       # Window Size for Drift Detection (i.e. W-parameter in the paper)
              beta=0.001,                   # Update rate for the alpha-threshold
              base_model='probit')          # Name of the predictive model (whose parameters we investigate)

while stream.has_more_samples():
    x, y = stream.next_sample(batch_size=100)  # Load new sample
    global_drift_detected, partial_drift_detected, comp_time = erics.check_drift(x, y)  # Detect global/partial concept drift

    if global_drift_detected:
        print('New global drift detected!')
        ''' Do something '''
    elif partial_drift_detected:
        print('New partial drift detected!')
        partial_drifts = erics.partial_drifts  # Returns an array of tuples: (time step, feature index)
        ''' Do something '''

stream.restart()  # Restart the FileStream
```

## Use Your Own Predictive Model
ERICS is model-agnostic. Hence, you may use the parameters of any predictive model.
To add another predictive model, you need to substitute the placeholders ``### ADD YOUR OWN MODEL HERE ###`` in *erics.py* accordingly.

**Note**: We consider normally distributed model parameters in this implementation. If you require a different parameter distribution, you may specify ERICS according to the paper.

If you want to contribute your instantiation of ERICS to this repository, please feel free to issue a pull request or send us an email.

## Related Papers
[1] Haug, Johannes, et al. ["Leveraging Model Inherent Variable Importance for Stable Online Feature Selection."](https://dl.acm.org/doi/abs/10.1145/3394486.3403200) Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining. 2020.