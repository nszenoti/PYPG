import matplotlib.pyplot as plt
import seaborn as sns
import mplcursors


# Set global figure size for all plots
plt.rcParams['figure.figsize'] = (10, 6)

# Set global font for titles, labels, etc.
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 12

# Set global color cycle for lines (this will affect line color in most plots)
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'])

# Set the grid style globally (for both major and minor grids)
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.6
plt.rcParams['grid.color'] = 'gray'

# Set the spine (border) style for all axes
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

# Set global font sizes for title, xlabel, and ylabel
plt.rcParams['axes.titlesize'] = 16  # Default font size for plot titles
plt.rcParams['axes.labelsize'] = 14  # Default font size for x and y labels

# ----

# Set global Seaborn style and context
sns.set_theme(style="whitegrid", palette="muted", context="talk")

# Alternatively, you can customize more specific themes:
# sns.set_context("paper")   # For printing
# sns.set_palette("pastel")  # Set the color palette

'''
Here’s a breakdown of options for sns.set_theme():

style: Controls background color and gridlines (options: "darkgrid", "whitegrid", "dark", "white", "ticks").
palette: Defines the color palette (options: "deep", "muted", "pastel", etc.).
context: Sets the size of plot elements (options: "paper", "notebook", "talk", "poster").
'''
# ----
# 3.1 Title, Labels, and Font Customization
# Customize titles and axis labels
def customize_labels(ax, title, xlabel, ylabel):
    ax.set_title(title, fontsize=16, fontweight='bold', loc='center')
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)

# ---
# 3.2 Improving Legend Placement
def customize_legend(ax):
    ax.legend(loc='best', fontsize=12, frameon=False)  # 'best' places the legend in the optimal location

# ---
# 3.3 Control Plot Layout
plt.tight_layout()  # Adjusts subplots to give more space to labels, etc.

# --------
# --------

# 4. Color Palettes and Style for Aesthetics

# Set color palette for seaborn
sns.set_palette("Blues")  # Change to any palette like "Set1", "husl", "muted", etc.
# Set custom colors for individual plots
sns.set_palette(["#2ca02c", "#d62728", "#1f77b4"])  # Custom hex color codes

# --------
# --------

# 5. Ticks and Tick Labels

# Customize ticks and their labels
def customize_ticks(ax):
    ax.tick_params(axis='x', direction='in', length=6)
    ax.tick_params(axis='y', direction='in', length=6)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')  # Rotate labels for better visibility

# --------
# --------
#6. Use Subplots for Multiple Plots
#If you want to display multiple plots side by side, use plt.subplots() for an organized layout. This avoids overlapping and keeps your visualizations neat.
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plotting on the first subplot
sns.lineplot(ax=axes[0], x=x, y=y)
axes[0].set_title("Line Plot")

# Plotting on the second subplot
sns.scatterplot(ax=axes[1], x=x, y=y)
axes[1].set_title("Scatter Plot")

plt.tight_layout()  # Adjust the layout
plt.show()

# --------
# --------
# 7. Remove Redundant Axis Labels in Subplots

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot on the first subplot
sns.lineplot(ax=axes[0], x=x, y=y)
axes[0].set_title("Line Plot")
axes[0].set_xlabel('')  # Remove redundant xlabel
axes[0].set_ylabel('')  # Remove redundant ylabel

# Plot on the second subplot
sns.scatterplot(ax=axes[1], x=x, y=y)
axes[1].set_title("Scatter Plot")
axes[1].set_xlabel('')  # Remove redundant xlabel
axes[1].set_ylabel('')  # Remove redundant ylabel

plt.tight_layout()
plt.show()

# --------
# --------
#8. Improving Plot Clarity with Gridlines and Background
# Set white background and customize gridlines for better contrast
sns.set(style="whitegrid")

# If you prefer a minimal grid
sns.set_style("white")

# alternativeky
# Remove gridlines
plt.grid(False)

# --------
# --------
# 9. Bar Plot Aesthetics

sns.barplot(x=['A', 'B', 'C'], y=[10, 20, 30], palette='coolwarm')

# Adjust bar width and add annotations
for index, value in enumerate([10, 20, 30]):
    plt.text(index, value + 0.5, str(value), ha='center', fontsize=12)

# --------
# --------
# 10. Make Plots Interactive with mplcursors
# !pip install mplcursors

# Example usage with a scatter plot
fig, ax = plt.subplots()
scatter = ax.scatter(x, y)

# Make plot interactive
mplcursors.cursor(scatter, hover=True)
plt.show()
