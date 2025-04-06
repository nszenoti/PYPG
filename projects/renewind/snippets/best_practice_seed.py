import tensorflow as tf
import random
import numpy as np

seed = 42
tf.random.set_seed(seed)
np.random.seed(seed)
random.seed(seed)
tf.config.experimental.enable_op_determinism()
