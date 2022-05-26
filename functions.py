import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV, cross_val_score,cross_val_predict, cross_validate

# Color swatches
bToG = ['#0300c3', '#042492', '#053b83', '#055274', '#05616a',
          '#067a59', '#068c4d', '#07ad37', '#08c626', '#09ff00']
yToR = ['#fcb045', '#fc8439', '#fc5e2f', '#fc4227', '#fd1d1d']

#This will be useful for EDA.
def colInfo(col):
    """
    Helper function to print out information regarding a pandas Series (DataFrame column)
    
    col = pd.Series
    
    float: bar plot
    int: histogram plot
    object: bar plot of top 10 occurcences. If number of itmes > 15, plot additional bottom 5 occurences
    """
    len_Col = col.shape[0]
    num_zeroes = (col == 0).sum()
    num_missing = col.isna().sum()
    mean = 0
    median = 0
    uniques = len(col.unique())
    try:
        num_unknowns = (col.map(lambda x: x.lower() in ['unknown', ' ', '']).sum())
    except:
        num_unknowns = 0

    try:
        mean = col.mean()
        median = col.median()
    except:
        mean = 0
        median = 0

    data = [
        ['Zeroes',  f'{num_zeroes:,}',  f'{(num_zeroes/len_Col *100):.2f} %'],
        ['Missing', f'{num_missing:,}',  f'{(num_missing/len_Col *100):.2f} %'],
        ['Unknown', f'{num_unknowns:,}',
            f'{(num_unknowns/len_Col *100):.2f} %'],
        ['Uniques', f'{uniques:,}', f'{(uniques/len_Col *100):.2f} %'],
        ['Mean', f'{mean:.2f}', '-'],
        ['Median', f'{median:.2f}', '-'],
    ]
    
    info_table = pd.DataFrame(data, columns=['', 'Number', 'Percentage']).set_index('').style.set_caption("Table Info")
    
    #Creating Value Count Table
    vCountNum = col.value_counts()
    vCountPct = col.value_counts(normalize=True)*100
    vCountNum.name = 'Value Count'
    vCountPct.name = '% Value Count'
    
    #Limiting Table to top 10
    value_count_table = pd.concat([vCountNum,vCountPct], axis=1)
    value_count_table = value_count_table.iloc[:10].style.set_caption("Top 10 Value Count Info")
    
    # Display Tables as Panda DataFrames
    display(info_table,value_count_table)

    # Display plots depending upon datatype
    if col.dtype == 'float64':
        fig, ax = plt.subplots(figsize=(15, 8))
        plt.plot(col)
        plt.axhline(y=mean, color='r', linestyle='-.', label='Mean')
        plt.axhline(y=median, color='b', linestyle='-.', label='Median')
        plt.title('Bar plot: '+col.name)
        plt.legend()
        plt.ylabel(col.name)

    elif col.dtype == 'int64':
        fig, ax = plt.subplots(figsize=(15, 8))
        plt.hist(col)
        plt.title('Histogram plot: '+col.name)
        plt.ylabel(col.name)
        
        if len(col.value_counts()) < 30:
            fig, ax = plt.subplots(figsize=(15, 8))
            col.value_counts().iloc[:10].plot(kind='bar', color = bToG)
            plt.title('Frequency of top 10: '+col.name)
            plt.ylabel(col.name)
    
    elif col.dtype == 'O':
        fig, ax = plt.subplots(figsize=(15, 8))
        col.value_counts().iloc[:10].plot(kind='bar', color = bToG)
        plt.title('Frequency of top 10: '+col.name)
        plt.ylabel(col.name)
        
        if len(col.value_counts()) > 15:
            fig, ax = plt.subplots(figsize=(15, 8))
            col.value_counts().iloc[-5:].plot(kind='bar', color = yToR)
            plt.title('Frequency of bottom 5: '+col.name)
            plt.ylabel(col.name)
            
 #This will be useful for the models when getting my scores for my models.           
def modelReport(model, X, y):
    '''
    Prints out cross validation test scoring metrics as a Pandas dataframe
    Displays a confusion matrix of the cross validation
    
    model = estimator to use for report generation
    X = input 
    y = output/label
    cv = Generates a cross validation report
    
    '''
    display(getAllCrossValScores(model, X, y))
     # Getting cross val scores
    #getAllCrossValScores(model, X, y)
    
    # Using cross_val_predict or model.predict to create a confusion matrix
    preds = cross_val_predict(estimator=model, X=X, y=y)  
        
    cm = confusion_matrix(y, preds, labels=model.classes_)
    disp = ConfusionMatrixDisplay(cm, display_labels=model.classes_)
    fig, ax = plt.subplots(figsize=(8, 8))
    disp.plot(cmap='OrRd', ax=ax)

#Shows me my scores!
def getAllCrossValScores(model, X, y):
    '''
    Prints out cross validation test scoring metrics as a Pandas dataframe
    
    f1 =  F1-score (micro & macro)
    '''
    # Using cross_validate to generate accuracy, recall, precision and f1-scores
    cv = cross_validate(model, X, y, scoring=[
                        'f1_macro', 'f1_micro'])
    
    f1_macro = cv['test_f1_macro'].mean()
    f1_micro = cv['test_f1_micro'].mean()

    data = [
        ['F1 Macro', f'{f1_macro:.4f}'],
        ['F1 Micro', f'{f1_micro:.4f}'],
    ]

    info_table = pd.DataFrame(data, columns=['', 'Scores']).set_index(
        '').style.set_caption("Cross Validation Results")
    return(info_table)

#This will be useful for gridsearch after my modeling.

def prettyPrintGridCVResults(GSCVModel):
    '''
    Tabulates results a grid search.
    Ranks by F1 Micro-Score
    Shows 2 mean test metrics:  F1-score Macro, F1-score Micro
    Shows all parameters used for that model
    '''
    
    list_cols = ['mean_test_f1_micro']
    list_metrics = [ 'mean_test_f1_macro', 'mean_test_f1_micro']
    list_cols.extend(list_metrics)

    for col in GSCVModel.cv_results_.keys():
        if col.startswith('param_'):
            list_cols.append(col)
    
    table = pd.DataFrame(GSCVModel.cv_results_)
    for m in list_metrics:
        table[m] = table[m].map('{:,.4f}'.format)
    table = table[list_cols].sort_values(by='mean_test_f1_micro', ascending = False )
    

        
    table.rename(columns={'mean_test_f1_micro': 'Mean Test F1-Score (micro)',
                          'mean_test_precision_macro': 'Mean Test Precision (micro)'
             
                          }, inplace=True)
    

    return table.set_index('Mean Test F1-Score (micro)')