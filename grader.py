import pennylane as qml
from pennylane import numpy as np

class Exercise:
    def __init__(self, name, expected_device, expected_output):
        self.name = name
        self.expected_device = expected_device
        self.expected_output = expected_output

class Answer:
    def __init__(self, device, qnode, shots = None, circuit_params=None):            
        self.device = device
        self.qnode = qnode 
        self.shots = shots
        self.circuit_params = circuit_params
        
        empty_shots = shots is None
        empty_params = circuit_params is None #True if none
        
        if empty_shots and empty_params:
            self.output = qnode()
        elif not(empty_shots) and empty_params:
            self.output = qnode(shots = shots)
        elif empty_shots and not(empty_params):
            self.output = qnode(circuit_params)
        else: 
            self.ouput = qnode(circuit_params, shots = shots ) #test this

#Check if user's device matches the expected device
def check_device(user_device, expected_device):
    try:
        #Check if device name matches expected name. 
        #Might not be necessary?
        assert user_device.name == expected_device['name']

        #Check if number of wires matches expected number of wires
        assert len(user_device.wires) == expected_device['num_wires']
        return True
    except AssertionError:
        return False

#Check if the user's output matches the expected output
def check_output(user_output, expected_output):
    try:
        #Check if user's answer matches expected output
        if np.allclose(user_output, expected_output):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error during execution: {e}")
        return False

def grade(exercise, answers):

    print(f"Checking exercise: {exercise.name}")

    # Initialize an empty list to store the outputs of the answers
    arr = []

    # Check if answers is a single Answer object. If so, convert it to a list
    if not isinstance(answers, list): 
        answers = [answers]
    # Iterate over each answer to do the necessary checks
    for a in answers:
        try:
            if not check_device(a.device, exercise.expected_device):
                raise Error("The device is incorrectly defined")
        except Exception as e:
            print(f"{e}")

        arr.append(a.output)
    try:    
         # Check if the combined output of the answers matches the expected output.
        if not check_output(arr, exercise.expected_output):
            print(arr, exercise.expected_output)
            raise Exception("The output is incorrect") 
        print("Correct")
    except Exception as e:
        print(f"{e}")
        
#Solutionnaire 
exercise_bell_pair = Exercise(
    name="Bell Pair",
    expected_device={'name': 'default.qubit', 'num_wires': 2},
    expected_output=np.array([0.70710678+0.j, 0.+0.j, 0.+0.j, 0.70710678+0.j])
)
exercise_psi_moins = Exercise(
    name="psi_moins",
    expected_device={'name': 'default.qubit', 'num_wires': 2},
    expected_output=np.array([ 0.70710678+0.j, 0.+0.j,  0.+0., -0.70710678+0.j])
)
exercise_phi_plus = Exercise(
    name="phi_plus",
    expected_device={'name': 'default.qubit', 'num_wires': 2},
    expected_output=np.array([0.+0.j, 0.70710678+0.j, 0.70710678+0.j, 0.+0.j])
)
exercise_phi_moins = Exercise(
    name="phi_moins",
    expected_device={'name': 'default.qubit', 'num_wires': 2},
    expected_output=np.array([ 0.+0.j,  0.70710678+0.j, -0.70710678+0.j, 0.+0.j])
)
exercise_prepare_with_gate = Exercise(
    name="prepare with gate",
    expected_device={'name': 'default.qubit', 'num_wires': 1},
    expected_output=np.array([ 0.8660254+0.j , 0.       -0.5j])
)
exercise_prepare_with_mottonen = Exercise(
    name="prepare with Mottonen",
    expected_device={'name': 'default.qubit', 'num_wires': 1},
    expected_output=np.array([np.sqrt(3)/2, 0.5j]),
)
exercise_expval = Exercise(
    name="Expectation Value",
    expected_device={'name': 'default.qubit', 'num_wires': 1},
    expected_output=np.array(0.0),
)
exercise_echantillons = Exercise(
    name="Échantillonage",
    expected_device={'name': 'default.qubit', 'num_wires': 1},
    expected_output=np.array([-1.0, 0.08, -0.026, 0.0036, 0.00326])
)