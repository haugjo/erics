# ERICS
This repository provides an implementation of the ERICS concept drift detection framework that is introduced in

*Johannes Haug and Gjergji Kasneci (2020). Learning Parameter Distributions to Detect Concept Drift in Data Streams.*

to be published in the Proceedings of the 25th International Conference on Pattern Recognition (ICPR) 2020.
An ArXiv-link to the paper will be added soon.

## Apply ERICS to Your Project
Here, we implemented ERICS for a Probit model, as described in the paper.
Note that we adopted the optimization scheme of the [FIRES](https://github.com/haugjo/fires) feature selection framework [1].
This implementation can be used as follows:




## Use Your Own Predictive Model
ERICS is model-agnostic. Hence, you may use the parameters of any predictive model.
To add another predictive model, you need to substitute the placeholders ``### ADD YOUR OWN MODEL HERE`` in *erics.py* accordingly.

If you want to contribute your instantiation of ERICS to this repository, please feel free to issue a pull request or send us an email.

## Related Papers
[1] Haug, Johannes, et al. ["Leveraging Model Inherent Variable Importance for Stable Online Feature Selection."](https://dl.acm.org/doi/abs/10.1145/3394486.3403200) Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining. 2020.