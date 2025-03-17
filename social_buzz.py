import pandas as pd

# Load CSV files
df_reactions = pd.read_csv("Reactions.csv")
df_content = pd.read_csv("ContentFiltered.csv")
df_reaction_types = pd.read_csv("ReactionTypesFiltered.csv")


print("Columns in df_reaction_types:", df_reaction_types.columns)
print("Columns in df_reaction_types:", df_reactions.columns)

df_merged = df_reactions.merge(df_content[['Content ID', 'Category']], on='Content ID', how='left')
df_merged = df_merged.merge(df_reaction_types[['Reaction Type', 'Score']], on='Reaction Type', how='left')

print(df_merged.head())

# Group by category and sum scores
df_top5 = df_merged.groupby('Category')['Score'].sum().reset_index()

# Sort in descending order and pick the top 5
df_top5 = df_top5.sort_values(by='Score', ascending=False).head(5)

# Display the top 5 categories
print(df_top5)


# Save the full merged dataset
df_merged.to_csv("Final_Cleaned_Data.csv", index=False)

# Save the top 5 categories
df_top5.to_csv("Top_5_Categories.csv", index=False)

