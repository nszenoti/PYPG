import seaborn as sns
import matplotlib.pyplot as plt

# Set global style
sns.set_theme(style="whitegrid")  # Options: white, darkgrid, ticks

# Initialize figure size
plt.figure(figsize=(10, 6))

# Plot type (change based on needs, e.g., sns.histplot, sns.boxplot, etc.)
ax = sns.barplot(data=df, x="x_column", y="y_column", palette="viridis")

# Add title and axis labels
ax.set_title("Descriptive Title", fontsize=16, fontweight='bold')
ax.set_xlabel("X-axis Label", fontsize=12)
ax.set_ylabel("Y-axis Label", fontsize=12)

# Rotate x-axis labels (if needed)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

# Annotate bars (for barplots)
for p in ax.patches:
    ax.annotate(f'{p.get_height():.1f}', (p.get_x() + p.get_width() / 2, p.get_height()),
                ha='center', va='bottom', fontsize=10)

# Save plot (optional)
plt.savefig("plot_name.png", dpi=300, bbox_inches='tight')

# Show plot
plt.show()

# Avoid clipping
plt.tight_layout()
