import numpy as np
num_students = 4
num_subjects = 4
subjects = ['Math', 'Science', 'English', 'History']
student_scores = np.array([[int(input(f"Enter {subjects[j]} score for student {i+1}: ")) for j in range(num_subjects)] for i in range(num_students)])
print("Student Scores Matrix:")
print(student_scores)
average_scores = np.mean(student_scores, axis=0)
highest_average_subject_index = np.argmax(average_scores)
highest_average_subject = subjects[highest_average_subject_index]
print("Average scores for each subject:", average_scores)
print("Subject with the highest average score:", highest_average_subject)
