# 2. daļa (EN)

## Pandēmijas modelēšana ar Diferenciālvienādojumiem un Python (_uzdevumi adaptēti no IN1900 UiO kursa_) ##

> [!IMPORTANT] Uzmanīgi!
> - Šī daļa ir 60% no 2. PD
> - Termiņš: piektdiena, 2025. gada 19. decembris, 23:59

> [!WARNING] AI izmantošana
>
> Ja izmantojat AI, piemērojiet to pakāpeniski vienai apakšproblēmai vienlaikus un pārbaudiet,
> vai iegūtais risinājums ir pareizs un vai jūs to saprotat, pirms pāriet uz nākamo soli.
>
> Ielīmējot visu problēmas aprakstu ChatGPT vai līdzīgos rīkos, jūs, visticamāk, iegūsiet risinājumu, bet ļoti iespējams, ka tas būs risinājums nedaudz atšķirīgai problēmai.
>
> Tas netiks apstiprināts, un var būt ļoti grūti pielāgot ģenerēto kodu, lai tas atbilstu projekta prasībām.
>
> Gadījumos, kad mums rodas aizdomas par pārmērīgu AI rīku izmantošanu, jums varlūgt paskaidrot savu kodu DatZB011 pasniedzējiem.
>
> Ja nevarat paskaidrot, kā strādā Jūsu kods, projekts netiks apstiprināts.

> [!NOTE] Padoms
> Lai labāk orientētos tēmā un saprastu vienādojumus var izlasīt šīs [grāmatas 5. nodaļu](https://link.springer.com/book/10.1007/978-3-031-46768-4).

## 1.0 Getting started

- Download the `files.zip` archive
- Unzip `files.zip` with Extract all to your prefered folder
![Extract All](images/extract.png)
- You should have `beta_values.txt`, `covid19.py`, `lockdown.py`, `outbreak.py`, `SEIR.py`, `ODESolver.py`, `README.md` and `SEIR0.py` files.
- Run `ODESolver.py` to check if everything works. It should output: `All methods passed the exact solution test.`
- Now we are ready to begin.

## Problem 1. Filename: `SEIR0.py`

### 1.1

- Implement a test function `test_SEIR0()` to verify that the call function of the class works correctly.
- Inside the test function you should create an instance of the class, using either the default parameter values or values you choose yourself.
- Then call the instance with suitable arguments `t`, `u`, for instance `t=0` and `u=[1,1,1,1,1,1]` or some other choice which makes it easy to calculate the result by hand, and compare the output with the expected values.
- Remember to compare the values with a tolerance (for instance `tol=1e-10`) since the outputs are floats.

> [!NOTE] Hint
> Here this can help `assert np.allclose(du, expected_du, atol=1e-10)`

### 1.2

- Make a function `solve_SEIR(model, T, N, S_0, E2_0)` which takes an instance of the `SEIR0` class as its first argument, and solves the system of
  differential equations.
- Use one of the solvers from the `SEIR0` hierarchy, for instance the `RungeKutta4` class.
- The equations should be solved from time `0` to `T`, where `T` the number of steps `N` are given as arguments to the function.
- The parameters `S_0`, `E2_0` are initial conditions for the `S` and `E2` categories. All other initial conditions are set to zero, so the complete initial condition for the ODE system should be `[S_0, 0, E2_0, 0, 0, 0]`. The function should return arrays `t`, `u` containing the time and the solution.

### 1.3

- Make a function `plot_SEIR(t, u)` for visualizing the components $S(t)$, $I(t)$, $Ia(t)$ and $R(t)$ in the same plot.
- Include a legend with labels for each curve, and labels on axes.

![Figure 1](images/figure1.png)
_Figure 1: Solution of the SEEIIR model. The plot shows the dynamics of the categories $S,I,Ia,R$._

### 1.4

- Finally, create an instance of the `SEIR0` class from 1.1 , with $\beta$ = 0.4, and
  the default values for all other parameters.
- Call the functions from 1.2 to solve the model for initial values `S_0 = 5.5e6`, `E2_0 = 100`, all other initial values
  zero, `T = 200`, and `N = 400`.
- Call the function from 1.3 to plot the solution.
- The resulting plot should look exactly like the one in Figure 1
- Make sure to put the function calls inside a test block at the bottom of the file, i.e.:

```python
if __name__ == "__main__":
    model = SEIR0(beta = 0.4)
    ...
```

Placing the code inside this test is useful since you will import from the `SEIR0.py` file in the following problems, and we don’t want these lines to be run when the code is imported.

## Problem 2. Modify the SEIR0 class. FIlename: `SEIR0.py`

In this exercise we will extend the class from Problem 1 to support a time dependent model parameters. The code shall be written as a separate file `SEIR.py`, which should import the necessary parts from `SEIR0.py`.

### 2.1

Write the class `SEIR` as a subclass of `SEIR0`. The new class should accept that the `beta` parameter can be given either as a constant or as a Python function (a function of time). This can be handled by placing an if test similar to this inside the constructor:

```python
if isinstance(beta, (float, int)): # is it a number?
  self.beta_function = lambda t: beta # wrap as function
elif callable(beta):
  self.beta_function = beta
super().__init__(self.beta_function(0), ...)
```

The rest of the parameters are just passed unmodified to the constructor of the base class.
The method `__call__(self, t, u)` will also be almost identical to the
class in Problem 1, so we can call the base class method to minimize code duplication. In the start of the `__call__` method you should update the attribute self.beta by an appropriate call to self.beta_function, and then you can call the method from the base class. Do not simply copy the methods from the SEIR0 class and modify them in the subclass. The point of inheritance is to minimize code duplication, and this is a key part of this Problem.

### 2.2

Write two test functions `test_SEIR_beta_const` and `test_SEIR_beta_var` to verify that the class works correctly. The first should test the class with a constant beta and can be identical to the test function in Problem 1. The other one should define a non-constant beta, for instance a linear or piecewise constant function, and check that the model gives the expected result for two different values of t.

### 2.3

Write a new function `plot_SEIR(t, u, components=['S','I','Ia','R'])`.
This should be a slightly more advanced version of the function from Problem 1, where the additional argument `components` is a list of strings/labels indicating which solution `components` we want to plot, from one to all six components of `u`. Apart from this flexibility, the function shall be the same as the one in Problem 1. In particular, because of the default value for the `components` argument, calling the new function as `plot_SEIR(t, u)` should result in exactly the same plot as the version from Problem 1.

### 2.4

Add the following block to the end of the file to call the test functions and then create an instance of the model class, solve the problem and plot the solution:

```python
if __name__ == "__main__":
    test_SEIR_beta_const()
    test_SEIR_beta_var()
    model = SEIR(beta = 0.4)
    t, u = solve_SEIR(model, T = 200, N = 400,
    S_0 = 5.5e6, E2_0 = 100)
    plot_SEIR(t,u)
```

The resulting plot should look exactly like the one you got in Problem 1. Find the
peak of the I category, either by a visual inspection of the plot or by a suitable
call to the builtin `max` function. Estimates from the early phase of the pandemic
indicated that about 20% of the infected cases would need hospital care, and
5% would need a mechanical ventilator. There are around 700 ventilators in
Norwegian hospitals. How does this number compare to your estimate?

## Problem 3. Simulate a pandemic outbreak. Filename: `outbreak.py`

In this exercise we will use the class `SEIR` and the solver functions from Problem 2 to simulate possible scenarios of the Covid19 pandemic in Norway. The code should be written in a separate file `outbreak.py`, which should import from `SEIR.py`.

Until now, we have assumed that $\beta$ is constant. The $\beta$ parameter describes the probability that a contagious person (in $E2,I,Ia$) meets and infects a susceptible person. In reality, $\beta$ depends on numerous factors, including the infectiousness of the disease itself, immunity of the population resulting from vaccination and previous infections, as well as the general behavior of the population. We will now extend our model to use a piecewise constant $\beta$.

Epidemiologists often refer to the reproduction number $R$ of an epidemic,
which is the average number of new persons that an infected person infects. The
critical number is $R = 1$, since if $R < 1$ the epidemic will decline, while for $R > 1$
it will grow exponentially. In the simplest models, the relationship between $R$
and $\beta$ is $R = \beta \tau$, where $\tau$ is the mean duration of the infectious period. In our model, which has multiple infectious categories, we have

$$
R = r_{e2} \beta / \lambda_2 + r_{ia} \beta / \mu + \beta / \mu,
$$

since the mean durations of the E2 period is $1/ \lambda _2$ and the mean duration of both $I$ and $Ia$ is $1/ \mu$. The choice of $\beta = 0.4$ gives $R \approx 3.2$, which is similar to
the values used by the Norwegian Institute of Public Health (FHI) to model the early stage of the outbreak in Norway, from mid February to mid March 2020. As we all
know, severe restrictions on travel and social interactions were introduced in
Norway on March 12, 2020. These restrictions substantially reduced the number
of contacts between infected and susceptible persons, which is represented in the
model as a reduction in the parameter $\beta$.

Write a function `beta(t)` which represents the piecewise constant $\beta$:

$$
\beta(t) = \begin{cases}
    0.4 & \text{if } t \leq 100 \\
    0.083 & \text{if } t > 100
\end{cases}
$$

Create an instance of the `SEIR` class with this piecewise constant $\beta$, and call the
`solve_SEIR` and `plot_SEIR` functions to solve the problem. The resulting plot should look like the one in Figure 2.

![Figure 2](images/figure2.png)
_Figure 2: Solution of the SEIR model with the discontinuous $\beta$ function. The plot shows the dynamics of the categories $S,I,Ia,R.$_

## Problem 4. Managing a pandemic. Filename: `lockdown.py`

As we are all very aware, the Covid19 pandemic had a substantial impact on society over a couple of years, and the number of infections increased and reduced in multiple waves. Numerous mutations of the virus affected its infectiousness,
and frequent changes in the restrictions on travel and social interactions also impacted the spread of the disease. In the models run by FHI to understand the pandemic and predict incoming waves, these changes were reflected as piecewise constant values of the $\beta$ parameter, similar to the model implemented in the previous problem, but with many more steps. A file `beta_values.txt` with suitable beta values should be in the `files` folder. The values are based on the parameter used by FHI in their real-world pandemic models, but slightly adapted to fit better to our model.

Implement a piecewise constant $\beta$ as a class `Beta`.
The class should have
(at least) three methods:

- A constructor `__init__(self, filename)`, which takes a file on the format of
`beta_values.txt` as argument, does the necessary processing of the file, and
stores the $\beta$ values and time intervals in suitable data structures.

This can be done in multiple ways, but one option is to store two lists of equal length; one containing the $\beta$ values and one containing the start date for the interval when each $\beta$ value applies. (With this approach you can ignore the end dates for each interval.) We can assume that $t = 0$ in our model corresponds to the date 15.02.2020, so the list of "dates" can be integers counting from that date. These lists can then be used as lookup tables inside the `__call__` method to evaluate $\beta$.

For converting from the dates in the file to an integer counting from the first date, the `datetime` module is useful. The most relevant parts of the `datetime` module are two classes called `date` and `timedelta`, so a
suitable import statement can be

```python
  from datetime import date, timedelta
```

It may also be useful to implement a method to convert from the date format used in the file to a `date` object. Such a method may, for instance, look like this:

```python
def str2date(self, date_str):
    """
    Convert a date string on the format dd.mm.yyyy
    to a datetime.date object
    """
    day, month, year = (int(n) for n in date_str.split('.'))
    return date(year, month, day)
```

If you have two dates represented as date objects, they can be subtracted to yield a `timedelta` object, and the number of days can be accessed as an attribute of the `timedelta` class named `days`. Here is a short example:

```python
# date0 and date1 are instances of class datetime.date
delta = date1 - date0
n_days = delta.days
```

Since the processing of the input file will require quite a few lines, the constructor can end up a bit long and messy. It may be useful to structure the code by defining one or more methods to perform the file reading and processing, and then calling the method(s) from the constructor.

- A `__call__(self, t)` method, which takes the time as input, and returns the $\beta$ value for the given day. If you created two lists in the constructor, as suggested above, a suitable approach will be to loop through these lists and add an appropriate `if` test to return the correct value of $\beta$.

There are many other ways this can be done, and some are probably more
elegant, but this is a simple approach that works.

- A method named `plot(self, T)` which takes a time point T as argument, and plots the $\beta$ function for $t$ between 0 and $T$.

> [!NOTE] Hint 1
> In order for the plot to capture the jumps and actually look like
a discontinuous function, you need to use quite a few t values. For
instance, using `t = np.linspace(0, T, 1000)` should make the plot look fairly good.

> [!NOTE] Hint 2
> If your `__call__` method contains one or more `if` tests, the
usual approach of sending the entire `t` array to the function will not work.
>
> A `for` loop or a call to `np.vectorize` may then be needed to compute the array of $\beta$ values.

If the class defined above is implemented correctly, the following test block should work. Add it to the bottom of your file.

```python
if __name__ == "__main__":
    from SEIR import SEIR, solve_SEIR, plot_SEIR
    beta = Beta("beta_values.txt")
    beta.plot(1000)

    model = SEIR(beta)
    t, u = solve_SEIR(model, T=1000, N=1000,
                      S_0=5.5e6, E2_0=100)
    plot_SEIR(t, u, components=["I", "Ia"])
```

The $\beta$ plot, which shows up first, should look similar to the Figure 3. It is not important that the plot looks exactly the same, but it should be very similar. The solution plot shows up when you close the first plot window, and should look like the Figure 4. As you can see, the solution does not look very interesting, and it does not properly capture the
multiple waves of infections observed in Norway. Can you think of what the model is missing, which makes it unable to capture the dynamics of the pandemic?

![Figure 3](images/figure3_5.png)
_Figure 3: The piecewise constant $\beta$ parameter read from file._

![Figure 4](images/figure3.png)
_Figure 4: Solution of the model with this choice of $\beta$._

## Problem 5. Extending the model. Filename: `covid19.py`

The plots from Problem 4 did not look too interesting, and did not really capture the dynamics of the Covid19 pandemic in Norway. There may be several reasons for why the model fails, but one possible explanation is that there is no import of infected people. After the first wave has been crushed by the lockdown, the number of infected persons is too low to start off new waves, even if the reproduction number $R > 1$ in some time intervals. The goal for this last part of the project is to modify the `SEIR` class to account for import of infected people.

There are several ways to include this in the model, and we shall adopt the
simple approach of adding a source term to the equation for the $E_2$ category.
The original equation reads

$$
\frac{dE_2}{dt} = \lambda_1 (1-p_a)E_1 - \lambda_2 E_2
$$

and we may simply modify this to

$$
\frac{dE_2}{dt} = \lambda_1 (1-p_a)E_1 - \lambda_2 E_2 + \Sigma \tag{1}
$$

to model an influx of $\Sigma$ people in the $E_2$ category per day. While this simple model may not be the most realistic, it is suitable for illustrating the impact of infection imports.

Implement a subclass `SEIRimport(SEIR)` of the class you created in Problem 2. Reuse as much code as possible from the base class. You need to modify both the constructor and the `__call__` method, since the constructor must take an additional parameter (`sigma`), and the call method includes the additional term in the equation for $E_2$. However, by calling the methods from the base class appropriately, both methods can be implemented with very little new code.

Repeat the last steps from Problem 4 using the modified model with
$\Sigma = 10$. The plot should look something like the one in Figure 5.

![Figure 5](images/figure5.png)
_The solution of the SEIR model with the piecewise constant $\beta$ parameter from Problem 4, and an influx of infected people as given by (1), with $\Sigma$ = 10._
