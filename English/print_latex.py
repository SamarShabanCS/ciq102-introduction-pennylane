from IPython.display import display, Markdown

def print_state_vector(array):
    # Start the LaTeX string directly in display mode with $$ for centering
    latex_str = r"$$\left|\psi\right\rangle = "

    # Loop through each element in the array
    for i, amplitude in enumerate(array):
        # Format real and imaginary parts
        real_part = f"{amplitude.real:.6f}" if amplitude.real != 0 else ""
        imag_part = (f"{amplitude.imag:+.6f}" + "i") if amplitude.imag != 0 else ""
        
        # Handle cases where we have both real and imaginary parts
        if real_part and imag_part:
            formatted_amplitude = real_part + imag_part
        elif real_part or imag_part:
            formatted_amplitude = real_part + imag_part
        else:
            formatted_amplitude = "0"
        
        # Add formatted amplitude to the LaTeX string
        latex_str += f"{formatted_amplitude} \\left|{i}\\right\\rangle + "
    
    # Remove the last unnecessary plus sign and close with $$
    latex_str = latex_str.rstrip(" + ") + r"$$"

    # Display the centered LaTeX formatted string
    display(Markdown(latex_str))