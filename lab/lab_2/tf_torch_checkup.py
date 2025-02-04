import tensorflow as tf
print("Num GPUs Available:", len(tf.config.list_physical_devices('GPU')))

import torch
print(torch.__version__)
print(torch.cuda.is_available())
print(torch.version.cuda)