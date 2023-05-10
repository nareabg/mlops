# import dash

# from dash import Dash, dcc, html, Input, Output, State
# from prometheus_flask_exporter import PrometheusMetrics
# import psutil
# from apscheduler.schedulers.background import BackgroundScheduler

# from prometheus_client import Gauge

# app = dash.Dash(__name__, use_pages=True,suppress_callback_exceptions=True)
# server=app.server
# prom_metrics = PrometheusMetrics(app)
# scheduler = BackgroundScheduler()

# cpu_usage_metric = Gauge('cpu_usage', 'CPU usage as a percentage')
# memory_usage_metric = Gauge('memory_usage', 'Memory usage as a percentage')

# # periodically update the metrics with the current CPU and memory usage
# def update_metrics():
#     cpu_usage = psutil.cpu_percent()
#     memory_usage = psutil.virtual_memory().percent
#     cpu_usage_metric.set(cpu_usage)
#     memory_usage_metric.set(memory_usage)

# # update metrics every 10 seconds
# scheduler.add_job(update_metrics, 'interval', seconds=10)


# image_filename = 'logo.jpeg'
# w = 'w.jpg'

# app.layout= html.Div([ 
                       
#     html.Div([
#         html.Div([    
#             html.Img(src=app.get_asset_url(image_filename), id = 'esim')
#         ], id='image'),
#          html.Div([   
#                  html.Div([
#             dcc.Link(html.Button(page['name'], className="navigation",  style={'font-size': '24px', 'font-family': 'Hanuman'}), href=page['path'])
#             for page in sorted(dash.page_registry.values(), key=lambda p: p['name'], reverse=True)
#         ]),
#         html.Hr(),

#         # content of each page
#         dash.page_container   
#                  ],className = 'rectangle1' )
            
#         ],),  
# ],)
# #dash
# #appscheduler
# #prometheus_flask_exporter, psutils, pandas

# # @app.route('/metrics')
# # def prometheus_metrics():
# #     return prometheus_client.generate_latest()
# @server.route('/metrics')
# def prometheus_metrics():
#     return prometheus_client.generate_latest()


# if __name__=='__main__':
# 	# app.run_server(debug=True, port=8058)
#     scheduler.start()
#     app.run_server(debug=True, host='0.0.0.0', port=8058)

import dash
from dash import dcc, html
from prometheus_flask_exporter import PrometheusMetrics
import psutil
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from prometheus_client import Gauge
server = Flask(__name__)
app = dash.Dash(__name__, server=server, use_pages=True,suppress_callback_exceptions=True)
server = app.server
prom_metrics = PrometheusMetrics(server)
scheduler = BackgroundScheduler()

cpu_usage_metric = Gauge('cpu_usage', 'CPU usage as a percentage')
memory_usage_metric = Gauge('memory_usage', 'Memory usage as a percentage')

# periodically update the metrics with the current CPU and memory usage
def update_metrics():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    cpu_usage_metric.set(cpu_usage)
    memory_usage_metric.set(memory_usage)

# update metrics every 10 seconds
scheduler.add_job(update_metrics, 'interval', seconds=10)

image_filename = 'logo.jpeg'

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url(image_filename), id='esim')
        ], id='image'),
        html.Div([
            html.Div([
                dcc.Link(html.Button(page['name'], className="navigation", style={'font-size': '24px', 'font-family': 'Hanuman'}), href=page['path'])
                for page in sorted(dash.page_registry.values(), key=lambda p: p['name'], reverse=True)
            ]),
            html.Hr(),
            # content of each page
            dash.page_container
        ], className='rectangle1')
    ]),
])

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=8058)