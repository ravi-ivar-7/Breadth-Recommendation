import pandas as pd
import numpy as np

df=pd.read_csv("static/nsc_20240302091609.csv")
# df.head()

def sort_and_get_mean(df, selected_courses, cgpa):
    if cgpa > 9:
        df_filtered = df[df['course'].isin(selected_courses)].sort_values(by='cum_EX_A_%')
    elif 8 < cgpa <= 9:
        df_filtered = df[df['course'].isin(selected_courses)].sort_values(by='cum_EX_A_%')
    elif 7.5 < cgpa <= 8:
        df_filtered = df[df['course'].isin(selected_courses)].sort_values(by='cum_EX_A_B_%')
    elif 6 < cgpa <= 7.5:
        df_filtered = df[df['course'].isin(selected_courses)].sort_values(by='cum_EX,A,B,C_%')

    sorted_courses = df_filtered[['course', 'Mean Grade']]
    return sorted_courses



# Let the user choose a session

sessions = df['session'].unique()

print("Choose a session:")
for index, session in enumerate(sessions, start=1):
    print(f"{index}. {session}")

selected_session_index = int(input("Enter the index of the session: ")) - 1 # input
selected_session = sessions[selected_session_index]

# Filter DataFrame based on the initially chosen session
df_session_filtered = df[df['session'] == selected_session]

# Get unique categories for the selected session
categories = df_session_filtered['category'].unique()

# Let the user choose a category
print("\nChoose a category:")
for index, category in enumerate(categories, start=1):
    print(f"{index}. {category}")

selected_index = int(input("Enter the index of the category: ")) - 1
selected_category = categories[selected_index]

# Display Personal Interest options for the selected category and session
print("\nChoose Personal Interests (or select 'None' to see all courses for the chosen category):")
personal_interest_options = ['None'] + df_session_filtered[df_session_filtered['category'] == selected_category]['Personal Interest'].unique().tolist()

for index, option in enumerate(personal_interest_options, start=1):
    print(f"{index}. {option}")

selected_option_indices = input("Enter the indices of the Personal Interest options separated by commas (e.g., 1,3,5): ")
selected_option_indices = [int(index) - 1 for index in selected_option_indices.split(',')]

selected_personal_interest = [personal_interest_options[index] for index in selected_option_indices]

# Display courses for the selected Personal Interest, category, and session
if 'None' in selected_personal_interest:
    selected_courses = df_session_filtered[df_session_filtered['category'] == selected_category]['course']
else:
    selected_courses = df_session_filtered[
        (df_session_filtered['category'] == selected_category) &
        (df_session_filtered['Personal Interest'].isin(selected_personal_interest))
    ]['course']
    
# Ask the user for their CGPA
cgpa = float(input("Enter your CGPA: "))

# Sort and display courses based on CGPA
sorted_selected_courses = sort_and_get_mean(df_session_filtered, selected_courses, cgpa)
print("\nCourses for the selected Personal Interest:")
print(sorted_selected_courses)
