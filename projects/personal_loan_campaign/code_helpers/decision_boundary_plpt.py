import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from matplotlib.colors import ListedColormap

# Generate synthetic dataset
X, y = make_classification(n_features=2, n_classes=2, n_clusters_per_class=1, n_redundant=0, random_state=42)

# Train Decision Tree Classifier
clf = DecisionTreeClassifier(max_depth=3)
clf.fit(X, y)

# Define function to plot decision boundary
def plot_decision_boundary(model, X, y):
    h = 0.02  # Step size in the mesh grid
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    # Get predictions for each point in the grid
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot decision boundary
    plt.contourf(xx, yy, Z, alpha=0.3, cmap=ListedColormap(['lightblue', 'lightcoral']))
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', cmap=ListedColormap(['blue', 'red']))
    plt.title("Decision Boundary Plot")
    plt.show()

# Plot the decision boundary
plot_decision_boundary(clf, X, y)
