#%%
# Removes all columns that do not contain variation in the nucleotide, i.e., that are the same for all sequences.
mask = seq_df.nunique() == 1
to_drop = mask[mask==True].index
seq_df.drop(to_drop, axis=1, inplace=True)


# This is how i first did it, iterating over all columns.
# This is a very inneffient way of working with pd dataframes.
# The best way is to use numpy's native ability of vector operations.
# That is, applying some function all at once to the dataframe.
# How you do it is using native commands on the whole dataframe.
# In this case, to use the "drop" command, I needed to first create a list of
# the columns to be dropped.
# length = len(seq_df.columns)-1
#
# with progressbar.ProgressBar(max_value=length) as bar:
#     i=1
#     for col in seq_df.columns[1:]:
#         bar.update(i)
#         i += 1
#         if seq_df[col].nunique() == 1:
#             seq_df.drop(col, axis=1, inplace=True)
