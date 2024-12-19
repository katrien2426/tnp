import matplotlib.pyplot as plt
import networkx as nx

def create_tree_layout(level):
    G = nx.Graph()
    pos = {}
    
    # 添加节点
    nodes = []
    y_spacing = 1.0
    current_level = 0
    nodes_in_level = 1
    node_count = 0
    
    while current_level <= level:
        x_spacing = 1.0 / (nodes_in_level + 1)
        level_nodes = []
        for i in range(nodes_in_level):
            G.add_node(node_count)
            pos[node_count] = (x_spacing * (i + 1), 1 - current_level * y_spacing / (level + 1))
            level_nodes.append(node_count)
            if current_level > 0 and len(nodes) > 0:
                # 连接到父节点
                parent = nodes[-nodes_in_level//2 + i//2]
                G.add_edge(parent, node_count)
            node_count += 1
        nodes.extend(level_nodes)
        current_level += 1
        nodes_in_level *= 2
    
    return G, pos

def draw_decision_tree(filename, level=2, title=""):
    plt.figure(figsize=(10, 8))
    G, pos = create_tree_layout(level)
    
    # 绘制边
    nx.draw_networkx_edges(G, pos, edge_color='gray')
    
    # 绘制节点
    node_colors = ['#4299E1'] + ['#48BB78']*2 + ['#ED64A6']*4
    nx.draw_networkx_nodes(G, pos, 
                          node_color=node_colors[:len(G.nodes())],
                          node_size=1000)
    
    # 添加标签
    labels = {0: 'Root'}
    for i in range(1, 3):
        labels[i] = chr(ord('A') + i - 1)
    for i in range(3, 7):
        labels[i] = chr(ord('C') + i - 3)
    nx.draw_networkx_labels(G, pos, labels, font_color='white')
    
    if title:
        plt.title(title, fontsize=16, pad=20)
    
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight', dpi=100)
    plt.close()

# 生成三张不同的树图
titles = [
    "Initial decision tree structure",
    "Characteristic fission process",
    "Feature importance score"
]

for i, title in enumerate(titles, 1):
    draw_decision_tree(f'img/tree{i}.png', level=2, title=title)
