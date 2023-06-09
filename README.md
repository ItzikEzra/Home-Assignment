<h1>Introduction</h1> <br>
This program reads and processes CSV files that contain student grades for quizzes. It then generates statistical data based on the processed data. This is done to meet the requirements of the home assignment.

<h2>Functions</h2>
<h3>read_csv_file(file_path)</h3>
This function takes in a file path and returns the data in the file as a list of lists, where each inner list represents a row in the CSV file. If there is an error reading the file, such as the file not being found, the function raises an exception.

<br>
<h3>calculate_quiz_statistics(csv_data)</h3>
This function takes in a list of lists representing the CSV data, where each inner list represents data about one student. The function calculates the average and standard deviation for each quiz and returns a list of tuples, where each tuple represents the average and standard deviation for a quiz. The tuple format is (quiz_name, quiz_average, quiz_std_dev).

<h4>Algorithm:</h4>
<ol>
<li>Create an empty list to hold the quiz statistics.</li>
<li>For each quiz column in the CSV data (starting with the third column):</li>
<ol type="a">
<li>Create a list of scores for that quiz by iterating over each row in the CSV data and adding the score to the list if it is not empty.</li>
<li>Calculate the average score for the quiz by dividing the sum of the scores by the number of scores.</li>
<li>Calculate the standard deviation for the quiz using the <code>calculate_standard_deviation()</code> function.</li>
<li>Append a tuple containing the quiz name, average score, and standard deviation to the list of quiz statistics.</li>
</ol>
<li>Return the list of quiz statistics.</li>
</ol>
<br>
<h3>calculate_student_statistics(csv_data)</h3>
This function takes in a list of lists representing the CSV data, where each inner list represents data about one student. The function calculates the average and standard deviation for each student's scores across all quizzes and returns a list of tuples, where each tuple represents the average and standard deviation for a student. The tuple format is (student_name, student_ID, student_average, student_std_dev).
<h4>Algorithm:</h4>
<ol>
<li>Create an empty list to hold the student statistics.</li>
<li>For each row (i.e. each student) in the CSV data:</li>
<ol type="a">
<li>Create a list of scores for that student by iterating over the scores in the row and adding the score to the list if it is not empty.</li>
<li>If the list of scores is empty, skip to the next row.</li>
<li>Calculate the average score for the student by dividing the sum of the scores by the number of scores.</li>
<li>Calculate the standard deviation for the student using the <code>calculate_standard_deviation()</code> function.</li>
<li>Append a tuple containing the student name, ID, average score, and standard deviation to the list of student statistics.</li>
</ol>
<li>Return the list of student statistics.</li>
</ol>
<br>
<h3>calculate_all_scores_statistics(csv_data)</h3>
This function takes in a list of lists representing the CSV data, where each inner list represents data about one student. The function calculates the average and standard deviation for all scores across all quizzes and returns a tuple containing the average and standard deviation.
<h4>Algorithm:</h4>

<ol>
<li>Create an empty list to hold all the scores in the CSV data.</li>
<li>For each row in the CSV data, and for each score in each row:</li>
<ol type="a">
<li>If the score is not empty, append it to the list of all scores.</li>
<li>Calculate the average score for all the scores in the list by dividing the sum of the scores by the number of scores.</li>
<li>Calculate the standard deviation for all the scores using the <code>calculate_standard_deviation()</code> function.</li>
<li>Return a tuple containing the average score and standard deviation.</li>
</ol>
</ol>
<br>
<h3>calculate_standard_deviation(score_list)</h3>

This function takes in a list of numerical values and calculates the standard deviation of the list. If the input list is empty, the function returns 0.
<h4>Algorithm:</h4>
<ol>
<li>If the <code>score_list</code> is empty, return 0.</li>
<li>Calculate the mean of the scores in the <code>score_list</code>.</li>
<li>Calculate the variance of the scores in the <code>score_list</code>.</li>
<li>Calculate the standard deviation of the scores by taking the square root of the variance.</li>
<li>Return the standard deviation.</li>
</ol>
<br>
<h3>display_statistics(csv_data)</h3>
This function takes in a list of lists representing the CSV data, where each inner list represents data about one student. The function displays various statistics about the data, including the average and standard deviation for each quiz, the average and standard deviation for each student's scores across all quizzes, and the average and standard deviation for all scores. This function does not return anything; it simply prints the statistics to the console.
