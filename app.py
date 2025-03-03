import streamlit as st


# Function to convert length units
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'miles': 0.000621371,
        'yards': 1.09361,
        'feet': 3.28084
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Function to convert temperature units
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value

# Function to convert mass units
def convert_mass(value, from_unit, to_unit):
    conversion_factors = {
        'grams': 1,
        'kilograms': 0.001,
        'milligrams': 1000,
        'pounds': 0.00220462,
        'ounces': 0.035274
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Streamlit app layout
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Title of the App
st.title("🔄 Unit Converter App")
st.markdown("### Convert between different units easily. Choose a category and enter the value to convert.")

# Create a container for the inputs and layout
with st.container():
    # Select category with icons
    category = st.selectbox(
        "Select category:",
        ("Length", "Temperature", "Mass"),
        format_func=lambda x: f"{x} {'🧳' if x == 'Length' else '🌡️' if x == 'Temperature' else '⚖️' if x == 'Mass' else ''}"
    )

    # Input field for value
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

    # Unit selections based on category
    if category == "Length":
        units = ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet"]
        from_unit = st.selectbox("From unit", units)
        to_unit = st.selectbox("To unit", units)

        if st.button("Convert"):
            result = convert_length(value, from_unit, to_unit)
            st.write(f"🔄 {value} {from_unit} is equal to {result} {to_unit}")

    elif category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
        from_unit = st.selectbox("From unit", units)
        to_unit = st.selectbox("To unit", units)

        if st.button("Convert"):
            result = convert_temperature(value, from_unit, to_unit)
            st.write(f"🔄 {value} {from_unit} is equal to {result} {to_unit}")

    elif category == "Mass":
        units = ["grams", "kilograms", "milligrams", "pounds", "ounces"]
        from_unit = st.selectbox("From unit", units)
        to_unit = st.selectbox("To unit", units)

        if st.button("Convert"):
            result = convert_mass(value, from_unit, to_unit)
            st.write(f"🔄 {value} {from_unit} is equal to {result} {to_unit}")

