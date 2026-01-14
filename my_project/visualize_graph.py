#!/usr/bin/env python3
"""
Quick script to visualize GraphRAG graph.graphml file
"""

import sys
from pathlib import Path

try:
    import networkx as nx
except ImportError:
    print("Error: networkx not installed. Install with: pip install networkx")
    sys.exit(1)

try:
    from pyvis.network import Network
    PYVIS_AVAILABLE = True
except ImportError:
    PYVIS_AVAILABLE = False
    print("Note: pyvis not installed. Install with: pip install pyvis for interactive HTML visualization")

try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("Note: matplotlib not installed. Install with: pip install matplotlib for static visualization")


def visualize_with_pyvis(graphml_path: Path, output_path: Path):
    """Create interactive HTML visualization using Pyvis"""
    print(f"Reading graph from {graphml_path}...")
    G = nx.read_graphml(graphml_path)
    
    print(f"Graph loaded: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    
    # Create Pyvis network
    net = Network(height='800px', width='100%', bgcolor='#222222', font_color='white')
    net.from_nx(G)
    
    # Configure physics
    net.set_options("""
    {
      "physics": {
        "enabled": true,
        "barnesHut": {
          "gravitationalConstant": -80000,
          "centralGravity": 0.3,
          "springLength": 200,
          "springConstant": 0.04
        }
      }
    }
    """)
    
    # Save
    net.save_graph(str(output_path))
    print(f"✅ Interactive graph saved to: {output_path}")
    print("   Open the HTML file in your browser to view!")


def visualize_with_matplotlib(graphml_path: Path, output_path: Path):
    """Create static PNG visualization using matplotlib"""
    print(f"Reading graph from {graphml_path}...")
    G = nx.read_graphml(graphml_path)
    
    print(f"Graph loaded: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    
    # Create figure
    plt.figure(figsize=(20, 20))
    
    # Calculate layout
    print("Calculating layout (this may take a moment)...")
    pos = nx.spring_layout(G, k=1, iterations=50)
    
    # Draw
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=500, alpha=0.6)
    nx.draw_networkx_edges(G, pos, alpha=0.2, width=0.5)
    nx.draw_networkx_labels(G, pos, font_size=8)
    
    plt.title("Knowledge Graph Visualization", fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    
    # Save
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Static graph saved to: {output_path}")


def print_graph_info(graphml_path: Path):
    """Print basic graph statistics"""
    G = nx.read_graphml(graphml_path)
    
    print("\n" + "="*50)
    print("Graph Statistics")
    print("="*50)
    print(f"Nodes: {G.number_of_nodes()}")
    print(f"Edges: {G.number_of_edges()}")
    print(f"Is connected: {nx.is_connected(G)}")
    
    if G.number_of_nodes() > 0:
        degrees = dict(G.degree())
        print(f"Average degree: {sum(degrees.values()) / len(degrees):.2f}")
        print(f"Max degree: {max(degrees.values())}")
        print(f"Min degree: {min(degrees.values())}")
    
    print("="*50 + "\n")


def main():
    # Determine paths
    script_dir = Path(__file__).parent
    graphml_path = script_dir / "output" / "graph.graphml"
    
    if not graphml_path.exists():
        print(f"❌ Error: GraphML file not found at {graphml_path}")
        print("   Make sure you've run indexing first!")
        sys.exit(1)
    
    # Print graph info
    print_graph_info(graphml_path)
    
    # Try interactive visualization first
    if PYVIS_AVAILABLE:
        output_html = script_dir / "output" / "graph_interactive.html"
        visualize_with_pyvis(graphml_path, output_html)
        return
    
    # Fallback to matplotlib
    if MATPLOTLIB_AVAILABLE:
        output_png = script_dir / "output" / "graph_visualization.png"
        visualize_with_matplotlib(graphml_path, output_png)
        return
    
    # If neither available, just print info
    print("No visualization libraries available.")
    print("Install one of:")
    print("  - pip install pyvis (for interactive HTML)")
    print("  - pip install matplotlib (for static PNG)")


if __name__ == "__main__":
    main()

