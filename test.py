from skmultiflow.data import FileStream

from erics import ERICS

stream = FileStream('./spambase.csv', target_idx=0)
stream.prepare_for_use()

batch_size = 100

erics = ERICS(n_param=stream.n_features,
              window_mvg_average=25,
              window_drift_detect=20,
              beta=0.001)

while stream.has_more_samples():
    x, y = stream.next_sample(batch_size)
    global_drift_detected, partial_drift_detected, comp_time = erics.check_drift(x, y)

    if global_drift_detected:
        print('New global drift detected!')
        '''
            Do something
        '''
    elif partial_drift_detected:
        print('New partial drift detected!')
        partial_drifts = erics.partial_drifts  # returns an array of tuples: (time step, feature index)
        '''
            Do something
        '''

stream.restart()
