import pandas as pd
from pyvis.network import Network
import colorsys

def hsl_to_hex(h, s, l):
    """Convert HSL color to hexadecimal (h: 0-360, s: 0-100, l: 0-100)"""
    h /= 360.0
    s /= 100.0
    l /= 100.0
    
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    return f"#{r:02x}{g:02x}{b:02x}"

# Read Excel file
df = pd.read_excel('netflix_data.xlsx')

# Create title mapping dictionary
title_map = df.set_index('N_id')['Title'].astype(str).to_dict()

# Process recommendations
edges = []
nodes = set()
recommendation_counts = {}

for _, row in df.iterrows():
    source = str(row['N_id']).strip()
    source_title = title_map.get(int(source), source)
    nodes.add(source_title)
    
    try:
        recommendations = [rec.strip() for rec in str(row['Recommendations']).split(',') if rec.strip()]
    except:
        recommendations = []
    
    for target in recommendations:
        target_title = title_map.get(int(target), target) if target.isdigit() else target
        edges.append((source_title, target_title))
        nodes.add(target_title)
        recommendation_counts[target_title] = recommendation_counts.get(target_title, 0) + 1

# Create network graph
net = Network(
    height='100vh',
    width='100%',
    bgcolor='#1a1a1a',
    directed=True,
    notebook=False
)

# Configure physics
net.set_options("""
{
  "physics": {
    "forceAtlas2Based": {
      "gravitationalConstant": -100,
      "centralGravity": 0.01,
      "springLength": 100,
      "springConstant": 0.08
    },
    "minVelocity": 0.75,
    "solver": "forceAtlas2Based",
    "timestep": 0.5
  },
  "edges": {
    "smooth": false,
    "arrows": {
      "to": {
        "enabled": true,
        "scaleFactor": 0.5
      }
    }
  }
}
""")

# Calculate color gradient parameters
max_count = max(recommendation_counts.values(), default=1)

# Add nodes with color gradient
for node in nodes:
    count = recommendation_counts.get(node, 0)
    
    # Calculate color gradient (red to green)
    hue = (count / max_count) * 120  # 0 (red) to 120 (green)
    color = hsl_to_hex(hue, 100, 50)
    
    net.add_node(
        node,
        size=10 + count*2,
        color=color,
        title=f"{node}\nRecommendations Received: {count}",
        shape='dot'
    )

# Add edges
for source, target in edges:
    net.add_edge(
        source,
        target,
        color='rgba(150, 150, 150, 0.3)',
        width=1,
        arrows='to'
    )

# Save and open
net.write_html('movie_network.html', local=True)
print("""
Visualization complete! Open movie_network.html in your browser.
- Color gradient: Red (few recommendations) → Green (many recommendations)
- Node size grows with recommendation count
- Hover over nodes to see details
- Drag nodes to explore connections
""")




#this creates the final html file for visualization with input xlsx file