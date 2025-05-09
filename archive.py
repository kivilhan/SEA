import networkx as nx
import matplotlib.pyplot as plt

def visualize(manager):
    G = nx.DiGraph()

    # Add nodes
    for obj in manager.objects.values():
        G.add_node(obj.id, label=obj.name, obj_type=obj.obj_type)

    # Add edges
    for obj in manager.objects.values():
        for tgt in obj.satisfies:
            G.add_edge(obj.id, tgt, relation='satisfies')
        for tgt in obj.satisfied_by:
            G.add_edge(obj.id, tgt, relation='satisfied_by')
        for tgt in obj.verified_by:
            G.add_edge(obj.id, tgt, relation='verified_by')
        for tgt in obj.validated_by:
            G.add_edge(obj.id, tgt, relation='validated_by')

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'relation')
    nx.draw(G, pos, with_labels=False, node_size=1500, node_color='lightblue', arrows=True)
    nx.draw_networkx_labels(G, pos, labels={n: d['label'] for n, d in G.nodes(data=True)})
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()
