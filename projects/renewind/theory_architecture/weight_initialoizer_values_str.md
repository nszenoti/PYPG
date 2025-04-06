Yes! In Keras, you **can use strings** to specify standard initializers like `"he_normal"` instead of creating the initializer object explicitly.

### Example – Using string:
```python
from tensorflow.keras.layers import Dense

layer = Dense(units=64, kernel_initializer='he_normal')
```

### Equivalent – Using the class:
```python
from tensorflow.keras.layers import Dense
from tensorflow.keras.initializers import HeNormal

layer = Dense(units=64, kernel_initializer=HeNormal())
```

### TL;DR:

✅ These are all valid string values you can use for weight initialization:
- `'he_normal'`
- `'he_uniform'`
- `'glorot_normal'`
- `'glorot_uniform'`
- `'lecun_normal'`
- `'lecun_uniform'`
- `'zeros'`
- `'ones'`
- `'random_normal'`
- `'random_uniform'`
- `'identity'`
- `'orthogonal'`

Let me know if you want to explore custom initializers or how different ones affect model training!**