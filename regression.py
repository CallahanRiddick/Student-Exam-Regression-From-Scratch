import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('student_exam_scores.csv')

# Didn't use this function just included it for reference/context.
def loss_function(m, b, points):
    sum_error = 0
    for i in range(len(points)):
        x = points.iloc[i].hours_studied
        y = points.iloc[i].exam_score
        sum_error += (y - (m * x + b)) ** 2
    sum_error / float(len(points))


def gradient_desent(m_cur, b_cur, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].hours_studied
        y = points.iloc[i].exam_score

        m_gradient += -(2/n) * x * (y - (m_cur * x + b_cur))
        b_gradient += -(2/n) * (y - (m_cur * x + b_cur))

    m = m_cur - m_gradient * L
    b = b_cur - b_gradient * L
    return m, b

m = 0
b = 0
L = 0.01
epochs = 1300

for i in range(epochs):
    if i % 100 == 0:
        print(f"Epoch: {i}")
    m, b = gradient_desent(m, b, data, L)

print(m, b)
plt.scatter(data.hours_studied, data.exam_score, color="black")
plt.plot(list(range(0, 13)), [m * x + b for x in range(0, 13)], color="green")
plt.show()

     
