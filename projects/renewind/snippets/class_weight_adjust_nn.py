from sklearn.utils.class_weight import compute_class_weight

# Compute class weights
class_weights = compute_class_weight('balanced', classes=[0, 1], y=y_train)
class_weights = dict(zip([0, 1], class_weights))

model.fit(X_train, y_train, class_weight=class_weights)