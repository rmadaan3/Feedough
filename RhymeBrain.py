from random import choice
import requests
rhymebrain_url = 'http://rhymebrain.com/talk'

def get_portmanteaus(word):
    params = { 'function': 'getPortmanteaus', 'word': word }
    rhymebrain_response = requests.get(rhymebrain_url, params).json()

    source = []
    combined = []
    i=0
    for portmanteau in rhymebrain_response:
        source.append(portmanteau['source'])
        combined.append(portmanteau['combined'])
        print(source[i]," --- ",combined[i])
        i=i+1