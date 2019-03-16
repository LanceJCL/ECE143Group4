from dataprocess import *
import matplotlib.pyplot as plt
import plotly 
import plotly.plotly as py
import plotly.graph_objs as go
import cufflinks as cf


df_certified, totaldf, Companyd, jobs, sorted_Company_count, sorted_Site_count = load_data_company('totalnew.csv')
new_input_new, new_list_name = data_for_bar(totaldf)
Salary, Salary_dict = Salary_Statistic(df_certified)
accecpted,denied,jobs_name_list,top_com_list = data_best_company_for_top10jobs(jobs,totaldf,df_certified)



################Jobs distribution plot for top 5 company#######################
#plotly.tools.set_credentials_file(username='Lanceljc', api_key='9om7ohKNz7yvpYZ7ehlJ')
#cf.set_config_file(offline=False, world_readable=True, theme='ggplot')
#df = pd.DataFrame(new_input_new, columns=new_list_name)
#df.iplot(kind='barh',barmode='stack', bargap=.1)

#################plot for distribution of Salary###############################
import matplotlib.mlab as mlab
x = list(Salary)
num_bins = 40
plt.figure(figsize=(20,10))
# the histogram of the data
n, bins, patches = plt.hist(x, num_bins, facecolor='orange', alpha=0.5)
 
# add a 'best fit' line
plt.xlabel('Annual Salary',fontsize=20)
plt.ylabel('Counts',fontsize=20)
plt.title(r'Distribution of Salary',fontsize=32)
plt.axvline(sum(x)/len(x), color='k', linestyle='dashed', linewidth=1)
plt.xlim((0, 430000))
plt.text(sum(x)/len(x) + sum(x)/len(x)/10, 
         sum(x)/len(x) - sum(x)/len(x)/10, 
         'Mean: {:.2f}'.format(sum(x)/len(x)))
# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()

####################Plot of best company for top 10 jobs#######################
import plotly.graph_objs as go

N = len(accecpted)
x = jobs_name_list[:N]#np.linspace(1, N, N)
y = np.array(accecpted)
x2 = top_com_list
y2 = np.array(denied)
for i in range(N):
    x[i]=x[i]+'/// '+top_com_list[i]
df = pd.DataFrame({'x': x, 'y': y, 'y2':y2})
df.head()

data = [
    go.Bar(
        x=df['x'], # assign x as the dataframe column 'x'
        y=df['y']
    ),
    go.Bar(
        x=df['x'],
        y=df['y2']
    )
]

layout = go.Layout(
    barmode='stack',
    title='Stacked Bar with Pandas'
)

fig = go.Figure(data=data, layout=layout)

# IPython notebook
py.iplot(fig, filename='pandas-bar-chart-layout')

