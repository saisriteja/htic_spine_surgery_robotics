import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# data = np.load("freedrive_force_data_linear_3.npy",allow_pickle=True)

data = np.load("/home/saisriteja/notebooks/ee_attached_force_data.npy",allow_pickle=True)

fx,fy,fz,tx,ty,tz,velocities_joints,endeffector_position,endeffector_speed = data


endeffector_position = np.array(list(endeffector_position))

resultant_force  = [np.linalg.norm(np.abs([ifx,ify,ifz])) for ifx,ify,ifz in zip(fx,fy,fz) ]
resultant_torque  = [np.linalg.norm(np.abs([itx,ity,itz])) for itx,ity,itz in zip(tx,ty,tz) ]


x = [i for i in range(len(fx))]


# fig = go.Figure()
# Create and style traces

fig = make_subplots(rows=2, cols=1, start_cell="top-left")

fig.add_trace(go.Scatter(x=x, y=fx, name='fx',
                         line=dict(color='firebrick', width=4,dash = 'dashdot')),row=1, col=1)
fig.add_trace(go.Scatter(x=x, y=fy, name = 'fy',
                         line=dict(color='firebrick', width=4,dash = 'dot')),row=1, col=1)
fig.add_trace(go.Scatter(x=x, y=fz, name='fz',
                         line=dict(color='firebrick', width=4,
                              dash='dash')
),row=1, col=1)
fig.add_trace(go.Scatter(x=x, y=resultant_force, name = 'resultant force',
                         line=dict(color='royalblue', width=4)),row=1, col=1)



fig.add_trace(go.Scatter(x=x, y=tx, name='Tx',
                         line=dict(color='firebrick', width=4,dash = 'dashdot')),row=2, col=1)
fig.add_trace(go.Scatter(x=x, y=ty, name ='Ty',
                         line=dict(color='firebrick', width=4,dash = 'dot')),row=2, col=1)
fig.add_trace(go.Scatter(x=x, y=tz, name='=Tz',
                         line=dict(color='firebrick', width=4,
                              dash='dash')
),row=2, col=1)
fig.add_trace(go.Scatter(x=x, y=resultant_torque, name = 'resultant Torque',
                         line=dict(color='royalblue', width=4)),row=2, col=1)



fig.show()

