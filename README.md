# asgmt-1-programming-design-2026

> Programming Design 2026

## 01. Define a function `is_return_necessary_for_assignments()` which answers whether a `return` statement is necessary or not in our assignments.

```python
def is_return_necessary_for_assignments() -> bool:
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a function `calculate_movie_minutes()` which returns the time of a movie in minutes given hours and minutes.

```python
def calculate_movie_minutes(hours: int, mins: int) -> int:
    """
    >>> calculate_movie_minutes(2, 22) # The Shawshank Redemption
    142
    >>> calculate_movie_minutes(2, 55) # The Godfather
    175
    >>> calculate_movie_minutes(2, 32) # The Dark Knight
    152
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a function named `say_hello_to_anyone()` which says Hello to anyone given a name.

```python
def say_hello_to_anyone(anyone: str) -> str:
    """
    >>> say_hello_to_anyone("world")
    'Hello World!'
    >>> say_hello_to_anyone("python")
    'Hello Python!'
    >>> say_hello_to_anyone("tony")
    'Hello Tony!'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a function `format_number_of_assignments_exams_bonuses()` which returns the number of assignments, exams, and bonuses for this course.

```python
def format_number_of_assignments_exams_bonuses(n_assignments: int, n_exams: int, n_bonuses: int) -> str:
    """
    >>> format_number_of_assignments_exams_bonuses(6, 2, 2)
    '6 assignments 2 examinations 2 bonuses.'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a function `repeat_n_times()` which returns a concatenated `str` given an integer `n`.

```python
def repeat_n_times(str_to_repeat: str, n: int) -> str:
    """
    >>> repeat_n_times("Important!", 3)
    'Important!Important!Important!'
    >>> repeat_n_times("Go!", 3)
    'Go!Go!Go!'
    >>> repeat_n_times("Awesome!", 2)
    'Awesome!Awesome!'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `format_temperature_degrees()` which returns Fahrenheit degrees in text format given Celsius degrees.

$$
\text{Fahrenheit}^{\circ} \text{F} = \text{Celsius}^{\circ} \text{C} \times \frac{9}{5} + 32
$$

```python
def format_temperature_degrees(celsius: int) -> str:
    """
    >>> format_temperature_degrees(0)
    '0 Degrees Celsius = 32.0 Degrees Fahrenheit'
    >>> format_temperature_degrees(100)
    '100 Degrees Celsius = 212.0 Degrees Fahrenheit'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `format_integer_with_dollar_sign_and_commas()` which returns a comma format with dollar sign given an integer.

```python
def format_integer_with_dollar_sign_and_commas(x: int) -> str:
    """
    >>> format_integer_with_dollar_sign_and_commas(1000)
    '$1,000'
    >>> format_integer_with_dollar_sign_and_commas(1000000)
    '$1,000,000'
    >>> format_integer_with_dollar_sign_and_commas(1000000000)
    '$1,000,000,000'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `is_positive()` which returns whether input is a positive integer or not.

```python
def is_positive(x: int) -> bool:
    """
    >>> is_positive(-1)
    False
    >>> is_positive(0)
    False
    >>> is_positive(1)
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `is_even()` which returns whether input is an even number or not.

```python
def is_even(x: int) -> bool:
    """
    >>> is_even(0)
    True
    >>> is_even(1)
    False
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(4)
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `are_vowels_contained()` which returns whether input text contains one of the vowels: a, e, i, o, u.

```python
def are_vowels_contained(x: str) -> bool:
    """
    >>> are_vowels_contained('pythn')
    False
    >>> are_vowels_contained('ncnd')
    False
    >>> are_vowels_contained('rtclt')
    False
    >>> are_vowels_contained('python')
    True
    >>> are_vowels_contained('anaconda')
    True
    >>> are_vowels_contained('reticulate')
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```