# Hướng dẫn Visualize GraphML Files

File `graph.graphml` đã được tạo trong thư mục `output/`. Dưới đây là các cách để visualize nó:

## Phương pháp 1: Gephi (Khuyến nghị - Desktop App)

### Bước 1: Cài đặt Gephi
1. Tải Gephi từ: https://gephi.org/users/download/
2. Cài đặt và mở Gephi

### Bước 2: Import GraphML
1. Mở Gephi
2. Chọn `File` -> `Open...`
3. Điều hướng đến `my_project/output/graph.graphml`
4. Chọn file và click `Open`

### Bước 3: Cài đặt Plugin Leiden Algorithm
1. Vào `Tools` -> `Plugins`
2. Tìm "Leiden Algorithm"
3. Click `Install` và restart Gephi

### Bước 4: Chạy Statistics
1. Trong tab `Statistics` (bên phải), click `Run` cho:
   - `Average Degree`
   - `Leiden Algorithm`
2. Với Leiden Algorithm, đặt:
   - **Quality function**: Modularity
   - **Resolution**: 1

### Bước 5: Tô màu theo Clusters
1. Vào `Appearance` pane (góc trên bên trái)
2. Chọn `Nodes` -> `Partition`
3. Click icon color palette (góc trên bên phải)
4. Chọn `Cluster` từ dropdown
5. Click `Palette...` -> `Generate...`
6. Uncheck `Limit number of colors`, click `Generate`, rồi `Ok`
7. Click `Apply` để tô màu graph

### Bước 6: Resize Nodes theo Degree
1. Trong `Appearance` pane, chọn `Nodes` -> `Ranking`
2. Chọn icon `Sizing` (góc trên bên phải)
3. Chọn `Degree` và đặt:
   - **Min**: 10
   - **Max**: 150
4. Click `Apply`

### Bước 7: Layout Graph
1. Trong tab `Layout` (góc dưới bên trái), chọn `OpenORD`
2. Đặt `Liquid` và `Expansion` stages = 50, các cái khác = 0
3. Click `Run` và đợi

### Bước 8: Chạy ForceAtlas2
1. Chọn `Force Atlas 2` trong layout options
2. Đặt settings:
   - **Scaling**: 15
   - **Dissuade Hubs**: checked
   - **LinLog mode**: unchecked
   - **Prevent Overlap**: checked
3. Click `Run` và đợi
4. Click `Stop` khi nodes đã ổn định

### Bước 9: Thêm Labels (Tùy chọn)
1. Bật text labels trong phần tương ứng
2. Cấu hình và resize theo nhu cầu

---

## Phương pháp 2: Python với NetworkX và Matplotlib

Tạo file Python script để visualize:

```python
import networkx as nx
import matplotlib.pyplot as plt

# Đọc GraphML file
G = nx.read_graphml('output/graph.graphml')

# Tạo visualization
plt.figure(figsize=(20, 20))
pos = nx.spring_layout(G, k=1, iterations=50)

# Vẽ nodes và edges
nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                       node_size=500, alpha=0.6)
nx.draw_networkx_edges(G, pos, alpha=0.2)
nx.draw_networkx_labels(G, pos, font_size=8)

plt.title("Knowledge Graph Visualization")
plt.axis('off')
plt.tight_layout()
plt.savefig('output/graph_visualization.png', dpi=300, bbox_inches='tight')
plt.show()
```

Chạy script:
```bash
python visualize_graph.py
```

---

## Phương pháp 3: Python với Pyvis (Interactive HTML)

```python
import networkx as nx
from pyvis.network import Network

# Đọc GraphML
G = nx.read_graphml('output/graph.graphml')

# Tạo Pyvis network
net = Network(height='800px', width='100%', bgcolor='#222222', font_color='white')
net.from_nx(G)

# Thêm physics options
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

# Lưu và mở
net.save_graph('output/graph_interactive.html')
print("Graph saved to output/graph_interactive.html")
print("Open the HTML file in your browser!")
```

Cài đặt Pyvis:
```bash
pip install pyvis
```

---

## Phương pháp 4: Cytoscape (Desktop App)

1. Tải Cytoscape từ: https://cytoscape.org/download.html
2. Mở Cytoscape
3. `File` -> `Import` -> `Network from File`
4. Chọn `graph.graphml`
5. Graph sẽ được hiển thị với các layout options có sẵn

---

## Phương pháp 5: Online Tools

### yEd Graph Editor
1. Truy cập: https://www.yworks.com/products/yed
2. Tải yEd (free)
3. `File` -> `Open...` -> Chọn `graph.graphml`
4. Sử dụng `Layout` menu để áp dụng các layout algorithms

### Graphviz Online
1. Truy cập: https://dreampuf.github.io/GraphvizOnline/
2. Convert GraphML sang DOT format trước (cần script Python)

---

## Phương pháp 6: Jupyter Notebook với yfiles-jupyter-graphs

Xem example notebook tại:
`examples_notebooks/community_contrib/yfiles-jupyter-graphs/graph-visualization.ipynb`

```python
import pandas as pd
import networkx as nx
from yfiles_jupyter_graphs import GraphWidget

# Đọc GraphML
G = nx.read_graphml('output/graph.graphml')

# Convert sang format cho yfiles
w = GraphWidget()
w.nodes = [{"id": node, "properties": {"label": node}} for node in G.nodes()]
w.edges = [{"start": u, "end": v} for u, v in G.edges()]
w.directed = False
w.node_label_mapping = "label"

display(w)
```

---

## Quick Start Commands

### Xem GraphML file bằng text editor:
```bash
# Windows PowerShell
Get-Content my_project\output\graph.graphml | Select-Object -First 50

# Linux/Mac
head -50 my_project/output/graph.graphml
```

### Kiểm tra số lượng nodes và edges:
```python
import networkx as nx
G = nx.read_graphml('my_project/output/graph.graphml')
print(f"Nodes: {G.number_of_nodes()}")
print(f"Edges: {G.number_of_edges()}")
```

---

## Lưu ý

- File GraphML của bạn đã có sẵn tại: `my_project/output/graph.graphml`
- GraphML là format chuẩn, có thể mở bằng nhiều tools khác nhau
- Nếu muốn tạo lại GraphML với các tùy chọn khác, cập nhật `settings.yaml`:
  ```yaml
  snapshots:
    graphml: true  # Đã được bật
  ```

