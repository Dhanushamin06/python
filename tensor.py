# !pip install tensorflow-datasets
import tensorflow_datasets as tfds
import tensorflow as tf

# Construct a tf.data.Dataset
ds = tfds.load('mnist', split='train', as_supervised=True, shuffle_files=True)

# Build your input pipeline
ds = ds.shuffle(1000).batch(128).prefetch(10).take(5)
for image, label in ds:
  pass