import importlib.util
import numpy as np

# load the module
spec = importlib.util.spec_from_file_location("program_features", "/path/to/program_features.py")
program_features = importlib.util.module_from_spec(spec)
spec.loader.exec_module(program_features)

# access the data
X = program_features.features_array
