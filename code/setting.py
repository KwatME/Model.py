from make_path_dict import make_path_dict

# ==============================================================================
# Please tell me about your feature-by-sample data.
# ==============================================================================
FEATURE_X_SAMPLE_FILE_PATH = "../data/rna__gene_x_cell_line.fibroblast.tsv"

FEATURE_X_SAMPLE_ALIAS = "RNA CCLE Fibroblast (18.12.11)"

FEATURE_ALIAS = "Gene"

SAMPLE_ALIAS = "Cell Line"

FEATURE_X_SAMPLE_VALUE_NAME = "TPM"

HIGHLIGHT_JSON_FILE_PATH = "../data/highlight.json"

# ==============================================================================
# How do you want to plot?
# ==============================================================================
PLOT_HEAT_MAP_MAX_SIZE = int(2e5)

PLOT_CLUSTER_MAX_SIZE = int(2e3)

PLOT_DISTRIBUTIONS_MAX_SIZE = int(2e4)

PLOT_RUG_MAX_SIZE = int(2e3)

PLOT_STD = 2.4

UPLOAD_TO_PLOTLY = True

# ==============================================================================
# How many thread(s) are you willing to use simultaneously?
# ==============================================================================
MAX_N_JOB = 8

# ==============================================================================
# How do you want to pre-process the data?
# ==============================================================================
FEATURES_TO_DROP = None

SAMPLES_TO_DROP = None

NANIZE = None  # Value less than or equal to NANIZE will become nan

DROP_AXIS = None  # "0" for column | "1" for row | None for both

MAX_NA = None

MIN_N_NOT_NA_UNIQUE_VALUE = 1

SHIFT_AS_NECESSARY_TO_ACHIEVE_MIN_BEFORE_LOGGING = "0<"

LOG_BASE = 2

NORMALIZATION_AXIS = 0

NORMALIZATION_METHOD = "-0-"  # "-0-" | "0-1" | "sum" | "rank"

CLIP_MIN = None

CLIP_MAX = None

# ==============================================================================
# Do you want to select only good gene symbols?
# ==============================================================================
SELECT_GENE_SYMBOL = True

# ==============================================================================
# What are some elements you want to focus on?
# ==============================================================================
FEATURES_TO_PEEK = ("F2RL1", "ST14", "TERT", "YAP1", "ZEB1")

SAMPLES_TO_PEEK = ()

# ==============================================================================
# How do you want to normalize signal?
# ==============================================================================
RAW_SIGNAL_NORMALIZATION_METHOD = "0-1"

CONTEXT_SIGNAL_NORMALIZATION_METHOD = None

# ==============================================================================
# Which element type(s) do you want use for signal?
# ==============================================================================
ELEMENT_TYPES = ("feature",)

# ==============================================================================
# Which context(s) do you want use for signal?
# ==============================================================================
CONTEXTS = ("negative", "positive")

# ==============================================================================
# Do you want to select elements automatically when making signal?
# ==============================================================================
SELECT_FEATURE_AUTOMATICALLY = True

SELECT_SAMPLE_AUTOMATICALLY = False

# ==============================================================================
# How do you want to factorize the signal?
# ==============================================================================
NMF_KS = tuple(range(2, 10))

NMF_K = 3

# ==============================================================================
# How do you want to cluster elements using the factors?
# ==============================================================================
HCC_KS = NMF_KS

W_HCC_K = NMF_K

H_HCC_K = NMF_K

# ==============================================================================
# How do you want to make match panel?
# ==============================================================================
EXTREME_FEATURE_THRESHOLD = 16

N_SAMPLING = 0

N_PERMUTATION = 0

# ==============================================================================
# How do you want to filter noisy elements when making GPS Map?
# ==============================================================================
ELEMENT_ENTROPY_QUANTILE = 1

# ==============================================================================
# How do you want to make feature GPS Map?
# ==============================================================================
GPS_MAP_W_PULL_POWER = 1

GPS_MAP_W_ELEMENT_MARKER_SIZE = 10

GPS_MAP_W_BANDWIDTH_FACTOR = 2.4

# ==============================================================================
# How do you want to make sample GPS Map?
# ==============================================================================
GPS_MAP_H_PULL_POWER = 1

GPS_MAP_H_ELEMENT_MARKER_SIZE = 32

GPS_MAP_H_BANDWIDTH_FACTOR = 2.4

# ==============================================================================
# I'm making output paths based on these settings and populating `../output`.
# ==============================================================================
PATH_DICT = make_path_dict(
    NMF_K, W_HCC_K, H_HCC_K, FEATURE_X_SAMPLE_ALIAS, UPLOAD_TO_PLOTLY
)

# ==============================================================================
# All set! Enjoy this workflow :)
# ==============================================================================
