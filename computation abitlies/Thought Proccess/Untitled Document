import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph for the bubble diagram
G = nx.DiGraph()

# Define the main topic
main_topic = "Retention and Learning Mechanisms"
G.add_node(main_topic, shape="ellipse", color="lightblue", style="filled")

# Define subtopics
subtopics = [
    "Encoding Information",
    "Consolidation of Memories",
    "Types of Memory",
    "Forgetting and Retrieval",
    "Effective Study Techniques",
]

# Add subtopics as nodes and connect them to the main topic
for subtopic in subtopics:
    G.add_node(subtopic, shape="ellipse", color="lightyellow", style="filled")
    G.add_edge(main_topic, subtopic, arrowhead="normal", color="gray")

# Define relationships or connections between subtopics
relationships = [
    ("Encoding Information", "Sensory Memory"),
    ("Encoding Information", "Working Memory"),
    ("Consolidation of Memories", "Short-term Memory"),
    ("Consolidation of Memories", "Long-term Memory"),
    ("Effective Study Techniques", "Spaced Repetition"),
    ("Effective Study Techniques", "Active Recall"),
]

# Add relationships as edges between subtopics
for source, target in relationships:
    G.add_edge(source, target, arrowhead="normal", color="gray")

# Draw and visualize the bubble diagram
pos = nx.spring_layout(G, seed=42)  # Layout for better visualization
node_labels = {node: node for node in G.nodes()}
edge_labels = {(source, target): "" for source, target in G.edges()}

# Draw nodes, edges, labels, and styles
nx.draw_networkx_nodes(G, pos, node_color=[G.nodes[node]["color"] for node in G.nodes()])
nx.draw_networkx_edges(G, pos, edge_color=[G.edges[edge]["color"] for edge in G.edges()])
nx.draw_networkx_labels(G, pos, labels=node_labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="gray")

# Remove axis labels and display the bubble diagram
plt.axis("off")
plt.show()

