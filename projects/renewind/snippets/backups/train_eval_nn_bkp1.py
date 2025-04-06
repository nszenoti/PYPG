# Helper function to train model and record results
def train_and_evaluate_model(
    X_train,
    y_train,
    X_val,
    y_val,
    hidden_layers=1,
    neurons_per_layer=[16],
    activations=["relu"],
    epochs=50,
    batch_size=32,
    optimizer="adam",
    learning_rate=0.001,
    momentum=0.0,
    weight_initializer="he_normal",
    regularization=None,
    use_batch_norm=False,
    batch_norm_momentum=0.99,
    use_dropout=False,
    dropout_rates=0.2,
    model_id=None,
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
    use_batch_norm: Boolean or list of booleans for using batch normalization
    batch_norm_momentum: Momentum for batch normalization
    use_dropout: Boolean or list of booleans for using dropout
    dropout_rates: Float or list of floats for dropout rates
    model_id: Identifier for the model

    Returns:
    --------
    model: Trained Keras model
    history: Training history
    """
    global results, results_metrics

    # clears the current keras session, reseting all layers and models previously created, freeing up memory
    keras.backend.clear_session()

    # Generate model ID if not provided
    if model_id is None:
        model_id = f"model_{len(results) + 1}"

    # Input dimension
    input_dim = X_train.shape[1]

    # Convert single values to lists for layer-wise configuration
    if isinstance(use_batch_norm, bool):
        use_batch_norm = [use_batch_norm] * hidden_layers
    if isinstance(use_dropout, bool):
        use_dropout = [use_dropout] * hidden_layers
    if isinstance(dropout_rates, (int, float)):
        # is int or float
        dropout_rates = [dropout_rates] * hidden_layers

    # Create model
    model = keras.Sequential()

    # Input layer
    model.add(keras.layers.Input(shape=(input_dim,)))

    # Hidden layers
    for i in range(hidden_layers):
        # Get activation for this layer (use last one in list if not enough provided)
        layer_activation = activations[i] if i < len(activations) else activations[-1]

        # Get neurons for this layer
        neurons = (
            neurons_per_layer[i]
            if i < len(neurons_per_layer)
            else neurons_per_layer[-1]
        )

        # Add regularization if specified
        if regularization == "l1":
            reg = keras.regularizers.l1(0.01)
        elif regularization == "l2":
            reg = keras.regularizers.l2(0.01)
        elif regularization == "l1_l2":
            reg = keras.regularizers.l1_l2(l1=0.01, l2=0.01)
        else:
            reg = None

        # # Add dense layer
        # model.add(keras.layers.Dense(
        #     neurons_per_layer[i] if i < len(neurons_per_layer) else neurons_per_layer[-1],
        #     activation=layer_activation,
        #     kernel_initializer=weight_initializer,
        #     kernel_regularizer=reg
        # ))

        # Flow
        # Dense -> BatchNorm -> Activation -> Dropout

        # Add dense layer (without activation if using batch norm)
        if i < len(use_batch_norm) and use_batch_norm[i]:
            # When using batch norm, add the dense layer without activation
            model.add(
                keras.layers.Dense(
                    neurons,
                    activation=None,  # No activation yet
                    kernel_initializer=weight_initializer,
                    kernel_regularizer=reg,
                )
            )
            # Add batch normalization
            model.add(keras.layers.BatchNormalization(momentum=batch_norm_momentum))
            # Add activation separately (Activation applied after batch norm)
            model.add(keras.layers.Activation(layer_activation))
        else:
            # Standard dense layer with activation
            model.add(
                keras.layers.Dense(
                    neurons,
                    activation=layer_activation,
                    kernel_initializer=weight_initializer,
                    kernel_regularizer=reg,
                )
            )

        # Add dropout if specified for this layer
        if i < len(use_dropout) and use_dropout[i]:
            model.add(keras.layers.Dropout(dropout_rates[i]))

    # Output layer (binary classification)
    model.add(keras.layers.Dense(1, activation="sigmoid"))

    # Configure optimizer
    if optimizer.lower() == "adam":
        opt = keras.optimizers.Adam(learning_rate=learning_rate)
    elif optimizer.lower() == "sgd":
        opt = keras.optimizers.SGD(learning_rate=learning_rate, momentum=momentum)
    elif optimizer.lower() == "rmsprop":
        opt = keras.optimizers.RMSprop(learning_rate=learning_rate)
    else:
        opt = optimizer

    print(f"Model ID: {model_id}")
    print(model.summary())

    # Compile model
    model.compile(
        optimizer=opt,
        # Hard coded because we know its binary classification problem
        loss="binary_crossentropy",
        metrics=[
            # predicting a "no failure" when there is actually a failure) is costly,
            keras.metrics.Recall(),
            keras.metrics.Precision(),
            # F2 Score -> missing a failure is very costly, the F2 score provides a better overall evaluation metric than F1.
            keras.metrics.FbetaScore(beta=2.0),
        ],
    )

    # Define class weights for imbalanced data
    # class_weight = {0: 1, 1: (y_train == 0).sum() / (y_train == 1).sum()}

    # Calculate balanced class weights using scikit-learn

    class_weight = get_class_weights(y_train)

    # Record start time
    start_time = time.time()

    print("Started ...")

    # Train model
    history = model.fit(
        X_train,
        y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(X_val, y_val),
        class_weight=class_weight,
        verbose=1,
    )

    print("Finished !!!")

    # Calculate training time
    training_time = time.time() - start_time

    # Get final metrics
    train_metrics = model.evaluate(X_train, y_train, verbose=0)
    val_metrics = model.evaluate(X_val, y_val, verbose=0)

    # [loss, metric1, metric2, metric3, ...]
    #  |
    # [loss, recall, precision]   // for our case

    # Calculate F1 and F2 scores
    # train_recall = train_metrics[1]     # Recall is at index 1
    # train_precision = train_metrics[2]  # Precision is at index 2
    # val_recall = val_metrics[1]
    # val_precision = val_metrics[2]
    # train_f2 = train_metrics[3]    # F2(Fbeta) is at index 3
    # val_f2 = val_metrics[3]

    # F1 = 2 * (precision * recall) / (precision + recall)
    # train_f1 = 2 * (train_precision * train_recall) / (train_precision + train_recall + 1e-10)
    # val_f1 = 2 * (val_precision * val_recall) / (val_precision + val_recall + 1e-10)

    # # F2 = 5 * (precision * recall) / (4 * precision + recall)
    # train_f2 = 5 * (train_precision * train_recall) / (4 * train_precision + train_recall + 1e-10)
    # val_f2 = 5 * (val_precision * val_recall) / (4 * val_precision + val_recall + 1e-10)

    # Record results
    results = results.append(
        {
            "model_id": model_id,
            "hidden_layers": hidden_layers,
            "neurons_per_layer": str(neurons_per_layer),
            "activation": activations,
            "epochs": epochs,
            "batch_size": batch_size,
            "optimizer": optimizer,
            "learning_rate": learning_rate,
            "momentum": momentum,
            "weight_initializer": weight_initializer,
            "regularization": regularization,
            "train_loss": train_metrics[0],
            "val_loss": val_metrics[0],
            "training_time": training_time,
        },
        ignore_index=True,
    )

    results_metrics = results_metrics.append(
        {
            "model_id": model_id,
            "train_recall": train_metrics[1],
            "val_recall": val_metrics[1],
            "train_precision": train_metrics[2],
            "val_precision": val_metrics[2],
            "train_f2": train_metrics[3],
            "val_f2": val_metrics[3],
        },
        ignore_index=True,
    )

    return model, history
