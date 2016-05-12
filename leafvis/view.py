""" Defines a leafvis view for IPython """

import requests
import pickle
import store

from IPython.display import HTML
HOST = 'predictable.bom.gov.au'

def leaflet(layer, cmap='elevation', vmin=0, vmax=1200, host=HOST):
    """ Returns a HTML leaflet view """

    _ = store.create_layer(layer)

    # Tell the WMS server to refresh its grid cache.
    r = requests.get('http://{}:5000/grids/refresh'.format(host), params={})
    if r.content is None:
        raise ValueError('Cannot update grids')

    url = ('<iframe '
            ' src=http://{}:5000/map/{}/{}/{}/{}'
           ' width=500'
           ' height=500'
           '</iframe>'
          ).format(host, layer.name, cmap, vmin, vmax)

    return HTML(url)
