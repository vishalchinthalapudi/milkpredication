def preprocess(data):
    mapping = {'low':0, 'medium':1, 'high':2}
    data['Grade'] = data['Grade'].map(mapping)
    return data
