import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from sklearn.ensemble import RandomForestRegressor
import matplotlib.patches as patches

# Create sample data with known feature importance
np.random.seed(42)
n_samples = 1000
n_features = 4
feature_names = ['Feature A', 'Feature B', 'Feature C', 'Feature D']

# Create synthetic data where Feature A and C are more important
X = np.random.randn(n_samples, n_features)
y = 2 * X[:, 0] + 0.5 * X[:, 2] + np.random.normal(0, 0.1, n_samples)

# Create figure
plt.style.use('seaborn-v0_8-darkgrid')
fig = plt.figure(figsize=(10, 6))  
gs = plt.GridSpec(2, 2, width_ratios=[1, 1], height_ratios=[1, 1])

# 左边的树
ax_tree = fig.add_subplot(gs[:, 0])  
# 右边上方的置换过程
ax_perm = fig.add_subplot(gs[0, 1])
# 右边下方的重要性分数
ax_imp = fig.add_subplot(gs[1, 1])

def draw_tree(ax, depth=3, highlight_feature=None):
    """Draw a simple tree structure"""
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    
    def draw_node(x, y, feature=None, is_highlighted=False):
        size = 0.07  
        color = 'lightcoral' if is_highlighted else 'skyblue'
        circle = plt.Circle((x, y), size, color=color, ec='navy', alpha=0.7)
        ax.add_patch(circle)
        if feature:
            ax.text(x, y, feature, ha='center', va='center', fontsize=10)
    
    # Draw root
    draw_node(0.5, 0.9, 'Root', highlight_feature=='root')
    
    # Level 1
    draw_node(0.3, 0.6, feature_names[0], highlight_feature==feature_names[0])
    draw_node(0.7, 0.6, feature_names[1], highlight_feature==feature_names[1])
    ax.plot([0.5, 0.3], [0.85, 0.65], 'k-', alpha=0.5, linewidth=2)
    ax.plot([0.5, 0.7], [0.85, 0.65], 'k-', alpha=0.5, linewidth=2)
    
    # Level 2
    draw_node(0.2, 0.3, feature_names[2], highlight_feature==feature_names[2])
    draw_node(0.4, 0.3, feature_names[3], highlight_feature==feature_names[3])
    ax.plot([0.3, 0.2], [0.55, 0.35], 'k-', alpha=0.5, linewidth=2)
    ax.plot([0.3, 0.4], [0.55, 0.35], 'k-', alpha=0.5, linewidth=2)

def draw_permutation(ax, feature_idx, step):
    """Draw permutation process"""
    ax.clear()
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-0.5, 3.5)
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Draw original data points
    for i in range(4):
        color = 'lightcoral' if i == feature_idx and step > 0 else 'skyblue'
        rect = patches.Rectangle((i-0.3, 0), 0.6, 2, 
                               facecolor=color, alpha=0.3)
        ax.add_patch(rect)
        ax.text(i, 2.5, f'Feature {chr(65+i)}', ha='center', fontsize=10)
    
    if step > 0:
        ax.text(0.5, -0.3, 'Permuting values\nto measure importance', 
                ha='center', va='top', fontsize=10)

def update(frame):
    feature_idx = frame // 3
    step = frame % 3
    
    # Update tree visualization
    draw_tree(ax_tree, highlight_feature=feature_names[feature_idx] if step > 0 else None)
    ax_tree.set_title('Decision Tree Structure', pad=10, fontsize=12)
    
    # Update permutation visualization
    draw_permutation(ax_perm, feature_idx, step)
    ax_perm.set_title('Feature Permutation', pad=10, fontsize=12)
    
    # Update importance scores
    ax_imp.clear()
    importances = np.zeros(n_features)
    if step == 2:
        rf = RandomForestRegressor(n_estimators=10, random_state=42)
        rf.fit(X, y)
        importances = rf.feature_importances_
        
    bars = ax_imp.bar(feature_names[:feature_idx+1], 
                      importances[:feature_idx+1],
                      color='lightcoral', alpha=0.6)
    ax_imp.set_ylim(0, 0.8)
    ax_imp.set_title('Feature Importance', pad=10, fontsize=12)
    ax_imp.set_xlabel('Features', fontsize=10)
    ax_imp.set_ylabel('Importance', fontsize=10)
    ax_imp.tick_params(axis='both', which='major', labelsize=8)
    
    # Add explanation text
    texts = [
        "Starting importance calculation...",
        "Permuting feature values...",
        "Measuring prediction change..."
    ]
    if step < len(texts):
        plt.figtext(0.5, 0.02, texts[step], ha='center', fontsize=10,
                   bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
    
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    return ax_tree.patches + ax_perm.patches + bars.patches

# Create animation
anim = FuncAnimation(fig, update, frames=12, 
                    interval=1000, blit=True)

# Create save directory if it doesn't exist
import os
os.makedirs('img', exist_ok=True)

# Save animation
writer = PillowWriter(fps=1)
anim.save('img/feature_importance_process.gif', writer=writer)
plt.close()
