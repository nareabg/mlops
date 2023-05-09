import dash

from dash import Dash, dcc, html, Input, Output, State
from prometheus_flask_exporter import PrometheusMetrics
import psutil
from prometheus_client import Gauge

app = dash.Dash(__name__, use_pages=True,suppress_callback_exceptions=True)
server=app.server
prom_metrics = PrometheusMetrics(app)
cpu_usage_metric = Gauge('cpu_usage', 'CPU usage as a percentage')
# periodically update the metric with the current CPU usage
def update_cpu_usage_metric():
    cpu_usage = psutil.cpu_percent()
    cpu_usage_metric.set(cpu_usage)

image_filename = 'logo.jpeg'
w = 'w.jpg'

app.layout= html.Div([ 
                       
    html.Div([
        html.Div([    
            html.Img(src=app.get_asset_url(image_filename), id = 'esim')
        ], id='image'),
         html.Div([   
                 html.Div([
            dcc.Link(html.Button(page['name'], className="navigation",  style={'font-size': '24px', 'font-family': 'Hanuman'}), href=page['path'])
            for page in sorted(dash.page_registry.values(), key=lambda p: p['name'], reverse=True)
        ]),
        html.Hr(),

        # content of each page
        dash.page_container   
                 ],className = 'rectangle1' )
            
        ],),  
],)


@app.route('/metrics')
def prometheus_metrics():
    return prom_metrics.export_metrics()


if __name__=='__main__':
	app.run_server(debug=True, port=8058)
 