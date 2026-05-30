from app import app


def test_header_present():
    # 1. Verify the header is present and has the correct text
    layout = app.layout

    # Extract components from the nested layout structure
    card_children = layout.children[0].children
    h1_header = card_children[0]

    assert h1_header.children == "Soul Foods Sales Visualizer"


def test_visualization_present():
    # 2. Verify the visualization component is present by checking its ID
    layout = app.layout
    card_children = layout.children[0].children
    graph_component = card_children[3]  # dcc.Graph element

    assert graph_component.id == "sales-line-chart"


def test_region_picker_present():
    # 3. Verify the region picker component is present by checking its ID
    layout = app.layout
    card_children = layout.children[0].children
    filter_div = card_children[2]
    radio_items = filter_div.children[1]  # dcc.RadioItems element

    assert radio_items.id == "region-filter"