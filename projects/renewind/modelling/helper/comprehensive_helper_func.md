











```python
import time
import pandas as pd
from tensorflow import keras

# Create empty results dataframes
results = pd.DataFrame(columns=[
    'model_id',
    'hidden_layers',
    'neurons_per_layer',
    'activation',
    'epochs',
    'batch_size',
    'optimizer',
    'learning_rate',
    'momentum',
    'weight_initializer',
    'regularization',
    'train_loss',
    'val_loss',
    'training_time'
])

results_metrics = pd.DataFrame(columns=[
    'model_id',
    'train_accuracy',
    'val_accuracy',
    'train_precision',
    'val_precision',
    'train_recall',
    'val_recall',
    'train_f1',
    'val_f1',
    'train_f2',
    'val_f2',
    'train_auc',
    'val_auc'
])

# Helper function to train model and record results
def train_and_evaluate_model(
    X_train, y_train, X_val, y_val,
    hidden_layers=1,
    neurons_per_layer=[16],
    activation='relu',
    epochs=50,
    batch_size=32,
    optimizer='adam',
    learning_rate=0.001,
    momentum=0.0,
    weight_initializer='glorot_uniform',
    regularization=None,
    model_id=None
):
    """
    Train a neural network model and record results

    Parameters:
    -----------
    X_train, y_train: Training data
    X_val, y_val: Validation data
    hidden_layers: Number of hidden layers
    neurons_per_layer: List of neurons for each hidden layer
    activation: Activation function for hidden layers
    epochs: Number of training epochs
    batch_size: Batch size for training
    optimizer: Optimizer ('adam', 'sgd', etc.)
    learning_rate: Learning rate for optimizer
    momentum: Momentum (for SGD)
    weight_initializer: Weight initialization method
    regularization: Regularization method (None, 'l1', 'l2', 'l1_l2')
    model_id: Identifier for the model

    Returns:
    --------
    model: Trained Keras model
    history: Training history
    """
    global results, results_metrics

    # Generate model ID if not provided
    if model_id is None:
        model_id = f"model_{len(results) + 1}"

    # Input dimension
    input_dim = X_train.shape[1]

    # Create model
    model = keras.Sequential()

    # Input layer
    model.add(keras.layers.Input(shape=(input_dim,)))

    # Hidden layers
    for i in range(hidden_layers):
        # Add regularization if specified
        if regularization == 'l1':
            reg = keras.regularizers.l1(0.01)
        elif regularization == 'l2':
            reg = keras.regularizers.l2(0.01)
        elif regularization == 'l1_l2':
            reg = keras.regularizers.l1_l2(l1=0.01, l2=0.01)
        else:
            reg = None

        # Add dense layer
        model.add(keras.layers.Dense(
            neurons_per_layer[i] if i < len(neurons_per_layer) else neurons_per_layer[-1],
            activation=activation,
            kernel_initializer=weight_initializer,
            kernel_regularizer=reg
        ))

    # Output layer (binary classification)
    model.add(keras.layers.Dense(1, activation='sigmoid'))

    # Configure optimizer
    if optimizer.lower() == 'adam':
        opt = keras.optimizers.Adam(learning_rate=learning_rate)
    elif optimizer.lower() == 'sgd':
        opt = keras.optimizers.SGD(learning_rate=learning_rate, momentum=momentum)
    elif optimizer.lower() == 'rmsprop':
        opt = keras.optimizers.RMSprop(learning_rate=learning_rate)
    else:
        opt = optimizer

    # Compile model
    model.compile(
        optimizer=opt,
        loss='binary_crossentropy',
        metrics=[
            'accuracy',
            keras.metrics.Precision(),
            keras.metrics.Recall(),
            keras.metrics.AUC()
        ]
    )

    # Define class weights for imbalanced data
    class_weight = {0: 1, 1: (y_train == 0).sum() / (y_train == 1).sum()}

    # Record start time
    start_time = time.time()

    # Train model
    history = model.fit(
        X_train, y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(X_val, y_val),
        class_weight=class_weight,
        verbose=1
    )

    # Calculate training time
    training_time = time.time() - start_time

    # Get final metrics
    train_metrics = model.evaluate(X_train, y_train, verbose=0)
    val_metrics = model.evaluate(X_val, y_val, verbose=0)

    # Calculate F1 and F2 scores
    train_precision = train_metrics[2]  # Precision is at index 2
    train_recall = train_metrics[3]     # Recall is at index 3
    val_precision = val_metrics[2]
    val_recall = val_metrics[3]

    # F1 = 2 * (precision * recall) / (precision + recall)
    train_f1 = 2 * (train_precision * train_recall) / (train_precision + train_recall + 1e-10)
    val_f1 = 2 * (val_precision * val_recall) / (val_precision + val_recall + 1e-10)

    # F2 = 5 * (precision * recall) / (4 * precision + recall)
    train_f2 = 5 * (train_precision * train_recall) / (4 * train_precision + train_recall + 1e-10)
    val_f2 = 5 * (val_precision * val_recall) / (4 * val_precision + val_recall + 1e-10)

    # Record results
    results = results.append({
        'model_id': model_id,
        'hidden_layers': hidden_layers,
        'neurons_per_layer': str(neurons_per_layer),
        'activation': activation,
        'epochs': epochs,
        'batch_size': batch_size,
        'optimizer': optimizer,
        'learning_rate': learning_rate,
        'momentum': momentum,
        'weight_initializer': weight_initializer,
        'regularization': regularization,
        'train_loss': train_metrics[0],
        'val_loss': val_metrics[0],
        'training_time': training_time
    }, ignore_index=True)

    results_metrics = results_metrics.append({
        'model_id': model_id,
        'train_accuracy': train_metrics[1],
        'val_accuracy': val_metrics[1],
        'train_precision': train_precision,
        'val_precision': val_precision,
        'train_recall': train_recall,
        'val_recall': val_recall,
        'train_f1': train_f1,
        'val_f1': val_f1,
        'train_f2': train_f2,
        'val_f2': val_f2,
        'train_auc': train_metrics[4],  # AUC is at index 4
        'val_auc': val_metrics[4]
    }, ignore_index=True)

    return model, history
```




This comprehensive helper function:

1. Creates two dataframes to track model architecture, hyperparameters, and performance metrics
2. Provides a flexible function to build, train, and evaluate neural network models
3. Handles class imbalance through class weights
4. Calculates important metrics like F1 and F2 scores
5. Records training time and all relevant model details

You can use this to systematically experiment with different model configurations and track their performance.
