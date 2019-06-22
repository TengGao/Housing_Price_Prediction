from plotly import tools
import plotly.graph_objs as go 
from plotly.offline import iplot 
import cufflinks as cf 
cf.set_config_file(offline=True)
import numpy as np 
from math import ceil


def histogram_grid(data, histfunc='count', asFigure=False, **layout):
    # Add Histogram function soon
    num_rows = data.shape[1]//2+1
    fig = tools.make_subplots(rows=num_rows, cols=2, print_grid=False,
                              subplot_titles=(data.columns))

    title = 'Value Counts Per Columns' if histfunc=='count' else 'Distribution Per Columns'

    for i, col in enumerate(data.columns):
        if histfunc == 'count':
            count = data[col].value_counts()
            trace = go.Bar(x=count.index, y=count.values)
        elif histfunc == 'sum':
            trace = go.Histogram(x=data[col])
        fig.append_trace(trace, i//2+1, i%2+1)
    fig['layout'].update(height=num_rows*500, width=1200, showlegend=False, template='plotly_dark', title=title)
    fig['layout'].update(layout)
    if asFigure:
        return fig
    else:
        iplot(fig)

def scatter_target_plot(data, select_columns, target, num_cols=3, asFigure=False, **layout):
    num_rows = ceil(len(select_columns)/num_cols)
    fig = tools.make_subplots(rows=num_rows, cols=num_cols, print_grid=False, subplot_titles=numeric_columns)
    for i, col in enumerate(select_columns):
        fig.append_trace(
            go.Scatter(x=data[col], y=data[target], mode='markers'),
            row = i//num_cols+1,
            col = i%num_cols+1
        )

    fig['layout'].update(
        height=num_rows*500, 
        width=1200, 
        showlegend=False, 
        template='plotly_dark', 
        title=f'Select Columns Value VS {target}')
    if asFigure:
        return fig
    else:
        iplot(fig)