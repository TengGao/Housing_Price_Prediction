from plotly import tools
import plotly.graph_objs as go 
import numpy as np 
def histogram_grid(data, histfunc='count', asFigure=False, **layout):
    # Add Histogram function soon
    num_rows = data.shape[1]//2+1
    fig = tools.make_subplots(rows=num_rows, cols=2, print_grid=False,
                              subplot_titles=(data.columns))

    for i, col in enumerate(data.columns):
        
        count = data[col].value_counts()
        trace = go.Bar(x=count.index, y=count.values)
        fig.append_trace(trace, i//2+1, i%2+1)
    fig['layout'].update(height=num_rows*500, width=1200, showlegend=False, template='plotly_dark', title='Value Counts Per Columns')
    fig['layout'].update(layout)
    if asFigure:
        return fig
    else:
        iplot(fig)