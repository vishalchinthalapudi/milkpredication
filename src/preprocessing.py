def preprocess(data):
    # No null values (as seen in your dataset)
    # Convert Grade column to numeric
    mapping = {'low':0,'medium':1,'high':2}
    data['Grade'] = data['Grade'].map(mapping)
    return data
