import numpy as np
from scipy import stats

import plotly.graph_objs as go
import plotly.offline as offline


# Plot the Normal Distribution 
xs = np.linspace(-4, 4, 100)

fig = go.FigureWidget()
fig.add_scatter(x=xs,y=stats.norm.pdf(xs), line=dict(shape='spline'))
offline.plot(fig, show_link=False)


