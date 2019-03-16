import pandas as pd
import numpy as np
from collections import Counter
import operator

def load_data_company(file_name):
    '''
    load main csv file output df
    the file must be totalnew.csv
    the output will be the sorted dictionary of count for company and jobs statistic 
    '''
    assert file_name == 'totalnew.csv'
    totaldf = pd.read_csv(file_name,low_memory=False)
    totaldfn = totaldf.reset_index()
    totaldf = totaldfn.drop(['index'], axis=1)
    df_certified = totaldf[totaldf.CASE_STATUS.isin(['CERTIFIED'])]
    df_certified = df_certified[df_certified.VISA_CLASS.isin(['H-1B'])]
    Sited = df_certified['WORKSITE_STATE']
    Companyd = df_certified['EMPLOYER_NAME']
    jobs = df_certified['SOC_CODE']
    Site = list(Sited)
    Company = list(Companyd)
    Site_count = dict(Counter(Site))
    Company_count = dict(Counter(Company))
    sorted_Site_count = sorted(Site_count.items(), key=operator.itemgetter(1),reverse=True)
    sorted_Company_count = sorted(Company_count.items(), key=operator.itemgetter(1),reverse=True)
    
    return df_certified, totaldf, Companyd, jobs, sorted_Company_count, sorted_Site_count

def Salary_Statistic(df_certified):
    '''
    Input is the filtered mian dataframe which include certified only.
    Output will be Salary dataframe
    '''
    assert isinstance(df_certified,pd.DataFrame)
    Salary = df_certified['PREVAILING_WAGE']
    Salary = Salary[df_certified['PW_UNIT_OF_PAY']=='Year']
    Salary = Salary.iloc[:].str.replace(',', '').astype(float)
    Salary_dict = dict(Counter(Salary))
    return Salary, Salary_dict
    

def JobInformationextraction(totaldf):
    '''
    This function input is a processed main dataframe for this project
    and ask for user to input and information related to job title. 
    Ask if user want to know the approval rate for that input job title
    If Y then print approval rate for that input job title 
    Ask if user want to know the best company in approved number for input job title
    If Y then print best company in approved number for input job title
    This function will output the df with respected to the input job title and have only 
    input category.
    '''
    Job = input('Enter you job title ')
    Category = input('What Category you want to look up?')
    Approval_rate = input('Do you want to check approval rate?(Y/N)')
    BEST_COMPANY = input('Do you want to see the most approved Company?(Y/N)')
    assert isinstance(totaldf,pd.DataFrame)
    assert Job in list(totaldf['SOC_NAME'])
    assert Category in list(list(totaldf.columns.values)[1:])
    assert BEST_COMPANY in list(['Y','N'])
    assert Approval_rate in list(['Y','N'])
    print('\n------------------output------------------------\n')
    Job_title = totaldfn[totaldfn['SOC_NAME']==Job]
    if Approval_rate == 'Y':
        rate = 1.0*sum(Job_title['CASE_STATUS']=='CERTIFIED')/(1.0*len(Job_title))
        print('The approval rate for '+ Job + ' is ', rate*100,'%')
    if BEST_COMPANY == 'Y':
        Count = Counter(list(Job_title[Job_title['CASE_STATUS']=='CERTIFIED']['EMPLOYER_NAME']))
        sorted_count = sorted(Count.items(), key=operator.itemgetter(1),reverse=True)
        print('The most approved Company is '+sorted_count[0][0])
    print(Job_title[[Category]])
    return Job_title[Category]
                     
def data_for_bar(totaldf):
    '''
    This function take main dataframe as input 
    Output the a 2d array of value for bar chart and 1d array for labels of the charts
    '''
    assert isinstance(totaldf,pd.DataFrame)
    df_certified = totaldf[totaldf.CASE_STATUS.isin(['CERTIFIED'])]
    df_certified = df_certified[df_certified.VISA_CLASS.isin(['H-1B'])]
    Sited = df_certified['WORKSITE_STATE']
    Companyd = df_certified['EMPLOYER_NAME']
    jobs = df_certified['SOC_CODE']
    Site = list(Sited)
    Company = list(Companyd)
    
    Site_count = dict(Counter(Site))
    Company_count = dict(Counter(Company))
    sorted_Site_count = sorted(Site_count.items(), key=operator.itemgetter(1),reverse=True)
    sorted_Company_count = sorted(Company_count.items(), key=operator.itemgetter(1),reverse=True)
    
    Counterlist = []
    for i in range(5):
        company_name = sorted_Company_count[i][0]
        temjobs = jobs[Companyd==company_name]
        Counterlist.append(Counter(temjobs))
    list_jobs = []
    for i in range(5):
        temdict = dict(Counterlist[i])
        keys = list(temdict.keys())
        [list_jobs.append(ele) for ele in keys]
    list_jobs = list(set(list_jobs))
    list_jobs
    input_array = np.zeros((5,len(list_jobs)))
    for i in range(5):
        temdict = dict(Counterlist[i])
        for j in range(len(list_jobs)):
            if list_jobs[j] not in list(temdict.keys()):
                input_array[i,j]=int(0)
            else:
                input_array[i,j]=int(temdict[list_jobs[j]])
    new_list = list_jobs.copy()
    for i in range(input_array.shape[1]):
        if sum(input_array[:,i])<10000:
            new_list[i] = 'nan'
    new_list = list(set(new_list))
    new_input = np.zeros((5,len(new_list)-1))
    tem_new = []
    for ele in new_list:
        if ele != 'nan':
            tem_new.append(ele)
    new_list = tem_new
    new_input=np.zeros((5,len(new_list)))
    for i in range(5):
        temdict = dict(Counterlist[i])
        for j in range(len(new_list)):
            if new_list[j] not in list(temdict.keys()):
                new_input[i,j]=int(0)
            else:
                new_input[i,j]=int(temdict[new_list[j]])
    new_list_name = []
    jobs_name = df_certified['SOC_NAME']
    for name in new_list:  
        tem = list(jobs_name[jobs==name])[0]
        new_list_name.append(tem)
    new_list_name.append('other')
    otherss = [] 
    for i in range(5):
        temvalue = sum(input_array[i]) -sum(new_input[i])
        otherss.append(temvalue)
    new_input_new = np.concatenate((new_input,np.array(otherss).reshape(-1,1)),axis = 1)
    return new_input_new, new_list_name
def data_best_company_for_top10jobs(jobs,totaldf,df_certified):
    '''
    This function take main dataframe as input and job and jobs_name dataframe extract from before  
    Output are accpected and denied number counts for best company for top 10 jobs
    and the corresponding xlabel 
    '''
    assert isinstance(jobs,pd.core.series.Series)
    assert isinstance(totaldf,pd.DataFrame)
    assert isinstance(df_certified,pd.DataFrame)
    jobs_name = df_certified['SOC_NAME']
    jobs_count = dict(Counter(jobs))
    sorted_jobs_count = sorted(jobs_count.items(), key=operator.itemgetter(1),reverse=True)
    jobs_id = list(dict(sorted_jobs_count).keys())
    jobs_name_list = []
    i=0
    for name in jobs_id:  
        i+=1
        if i>40:break
        if i%50 ==0 :print(i)
        tem = list(jobs_name[jobs==name])[0]
        jobs_name_list.append(tem)
    Company = totaldf[totaldf.VISA_CLASS.isin(['H-1B'])]['EMPLOYER_NAME']
    jobs_c = totaldf[totaldf.VISA_CLASS.isin(['H-1B'])]['SOC_NAME']
    Status = totaldf[totaldf.VISA_CLASS.isin(['H-1B'])]['CASE_STATUS']
    precent =[]
    precent_job = []
    number =[]
    top_com_list = []
    accecpted = []
    denied = []
    one = []
    other =[] 
    for i in range(10):
        jobname = jobs_name_list[i]
        cor_company = Company[jobs_c==jobname]
        tem_count = dict(Counter(list(cor_company)))
        sorted_tem_count = sorted(tem_count.items(), key=operator.itemgetter(1),reverse=True)
        top_com = sorted_tem_count[0][0]
        top_com_list.append(top_com)
        top_com_state = Status[Company == top_com]
        number_c = sum(top_com_state=='CERTIFIED')
        rate_c = number_c/(sum(top_com_state=='DENIED')+number_c)
        accecpted.append(number_c)
        denied.append(sum(top_com_state=='DENIED'))
        top_com_job_state = jobs_c[Company == top_com]
        rate_j = sum(top_com_job_state==jobname)/len(top_com_job_state)
        one.append(sum(top_com_job_state==jobname))
        other.append(sum(top_com_job_state!=jobname))
        number.append(number_c) 
        precent.append(rate_c)
        precent_job.append(rate_j)
    return accecpted,denied,jobs_name_list,top_com_list