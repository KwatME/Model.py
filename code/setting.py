from _make_path_dict import _make_path_dict

TITLE = 'RNA TCGA Brain Primary Solid Tumor (18.11.19)'

FEATURE_X_SAMPLE_FILE_PATH = '../data/rna__gene_x_sample.brain_primary_solid_tumor.tsv'

NANIZE = 0

DROP_AXIS = 1

MAX_NA = 0.05

MIN_N_NOT_NA_UNIQUE_VALUE = None

SHIFT_AS_NECESSARY_BEFORE_LOGGING = '0<'

LOG_BASE = '2'

NORMALIZATION_AXIS = 0

NORMALIZATION_METHOD = '-0-'

SELECT_GENE_SYMBOL = True

FEATURES_TO_PEEK = (
    'F2RL1',
    'ST14',
    'IDH1',
    'EGFR',
)

SAMPLES_TO_PEEK = ()

MAX_N_JOB = 1

ELEMENTS = ('feature', )

CONTEXTS = (
    'negative',
    'positive',
)

SELECT_FEATURE_AUTOMATICALLY = True

N_TOP_FEATURE = None

SELECT_SAMPLE_AUTOMATICALLY = False

N_TOP_SAMPLE = None

NMF_KS = tuple(range(
    2,
    10,
))

NMF_K = 8

HCC_KS = NMF_KS

WT_HCC_K = NMF_K

H_HCC_K = NMF_K

EXTREME_FEATURE_THRESHOLD = 24

ELEMENT_ENTROPY_QUANTILE = 1

GPS_MAP_WT_PULL_POWER = 1

GPS_MAP_WT_ELEMENT_MARKER_SIZE = 12

GPS_MAP_WT_BANDWIDTH_FACTOR = 2.4

GPS_MAP_H_PULL_POWER = 1

GPS_MAP_H_ELEMENT_MARKER_SIZE = 12

GPS_MAP_H_BANDWIDTH_FACTOR = 2.4

PLOT_STD = 2.4

UPLOAD_TO_PLOTLY = False

PATH_DICT = path_dict = _make_path_dict(
    TITLE,
    ELEMENTS,
    NMF_K,
    WT_HCC_K,
    H_HCC_K,
    UPLOAD_TO_PLOTLY,
)
