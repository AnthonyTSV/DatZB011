# 2. Patstāvīgā darba uzdevumi

## 1. uzdevums. Raindrops Simulation

In this exercise, we will take a look at the **terminal velocity** for raindrops.  
The terminal velocity is the velocity of a raindrop where the gravity pulls down the raindrop as much as the air resistance acts on it.

The terminal velocity $v_T$ (in m/s) for a raindrop with radius $r$ and assumed to be shaped as a perfect sphere is:

$$
v_T = \sqrt{\frac{8r\rho_v g}{3\rho C}}
$$

where:  
- $\rho_v = 1 \, g/cm^3 = 1000 \, kg/m^3$ is the approximate density of water  
- $g = 9.81 \, m/s^2$  
- $\rho = 1.293 \, kg/m^3$ is the approximate density of air  
- $C = 0.47$ describes how much resistance the raindrop exerts on its environment (in this case the air)

---

### a)

In this subtask you are **not** supposed to use the Numpy-module.

- Make a program which generates $N = 100000$ different raindrops represented by random values for their radii in the interval [1 mm, 6 mm] = [$10^{-3}$ m, $6 \cdot 10^{-3}$ m].  
- Your program is supposed to take the time on how long it takes to generate the $N$ raindrops and thereafter find the average terminal velocity.  
- Your program should then display the average terminal velocity along with how much time it used.

---

### b)

Extend your program from (a) such that it does the same calculations, however by using the **Numpy-module and vectorization**.  
Write out the terminal velocity along with the runtime of your program which uses vectorization and the Numpy-module.

In this subtask you will also see that it is a huge improvement in time using vectorization and the Numpy-module compared to the time we got from (a).

**Hint:** To take the time in seconds of a program, it is possible to use the `time`-module.  
An example of finding how long time your program uses to print `'Hello, world!'` is as follows:

```python
import time

time_start = time.time()        # To start taking time
print("Hello, world!")
time_used = time.time() - time_start   # Find how much time we have used

print("Time used: %g seconds" % time_used)
