import csv
import math


def read_csv_file(file_path):
    """
        Reads data from a CSV file and returns it as a list of lists.

        Parameters:
            file_path (str): The path to the CSV file to read.

        Returns:
            List[List[str]]: The CSV data as a list of lists, where each inner list represents a row in the CSV file.

        Raises:
            Exception: If there is an error reading the file, such as  file not found.
        """
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            csv_content = [row for row in reader]
            return csv_content
    except Exception as e:
        print("Error: ", e)


def calculate_quiz_statistics(csv_data):
    """
       Calculates the average and standard deviation for each quiz.

       Parameters: csv_data (List[List[str]]): The CSV data as a list of lists, where each inner list represents data
       about one student.

       Returns: List[Tuple[str, float, float]]: A list of tuples, where each tuple represents the average and
       standard deviation for a quiz.
       The tuple format is (quiz_name, quiz_average, quiz_std_dev).
    """
    quiz_stats = []

    # Loop through each quiz, ignoring the first two columns (name and ID)
    for i in range(2, len(csv_data[0])):
        # Create a list of scores for the current quiz, ignoring any empty rows
        quiz_scores = [int(row[i]) for row in csv_data if row[i]]

        # Calculate the average and standard deviation for the current quiz
        quiz_average = sum(quiz_scores) / len(quiz_scores)
        quiz_std_dev = calculate_standard_deviation(quiz_scores)

        # Add the quiz's statistics to the list
        quiz_stats.append((f"Quiz {i - 1}", quiz_average, quiz_std_dev))

    return quiz_stats


def calculate_student_statistics(csv_data):
    """
        Calculates the average and standard deviation for each student.

        Parameters: csv_data (List[List[str]]): The CSV data as a list of lists, where each inner list represents data
       about one student.

        Returns:
            List[Tuple[str, float, float]]: A list of tuples, where each tuple represents the average and standard
            deviation for a student.
            The tuple format is (student_name, student_average, student_std_dev).
        """
    student_stats = []

    # Loop through each student's data
    for i in range(0, len(csv_data)):
        # Extract the scores for the student, ignoring empty scores
        student_scores = [int(score) for score in csv_data[i][2:] if score]
        # If the student has no scores, skip them
        if not student_scores:
            continue

        # Calculate the average and standard deviation for the student's scores
        student_average = sum(student_scores) / len(student_scores)
        student_std_dev = calculate_standard_deviation(student_scores)

        # Append the student's name, average, and standard deviation to the results list
        student_stats.append((csv_data[i][0], csv_data[i][1], student_average, student_std_dev))
    return student_stats


def calculate_all_scores_statistics(csv_data):
    """
            Calculates the average and standard deviation for the all scores.

            Parameters: csv_data (List[List[str]]): The CSV data as a list of lists, where each inner list represents
            data about one student.

            Returns:
             tuple: A tuple containing the average and standard deviation of all scores in the CSV data.
            """

    # Create a list of all scores in the CSV data by iterating over each row and each score in the row,
    # ignoring empty scores.
    all_scores = [int(score) for row in csv_data for score in row[2:] if score != '']

    # Calculate the average and standard deviation for all the scores.
    all_scores_average = sum(all_scores) / len(all_scores)
    all_scores_std_dev = calculate_standard_deviation(all_scores)
    return all_scores_average, all_scores_std_dev


def calculate_standard_deviation(score_list):
    """
    Calculates the standard deviation of a given list of scores.

    Parameters:
    - score_list (List[float]): A list of numerical values.

    Returns:
    - float: The standard deviation of the score list. If the input list is empty, it returns 0.

    """

    # Check if the input list is empty
    if len(score_list) == 0:
        return 0

    # Calculate the mean of the score list
    mean = sum(score_list) / len(score_list)

    # Calculate the variance of the score list
    variance = sum((x - mean) ** 2 for x in score_list) / len(score_list)

    # Calculate the standard deviation
    standard_deviation = math.sqrt(variance)

    return standard_deviation


def display_statistics(csv_data):
    """
       Displays statistics for the CSV data, including the average and standard deviation for each quiz,
       the average and standard deviation for each student's scores across all quizzes, and the average
       and standard deviation for all scores.

       Parameters: csv_data (List[List[str]]): The CSV data as a list of lists, where each inner list represents
       data about one student.

       Returns:
       None
       """

    # Print average score and the standard deviation of each quiz
    print('Average score and the standard deviation of each quiz:')
    print(f'{calculate_quiz_statistics(csv_data)}\n')

    # Print average score and the standard deviation of each student's scores across all quizzes
    print("Average score and the standard deviation of each student's scores across all quizzes:")
    print(f'{calculate_student_statistics(csv_data)}\n')

    # Print average score and the standard deviation of all scores
    print('Average score and the standard deviation of all scores:')
    print(f'{calculate_all_scores_statistics(csv_data)}\n')


def main(file_path):
    """
       This function reads CSV data from a file and displays statistics.

       Parameters:
       file_path (str): The path to the CSV file to be read.

       Returns:
       None
       """
    data = read_csv_file(file_path)
    display_statistics(data)


if __name__ == "__main__":
    file_path = ".\cognata.csv"
    main(file_path)
