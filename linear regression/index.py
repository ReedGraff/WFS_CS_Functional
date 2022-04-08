def Multiple_Linear_Regression():
    # Reference => https://www.analyticsvidhya.com/blog/2021/05/multiple-linear-regression-using-python-and-scikit-learn/
    from sklearn.linear_model import LinearRegression
    
    x_train, y_train, x_test, y_test = Spam_Detection.import_data()

    # creating an object of LinearRegression class
    LR = LinearRegression()

    # fitting the training data
    LR.fit(x_train,y_train)
    
    # Prediction Classes
    predictions = LR.predict(x_test)
    prediction_classes = [
        1 if prob > 0.5 else 0 for prob in np.ravel(predictions)
    ]
    
    # Pandas Dataframe
    df = pd.DataFrame({'Actual': y_test, 'Predicted': prediction_classes})
    result = df["Actual"].eq(df["Predicted"]).sum() / len(df) * 100
    print(result)
    print(df)