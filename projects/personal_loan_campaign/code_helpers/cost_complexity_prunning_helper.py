import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


def perform_cost_complexity_pruning(X_train, X_val, y_train, y_val, max_depth=None):
    """
    Perform cost complexity pruning and analyze the results.

    Parameters:
    -----------
    X_train, X_val : Training and validation features
    y_train, y_val : Training and validation labels
    max_depth : Maximum depth of the initial tree

    Returns:
    --------
    optimal_tree : The optimally pruned decision tree
    """
    # Train initial tree
    tree = DecisionTreeClassifier(max_depth=max_depth)
    tree.fit(X_train, y_train)

    # Get the path of pruned trees
    path = tree.cost_complexity_pruning_path(X_train, y_train)
    ccp_alphas, impurities = path.ccp_alphas, path.impurities

    # Create trees with different values of ccp_alpha
    trees = []
    for ccp_alpha in ccp_alphas:
        dt = DecisionTreeClassifier(max_depth=max_depth, ccp_alpha=ccp_alpha)
        dt.fit(X_train, y_train)
        trees.append(dt)

    # Remove the last element as it's an empty tree
    trees = trees[:-1]
    ccp_alphas = ccp_alphas[:-1]

    # Calculate accuracy scores
    train_scores = [accuracy_score(y_train, tree.predict(X_train)) for tree in trees]
    val_scores = [accuracy_score(y_val, tree.predict(X_val)) for tree in trees]

    # Get number of nodes for each tree
    tree_depths = [tree.get_depth() for tree in trees]
    node_counts = [tree.get_n_leaves() for tree in trees]

    # Plot results
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    # Plot accuracy vs alpha
    ax1.set_xlabel("ccp alpha")
    ax1.set_ylabel("Accuracy")
    ax1.plot(ccp_alphas, train_scores, marker="o", label="train")
    ax1.plot(ccp_alphas, val_scores, marker="o", label="validation")
    ax1.legend()
    ax1.set_title("Accuracy vs ccp_alpha")

    # Plot tree complexity vs alpha
    ax2.set_xlabel("ccp alpha")
    ax2.set_ylabel("Number of nodes")
    ax2.plot(ccp_alphas, node_counts, marker="o")
    ax2.set_title("Tree complexity vs ccp_alpha")

    plt.tight_layout()

    # Find optimal alpha
    best_val_score_idx = np.argmax(val_scores)
    optimal_alpha = ccp_alphas[best_val_score_idx]

    print(f"Optimal ccp_alpha: {optimal_alpha:.6f}")
    print(f"Number of nodes in optimal tree: {node_counts[best_val_score_idx]}")
    print(f"Best validation accuracy: {val_scores[best_val_score_idx]:.4f}")

    # Return the optimal tree
    return trees[best_val_score_idx]


# Example usage
def demo_cost_complexity_pruning(X_train, X_val, y_train, y_val):
    """
    Demonstrate the complete cost complexity pruning workflow.
    """
    # Train initial unpruned tree
    initial_tree = DecisionTreeClassifier()
    initial_tree.fit(X_train, y_train)

    initial_train_score = accuracy_score(y_train, initial_tree.predict(X_train))
    initial_val_score = accuracy_score(y_val, initial_tree.predict(X_val))

    print("Initial Tree:")
    print(f"Number of nodes: {initial_tree.get_n_leaves()}")
    print(f"Training accuracy: {initial_train_score:.4f}")
    print(f"Validation accuracy: {initial_val_score:.4f}")
    print("\nPerforming cost complexity pruning...")

    # Perform pruning
    pruned_tree = perform_cost_complexity_pruning(X_train, X_val, y_train, y_val)

    final_train_score = accuracy_score(y_train, pruned_tree.predict(X_train))
    final_val_score = accuracy_score(y_val, pruned_tree.predict(X_val))

    print("\nPruned Tree:")
    print(f"Number of nodes: {pruned_tree.get_n_leaves()}")
    print(f"Training accuracy: {final_train_score:.4f}")
    print(f"Validation accuracy: {final_val_score:.4f}")

    return pruned_tree