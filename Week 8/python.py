import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Temperature': [23, 23, 21, 20, 19, 15, 12, 23, 25, 30],
    'Movement':    [1,  0,  1,  1,  1,  1,  1,  0,  0,  1]
}

df = pd.DataFrame(data)
print(df)

plt.figure(figsize=(10, 5))
plt.plot(df['Temperature'], label="Temperature")
plt.plot(df['Movement'], label="Movement")
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Temperature and Movement over time')
plt.legend()
plt.show()
