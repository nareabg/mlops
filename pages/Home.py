import dash

from dash import Dash, dcc, html, Input, Output, State
from dash import callback,Input, Output, State, dcc, html

app = dash.Dash(__name__ )


image_filename = 'w.jpg'  
image_url = app.get_asset_url(image_filename)

nare = 'nare.jpg'  
nare = app.get_asset_url(nare)

luso = 'luso.jpg' 
luso = app.get_asset_url(luso)

armin = 'armin.jpg'  
armin = app.get_asset_url(armin)

 
dash.register_page(
    __name__,
    path='/'
)

layout =      html.Div([
    html.Div([
                html.P('UNLOCK THE POWER OF CUSTOMER LOYALTY', id = 'unlock_text'),

    ], className = 'black_box33'),

    html.Div([
        html.Div([
            html.H1('What is zenq?', id = 'zenq_text'),
        ], id = 'zenq'),
        html.Div([
            html.H4('In order to provide marketing analysts and data scientists with a helpful tool, the ZENQ package was developed. The primary purpose of the package is to analyze and give visualized feedback regarding CLV based on the data provided by the freight forwarding business. Moreover, computations of CLV and Recency, Frequency, and Monetary Value (RFM), in addition to forecasts, are the primary objective of the package. Because the package offers a number of different visualizations, it simplifies the process of comprehending the statistics and basing business decisions on those findings.', id = 'long_text'),
            ]),    
        html.Div([ ], id='purple'),    
        html.Div([ ], id = 'green'),   
    
        html.Div([
            html.Img(src=image_url, id = 'nkar')
        ]),
    ], id = 'box'),
    html.Div([
    html.Div([           
            html.Div([
                html.H2('OUR GIT_HUB', id = 'our_text'),],),
                    
            html.Div([
                html.H3('LINK', id = 'link'),  ], id = 'link_git')
    ], id = 'green_box') ,
    
    html.Div([
         html.H1('OUR TEAM', id = 'our_team'), 
    ],id = 'team_box'),
        
    html.Div([
        html.Div([
            
            html.Img(src=nare, id = 'nkar_nare'),
            html.H3('Nare Abgaryan', id = 'nare_name')
        ]),
        html.Div([
            html.Img(src=luso, id = 'nkar_luso'),
            html.H3('Lusine Babayan', id = 'luso_name')
        ]),
       html.Div([
            html.Img(src=armin, id = 'nkar_armin'),
            html.H3('Armine Khachatryan', id = 'armin_name')
        ]),  
        ], id = 'black_box_1')
    ], id = 'container'),
])
#   ], id='page_layout2')
    
    