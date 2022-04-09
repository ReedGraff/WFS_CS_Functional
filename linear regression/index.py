import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import matplotlib
#from wordcloud import WordCloud

# Univariate analysis of continuous variables
class Spam_Detection:
    def Side_By_Side():
        # Compile csv data into dataframe
        df = pd.read_csv("../datasets/instagram_spam/whole.csv")

        for column in list(df):
            print("Testing: " + column)
            
            # Set initialization info
            fig = plt.figure(figsize=(20,8),facecolor='white')
            gs = fig.add_gridspec(1,2)
            ax = [None for i in range(2)]
            ax[0] = fig.add_subplot(gs[0,0])
            ax[1] = fig.add_subplot(gs[0,1])
            
            # Set Headings
            ax[0].set_title('Distribution of the ' + column + '\n(Kernel Density Estimate)',fontsize=15,fontweight='bold', fontfamily='monospace')

            # Set Headings
            ax[1].set_title('Distribution of the ' + column + '\n(Histogram Plot)',fontsize=15,fontweight='bold', fontfamily='monospace')

            # Kernel Density Estimate
            sns.kdeplot(x=df[column],ax=ax[0],shade=True, color='gold', alpha=1,zorder=3,linewidth=5,edgecolor='black')
            # The y-axis in a density plot is the probability density function for the kernel density estimation.
            
            # Histogram Plot
            sns.histplot(x=df[column],ax=ax[1], color='olive', alpha=1,zorder=2,linewidth=1,edgecolor='black')

            for i in range(2):
                ax[i].set_ylabel('')
                ax[i].grid(which='both', axis='y', zorder=0, color='black', linestyle=':', dashes=(2,7))
                
                for direction in ['top','right','left']:
                    ax[i].spines[direction].set_visible(False)
                    
                    
            # Rename and save:
            column = column.translate({ord(i): None for i in '!@#$%^&*(){}[],./ ;:\'\"#'})
            plt.savefig("Visualizations/Visualization_of_" + column + ".png")









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

























    def import_data():
        orig_train = pd.read_csv('../datasets/instagram_spam/train.csv')
        orig_test = pd.read_csv('../datasets/instagram_spam/test.csv')

        # Training
        x_train = orig_train
        x_train = x_train.drop("fake",axis=1)
        x_train = x_train.values
        y_train = orig_train["fake"].values
        
        # Testing
        x_test = orig_test
        x_test = x_test.drop("fake",axis=1)
        x_test = x_test.values
        y_test = orig_test["fake"].values

        return x_train, y_train, x_test, y_test


Spam_Detection.Multiple_Linear_Regression()
