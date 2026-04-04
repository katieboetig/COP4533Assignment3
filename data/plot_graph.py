import matplotlib.pyplot as plt

tests= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
times= [0.057, 0.022, 0.021, 0.021, 0.021, 0.021, 0.024, 0.028, 0.042, 0.029]

plt.figure()
plt.plot(tests, times, marker='o')

plt.xlabel('Test Number')
plt.ylabel('Running Time (s)')
plt.title('Runtime Analysis')
plt.savefig('runtime_analysis.png')
plt.show()