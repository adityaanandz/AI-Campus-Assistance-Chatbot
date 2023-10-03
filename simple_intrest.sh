#!/bin/bash

# Prompt the user for principal amount
read -p "Enter the principal amount: " principal

# Prompt the user for interest rate
read -p "Enter the annual interest rate (as a percentage): " rate

# Prompt the user for the time (in years)
read -p "Enter the time (in years): " time

# Calculate simple interest
interest=$(echo "scale=2; $principal * $rate * $time / 100" | bc)

# Display the result
echo "Simple Interest: $interest"
