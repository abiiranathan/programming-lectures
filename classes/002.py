class Patient:
    def __init__(self, patient_id, name, age, gender, conditions=[]):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender

        # List to store patient's medical conditions
        self.conditions = conditions

    def add_condition(self, condition):
        self.conditions.append(condition)

    def get_conditions(self):
        return self.conditions

    def __str__(self):
        return f"Patient ID: {self.patient_id}\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}\nConditions: {self.conditions}"


class Condition:
    def __init__(self, name, description, severity):
        self.name = name
        self.description = description
        self.severity = severity

    def __str__(self):
        return f"Condition: {self.name}\nDescription: {self.description}\nSeverity: {self.severity}"


# Creating some sample patient data
patients = [
    Patient(
        1,
        "John Doe",
        45,
        "Male",
        [
            Condition("Hypertension", "High blood pressure", "Moderate"),
            Condition("Diabetes", "High blood sugar", "Mild"),
        ],
    ),
    Patient(
        2,
        "Jane Smith",
        32,
        "Female",
        [Condition("Asthma", "Respiratory condition", "Severe")],
    ),
    Patient(
        3,
        "Peter Jones",
        68,
        "Male",
        [Condition("Arthritis", "Joint inflammation", "Moderate")],
    ),
    Patient(
        4,
        "Mary Brown",
        28,
        "Female",
        [Condition("Anxiety", "Mental health condition", "Mild")],
    ),
]

# Analyzing patients within a specific age range
target_age_range = (30, 50)
condition_to_analyze = "Hypertension"

prevalence_count = 0
for patient in patients:
    if target_age_range[0] <= patient.age <= target_age_range[1]:
        if condition_to_analyze in [condition.name for condition in patient.conditions]:
            prevalence_count += 1

print(
    f"Prevalence of {condition_to_analyze} in patients between {target_age_range[0]} and {target_age_range[1]} years old: {prevalence_count}/{len(patients)}"
)
