import os

# import local_pyutils
from . import filenames, local_pyutils

# TODO(allie): generate a static class from this file (to enable autocomplete)

default_pars = local_pyutils.dotdictify(dict(
    paths=dict(
        files=dict(
            infile_features='',
            shufflenames_libsvm='',
            shuffle_idxs='',
            runinfo_fname='',
            done_file='',
            verbose_fname=''
        ),
        folders=dict(
            path_to_tmp='',
            path_to_results='',
            predict_directories='',
            output_directory=''
        )
    ),
    algorithm=dict(
        permutations=dict(
            n_shuffles=10,
            shuffle_size=1
        ),
        discriminability=dict(
            lambd=0.1,
            alpha=1e-30,
            solver_num=0,
            window_size=100,
            window_stride_multiplier=0.5,
            window_stride=None, # Set this OR window_stride_multiplier
            max_buffer_size=-1  # -1: no max buffer size.
            ),
        aggregation=dict(
            average_over_splits='mean'
        )
    ),
    system=dict(
        anomalyframework_root='./',
        path_to_trainpredict_relative='build/anomalyframework/cpp/score_shuffle',
        num_threads=8
    ),
    tags=dict(
        datestring='',
        timestring='',
        processId='',
        results_name=''
    )
))


class Pars(local_pyutils.dotdictify):
    def __init__(self, **kwargs):
        for key in default_pars:
            self.__setitem__(key, default_pars[key])
        self.set_values(**kwargs)
        self.system.anomalyframework_root = os.path.abspath(self.system.anomalyframework_root)
        filenames.fill_tags_and_paths(self)

    def set_values(self, **kwargs):
        for key, value in kwargs.items():
            local_pyutils.replace_in_nested_dictionary(self, key, value)
