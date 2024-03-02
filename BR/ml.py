import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler



import pandas as pd
import numpy as np

df=pd.read_csv("static/nsc_20240302091609.csv")
# Provided data
data = {
    'subject': ['CY11001-CHEMISTRY', 'CY19001-CHEMISTRY LAB.', 'EA10001-EXTRA ACADEMIC ACTIVITY-I', 'EA10005-INDUCTION PROGRAM',
                'EE11001-ELECTRICAL TECHNOLOGY', 'EE19001-ELECTRICAL TECHNOLOGY LAB.', 'HS13001-ENGLISH FOR COMMUNICATION',
                'MA10001-MATHEMATICS-I', 'ME19001-INTRODUCTION TO MANUFACTURING PROCESSES', 'CE13001-ENGINEERING DRAWING AND COMPUTER GRAPHICS',
                'CS10001-PROGRAMMING AND DATA STRUCTURES', 'CS19101-PROGRAMMING AND DATA STRUCTURES TUTORIAL AND LABORATORY',
                'EA10002-EXTRA ACADEMIC ACTIVITY-II', 'MA10002-MATHEMATICS-II', 'ME10001-MECHANICS', 'PH11001-PHYSICS',
                'PH19001-PHYSICS LAB.', 'AE21001-INTRODUCTION TO AERODYNAMICS', 'AE21003-DYNAMICS FOR AEROSPACE ENGINEERS',
                'BS20001-SCIENCE OF LIVING SYSTEM', 'EA10003-EXTRA ACADEMIC ACTIVITY-III', 'EC21101-BASIC ELECTRONICS',
                'EC29001-BASIC ELECTRONICS LAB.', 'EV20001-ENVIRONMENTAL SCIENCE', 'MA20101-TRANSFORM CALCULUS', 'CE13002-EXAMPLE SUBJECT'],  # Extended with one more subject
    'subject_grades': ['A', 'EX', 'Y', 'Y', 'C', 'B', 'A', 'B', 'A', 'EX', 'A', 'A', 'Y', 'A', 'EX', 'B', 'EX', 'A', 'A', 'EX', 'EX', 'A', 'A', 'EX', 'B'],
    'subject_session': ['Autumn17', 'Autumn17', 'Autumn17', 'Autumn17', 'Autumn17', 'Autumn17', 'Autumn17', 'Autumn17', 'Autumn17', 'Autumn17',
                        'Spring18', 'Spring18', 'Spring18', 'Spring18', 'Spring18', 'Spring18', 'Autumn18', 'Autumn18', 'Autumn18', 'Autumn18',
                        'Autumn18', 'Autumn18', 'Autumn18', 'Autumn18', 'Autumn18', 'Autumn18', 'Autumn18', 'Autumn18', 'Autumn18']
}

# Ensure all columns are of the same length
max_length = max(len(value) for value in data.values())
data = {key: value + [''] * (max_length - len(value)) for key, value in data.items()}

# Create DataFrame
df2 = pd.DataFrame(data)

# Extract course code
df2['course_code'] = df2['subject'].str.extract(r'^([A-Z]+\d+)-')
df2['subject'] = df2['subject'].str.replace(r'^[A-Z]+\d+-', '')

# Replace grades
grade_mapping = {'EX': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'P': 5, 'F': 0}
df2['subject_grades'] = df2['subject_grades'].replace(grade_mapping)

# Remove non-numeric characters
df2['subject_grades'] = df2['subject_grades'].replace('[^0-9]', '', regex=True)

# Convert the column to numeric
df2['subject_grades'] = pd.to_numeric(df2['subject_grades'], errors='coerce')

# Display the DataFrame after processing
print("\nDataFrame after removing non-numeric characters:")
import pandas as pd

# Assuming you have two dataframes: df and df2
# Drop duplicates based on 'course_code' keeping the first occurrence
df_first_occurrence = df.drop_duplicates(subset='course_code', keep='first')

# Merging based on the 'course_code' column
merged_df = pd.merge(df_first_occurrence, df2, on='course_code')

# Selecting specific columns from the merged dataframe
selected_columns = ["category",'EX_percent', 'A_percent', 'B_percent', 'C_percent', 'Mean Grade',"subject_grades"]

# Create a new dataframe with only the selected columns
final_df = merged_df[selected_columns]

# Display the final dataframe
print("Final DataFrame:")




# Assuming final_df is your DataFrame
# Extract features and target variable
X = final_df[['EX_percent', 'A_percent', 'B_percent', 'C_percent', 'Mean Grade']]
y = final_df['subject_grades']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build a simple neural network model
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dropout(0.5))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='linear'))  # Assuming regression task

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=2)

# Evaluate the model on the test set
loss = model.evaluate(X_test_scaled, y_test)
print(f'Mean Squared Error on Test Set: {loss}')

# Make predictions
predictions = model.predict(X_test_scaled)

# Print some predicted values and actual values for comparison
for pred, actual in zip(predictions[:10], y_test[:10]):
    print(f'Predicted: {pred[0]}, Actual: {actual}')
