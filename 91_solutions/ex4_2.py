# using `value_counts`
result = df['Position'].value_counts()
display(Markdown("Using `value_counts`:"))
display(result)

# using `groupby`
result = df.groupby(['Position'])['Position'].count()
display(Markdown("Using `groupby`:"))
display(result)

# using `pivot_table`
# NOTE: This is not the correct way to get the result
# We practice this to see the difference between value_counts/groupby/pivot_table ONLY
result = df.pivot_table(index='Position', aggfunc='count').iloc[:, 0]
display(Markdown("Using `pivot_table`:"))
display(result)