STUDENTS = 5 
scores = []
scoreSum = 0
for i in range(STUDENTS):
    value = int (input(" 성적을 입력하시요 : "))
    scores.append(value)
    scoreSum += value
scoreAvg = scoreSum / len (scores)
highScoreStudents = 0
for i in range( len (scores)):
    if scores[i] >= 80:
        highScoreStudents += 1

print(" 성적 평균은 ", scoreAvg , " 입니다 .")
print("80 점 이상 성적을 받은 학생은 ", highScoreStudents , " 명입니다 .")