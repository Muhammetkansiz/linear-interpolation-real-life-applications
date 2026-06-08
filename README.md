# Temperature Estimation Using Linear Interpolation 🌡️

This project demonstrates the application of numerical methods to solve real-world problems. It implements a **Linear Interpolation Model** in Python to estimate unknown air temperatures between specific known time intervals.

## Project Overview & Poster
Below is the comprehensive project infographic outlining the problem description, mathematical model, step-by-step calculations, and analytical findings.

![Project Poster](poster.jpg)

## Tech Stack & Tools
- **Language:** Python 3
- **Concepts:** Numerical Analysis, Linear Interpolation, Mathematical Modeling

## Use Cases & Adaptability (Any Linear Situation)
While this specific implementation estimates **air temperature**, the developed model is highly versatile and scalable. It can be seamlessly adapted to **any linear situation or time-series dataset**, such as:
- **Engineering & Physics:** Estimating velocity, pressure, or stress distribution changes over time.
- **IoT & Smart Systems:** Handling missing or corrupted sensor data in real-time monitoring systems where changes occur progressively.
- **Finance & Business:** Predicting constant growth rates or linear cost increases between known fiscal quarters.

## How It Works
The algorithm converts time into decimal formats (e.g., 11:15 becomes 11.25) and applies the standard linear interpolation formula:
y = y1 + ((x - x1) * (y2 - y1)) / (x2 - x1)
Given the data points at 10:00 (18°C) and 12:00 (24°C), the model successfully estimates the temperature at **11:15** to be **21.75 °C**.
