
# IMPORTANT # 
# ["Position"] was chosen to make the `count`
# TIP: try this: 
# df.groupby(['Manager Name', 'Department'])["Position"].count() to get a `pd.Series` as a result 
df.groupby(['Manager Name', 'Department'])[["Position"]].count()