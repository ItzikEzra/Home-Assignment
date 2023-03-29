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

    # Calculate quiz data, ignore first two columns, which include name and ID.
    # in this loop I represent the index of the cols.

    for i in range(2, len(csv_data[0])):
        # quiz_scores hold data for each quiz
        # if row[i] to ignore empty rows
        quiz_scores = [int(row[i]) for row in csv_data if row[i]]

        quiz_average = sum(quiz_scores) / len(quiz_scores)
        quiz_std_dev = calculate_standard_deviation(quiz_scores)
        # quiz #1 starting in index 2
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
    for i in range(0, len(csv_data)):
        student_scores = [int(score) for score in csv_data[i][2:] if score]
        if not student_scores:
            continue
        student_average = sum(student_scores) / len(student_scores)
        student_std_dev = calculate_standard_deviation(student_scores)
        student_stats.append((csv_data[i][0], student_average, student_std_dev))
    return student_stats


def calculate_all_scores_statistics(csv_data):
    """
            Calculates the average and standard deviation for the all scores.

            Parameters: csv_data (List[List[str]]): The CSV data as a list of lists, where each inner list represents
            data about one student.

            Returns:
             tuple: A tuple containing the average and standard deviation of all scores in the CSV data.
            """
    all_scores = [int(score) for row in csv_data[1:] for score in row[2:] if score != '']
    all_scores_average = sum(all_scores) / len(all_scores)
    all_scores_std_dev = calculate_standard_deviation(all_scores)
    return all_scores_average, all_scores_std_dev


def calculate_standard_deviation(score_list):
    if len(score_list) == 0:
        return 0
    mean = sum(score_list) / len(score_list)
    variance = sum((x - mean) ** 2 for x in score_list) / len(score_list)
    return math.sqrt(variance)


def display_statistics(csv_data):
    print('Average score and the standard deviation of each quiz:')
    print(f'{calculate_quiz_statistics(csv_data)}\n')
    print("Average score and the standard deviation of each student's scores across all quizzes:")
    print(f'{calculate_student_statistics(csv_data)}\n')
    print('Average score and the standard deviation of all scores:')
    print(f'{calculate_all_scores_statistics(csv_data)}\n')


def main(file_path):
    data = read_csv_file(file_path)
    display_statistics(data)


if __name__ == "__main__":
    file_path = ".\cognata.csv"
    main(file_path)
