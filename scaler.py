X_scaler = MinMaxScaler()
def normalize_spec(X,scaler):
    '''
    Input spectrogram should be in the shape of (n_samples, n_freqency_bin, n_time_steps)
    or in the shape of (n_samples, 1, n_freqency_bin, n_time_steps)
    '''
    X_norm = []
    if len(X[0].shape) == 3:
        print("Images with channels")
        for spec in X:
            H = spec.shape[1]; W=spec.shape[2]
            norm = scaler.fit_transform(spec.reshape(H*W,1))
            X_norm.append(norm.reshape(H,W))

        X_norm = np.array(X_norm)    

    elif len(X[0].shape) == 2:
        print("Images with H and W")
        for spec in X:
            H = spec.shape[0]; W=spec.shape[1]
            norm = scaler.fit_transform(spec.reshape(H*W,1))
            X_norm.append(norm.reshape(H,W))

        X_norm = np.array(X_norm)

    else:
        print("shape error, please check your input")
    return X_norm
