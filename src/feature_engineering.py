from sklearn.preprocessing import LabelEncoder

def encode_labels(df, column):
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column])
    return df