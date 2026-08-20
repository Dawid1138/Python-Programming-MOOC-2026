class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points

    def __str__(self):
        return f'ExamSubmission (examinee: {self.examinee}, points: {self.points})'

def passed(submissions: list, lowest_passing: int):
    passed_list = [x for x in submissions if x.points >= lowest_passing]
    return passed_list