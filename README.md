# Zameen Calculator

This is a simple land area calculator designed to help users convert dimensions into Kanal, Marla, or Marla by other specific measurement methods. The calculator provides four options for calculating land area based on various units. 

## Features

1. **Kanal Calculation**: Calculates the area in Kanal.
2. **Marla Calculation**: Calculates the area in Marla.
3. **Foot Method**: Calculates the area in Marla using a Foot-based method.
4. **Karam Method**: Calculates the area in Marla using a Karam-based method.
5. **Exit Option**: Allows the user to exit the program.

## Usage

1. Run the code.
2. Follow the on-screen prompts to select your preferred calculation method.
3. Enter the `length` and `width` in feet (or the appropriate unit for the method chosen).
4. The program will output the total area in the selected unit.
5. Select **Exit** to terminate the program.

## Example Input and Output

### Kanal Calculation
```
Enter the length = 540
Enter the width = 400
Total Kanal = 4.0
```

### Marla Calculation
```
Enter the length = 540
Enter the width = 400
Total Marla = 80
```

### Foot Method
```
Enter the length = 540
Enter the width = 400
Total Marla = 80
```

### Karam Method
```
Enter the length = 540
Enter the width = 400
Total Marla = 24000
```

## How It Works

1. **Input Options**: The user selects an option by entering a number (1-5).
2. **Calculation**:
   - **Kanal**: `(length * width) / 272 / 20`
   - **Marla** (Standard, Foot Method): `(length * width) / 272`
   - **Karam Method**: `(length * width) / 9`
3. **Output**: The calculated area is displayed on the screen.

## Requirements

- Python 3.x

## Disclaimer

This calculator is designed for general estimates and should not be used as a replacement for professional surveying methods. Please consult a professional for precise measurements and calculations.
