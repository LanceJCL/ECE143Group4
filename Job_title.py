
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#getting data and fetching most needed info
df = pd.read_csv("totalnew.csv", encoding='latin-1', low_memory=False, usecols=['CASE_SUBMITTED','DECISION_DATE', 'EMPLOYER_NAME', 'EMPLOYER_STATE', 'PREVAILING_WAGE', 'PW_UNIT_OF_PAY', 'CASE_STATUS', 'SOC_NAME', 'SOC_CODE'])
dfn = df.reset_index()
df = dfn.drop(['index'], axis=1)
df['year'] = pd.DatetimeIndex(df['CASE_SUBMITTED']).year
df = df[df.year.isin(range(2015,2019))]




#creates a pie of the top 5 least submitted job titles
def pie_chart_low5(df):
    '''
    type: dataframe 
    param: data to be analyzed
    creates a pie chart of the top 5 least submitted job titles
    '''
    isinstance(df, pd.DataFrame)
    
    thisset = set()

    #getting all job titles in a set
    for i in df['SOC_NAME']:
      thisset.add(i)
    
    
    #creating a mapping of the total number of applicants for each job title
    total_applications = {i:(df['SOC_NAME'].str.contains(i)).sum() for i in thisset}
    
    
    least_submitted_top5 = dict(sorted(total_applications.items(), key = lambda x: x[1])[:5])
    sizes = [least_submitted_top5[i] for i in least_submitted_top5.keys()]
    labels = ['{0} - {1} case(s) submitted'.format(i,j) for i, j in zip(least_submitted_top5.keys(), least_submitted_top5.values())]
    patches, texts = plt.pie(sizes, startangle = 90)
    patches, labels, dummy = zip(*sorted(zip(patches, labels, sizes), key = lambda x: x[2], reverse=True))
    plt.legend(patches, labels, loc = 'best', bbox_to_anchor = (-0.1, 1.), fontsize=15)
    plt.title("Top 5 least submitted job titles", bbox = {'facecolor': '0.8', 'pad':5}, fontsize = 15)

#creates a pie of the top 5 most submitted job titles

def pie_chart_top5(df):
    '''
    type: dataframe
    param: data to be analzed
    creates a pie chart of the top 5 most submitted job titles
    '''
    isinstance(df, pd.DataFrame)
    
    thisset = set()

    #getting all job titles in a set
    for i in df['SOC_NAME']:
      thisset.add(i)
    
    
    #creating a mapping of the total number of applicants for each job title
    total_applications = {i:(df['SOC_NAME']==i).sum() for i in thisset}
    
    most_submitted_top5 = dict(sorted(total_applications.items(), key = lambda x: -x[1])[:5])
    sizes = [most_submitted_top5[i] for i in most_submitted_top5.keys()]
    labels = ['{0} - {1} case(s) submitted'.format(i,j) for i, j in zip(most_submitted_top5.keys(), most_submitted_top5.values())]
    patches, texts = plt.pie(sizes, startangle = 90)
    patches, labels, dummy = zip(*sorted(zip(patches, labels, sizes), key = lambda x: x[2], reverse=True))
    plt.legend(patches, labels, loc = 'best', bbox_to_anchor = (-0.1, 1.), fontsize=15)
    plt.title("Top 5 most submitted job titles", bbox = {'facecolor': '0.8', 'pad':5}, fontsize = 15)


# creates stacked bar chart of top 5 job titles and their approval rates

 def stacked_bar_top5(df):
    '''
    type: dataframe
    param: data to be analyzed
    Creates a stacked_bar chart(showing denied and approved) for the top 5 job titles with highest approval rates
    '''
    isinstance(df, pd.DataFrame)
    
    
    #getting all job titles in a set
      for i in df['SOC_NAME']:
        thisset.add(i)
    
    
    
    #creating a mapping of the total number of applicants for each job title
    total_applications = {i:(df['SOC_NAME']==i).sum() for i in thisset}

    #creating a mapping of the total certified applicants for each job title
    approved_applicants = {i:((df['SOC_NAME']==i) & (df['CASE_STATUS']=='CERTIFIED')).sum() for i in thisset}
    
    #filtering out the job titles with submissions that are too low (<50)
    new_total = dict()
    for key, value in total_applications.items():
    if value>=50:
        new_total[key] = value
    
    new_percentage = {i: 100*approved_applicants[i]/total_applications[i] for i in new_total.keys()}
    new_approved = {i:approved_applicants[i] for i in new_total.keys()}
    N = 5
    ind = np.arange(N)
    width = 0.35
    top_5 = dict(sorted(new_percentage.items(), key = lambda x:-x[1])[:5])
    top_5_approved = tuple(new_approved[i] for i in top_5.keys())
    top_5_denied = tuple(new_total[i] - new_approved[i] for i in top_5.keys())
    p1 = plt.bar(ind, top_5_approved, width)
    p2 = plt.bar(ind, top_5_denied, width, bottom = top_5_approved)
    plt.ylabel('number of cases', fontsize = 15)
    plt.title('H1B cases of top 5 job titles', fontsize = 15)
    plt.xticks(ind, ('GRAPHIC DESIGNER', 'COMPUTER SYSTEMS ADMINISTRATOR', 'SALES ENGINEER', 'COMPUTER PROGRAMMER', 'COMPUTER SYSTEMS ANALYST'), rotation = 50)
    plt.legend((p1[0], p2[0]), ('Approved', 'Denied'))
    plt.show()



# creates stacked bar chart of top 5 job titles with lowest approval rates
def stacked_bar_worst5(df):
    '''
    type: dataframe
    param: data to be analyzed
    Creates a stacked_bar chart(showing denied and approved) for the top 5 job titles with lowest approval rates
    '''
    
    isinstance(df, pd.DataFrame)
    
    
    #getting all job titles in a set
      for i in df['SOC_NAME']:
        thisset.add(i)
    
    
    
    #creating a mapping of the total number of applicants for each job title
    total_applications = {i:(df['SOC_NAME']==i).sum() for i in thisset}

    #creating a mapping of the total certified applicants for each job title
    approved_applicants = {i:((df['SOC_NAME']==i) & (df['CASE_STATUS']=='CERTIFIED')).sum() for i in thisset}
    
    #filtering out the job titles with submissions that are too low (<50)
    new_total = dict()
    for key, value in total_applications.items():
    if value>=50:
        new_total[key] = value
    
    new_percentage = {i: 100*approved_applicants[i]/total_applications[i] for i in new_total.keys()}
    new_approved = {i:approved_applicants[i] for i in new_total.keys()}
    N = 5
    ind = np.arange(N)
    width = 0.35
    worst_5 = dict(sorted(new_percentage.items(), key = lambda x:x[1])[:5])
    worst_5_approved = tuple(new_approved[i] for i in worst_5.keys())
    worst_5_denied = tuple(new_total[i] - new_approved[i] for i in worst_5.keys())
    p1 = plt.bar(ind, worst_5_approved, width)
    p2 = plt.bar(ind, worst_5_denied, width, bottom = worst_5_approved)
    plt.ylabel('number of cases', fontsize = 15)
    plt.title('H1B cases of 5 lowest approved job titles', fontsize = 15)
    plt.xticks(ind, worst_5.keys(), rotation = 50)
    plt.legend((p1[0], p2[0]), ('Approved', 'Denied'))
    plt.show()



