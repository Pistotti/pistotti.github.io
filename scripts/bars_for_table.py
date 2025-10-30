import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# --- 1. Your Data ---
# Create a pandas DataFrame from your table data.
data = {
    'Language Pair': ['EN-ES (High)', 'EN-JA (Medium)', 'EN-MI (Low)'],
    'Median Perplexity': [21.60, 40.31, 148.72]
}
df = pd.DataFrame(data)

# --- 2. Plotting ---
# Set a professional style for the plot.
sns.set_theme(style="whitegrid")

# Create the figure and axes.
plt.figure(figsize=(8, 6))
ax = sns.barplot(
    x='Language Pair', 
    y='Median Perplexity', 
    data=df,
    palette='viridis' # A nice color palette, you can change this
)

# --- 3. Customization & Labels ---
# Add labels for clarity.
ax.set_xlabel('Language Resource Level', fontsize=12)
ax.set_ylabel('Median Perplexity (PPL)', fontsize=12)
ax.set_title('Baseline Perplexity for High-Quality Human Translations', fontsize=14, fontweight='bold')

# Add the exact values on top of each bar.
for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', 
                va='center', 
                xytext=(0, 9), 
                textcoords='offset points',
                fontsize=11)

# Ensure the y-axis starts at 0 for accurate representation.
ax.set_ylim(0, max(df['Median Perplexity']) * 1.15)

# --- 4. Save the Figure ---
# Save the figure in a high-quality format for your poster/thesis.
plt.savefig('perplexity_baseline_chart.png', dpi=300, bbox_inches='tight')
plt.savefig('perplexity_baseline_chart.pdf', bbox_inches='tight') # Also save as PDF for LaTeX

# Display the plot.
plt.show()