import json


class HospitalSystem:
    def __init__(self, name):
        self.patients = []
        self.doctors = []
        self.name = name
        self.appointments = []
        self.load()

    def add_patient(self):
        name = input("Enter name: ")
        age = input("Enter age: ")
        illness = input("Enter illness: ")
        new_patient = Person(name, age, illness)
        self.patients.append(new_patient)
        self.save()

    def add_doctor(self):
        name = input("Enter doctor name: ")
        specialty = input("Enter specialty: ")
        schedule = input("Enter available times (comma-separated): ").split(",")
        id_number = input("Enter ID: ")
        new_doctor = Doctor(name, specialty, schedule, id_number)
        self.doctors.append(new_doctor)
        self.save()

    def book_appointment(self):
        pn = input("Enter the patient name: ")

        print("\nAvailable Doctors:")
        for doc in self.doctors:
            print(f"Dr. {doc.name} ({doc.specialty}) - Available: {', '.join(doc.schedule)}")

        dn = input("Enter the Doctor's name: ").lower()

        for doc in self.doctors:
            if dn == doc.name.lower():
                pt = input("Enter the preferred time: ").strip()
                if pt in doc.schedule:
                    print("✅ Appointment Approved")
                    appointment = {"patient": pn, "Doctor": doc.name, "time": pt}
                    self.appointments.append(appointment)
                    doc.schedule.remove(pt)
                    return
                else:
                    print("❌ Time not available for that doctor.")
                    return

        print("❌ Doctor not found.")
        self.save()

    def view_appointments(self):
        for appointment in self.appointments:
            print(
                f"The patient {appointment['patient']} has a meeting with Dr. {appointment['Doctor']} at {appointment['time']}.")

    def show_doctors(self):
        for doc in self.doctors:
            print(f"Dr. {doc.name} ({doc.specialty})")

    def show_patients(self):
        for patient in self.patients:
            print(f"{patient.name} - {patient.illness}")

    def load(self):
        try:
            with open("Hospital.json", "r") as f:
                data = json.load(f)

                self.patients = []
                for p in data.get("Patients", []):
                    patient = Person(p["name"], p["age"], p["illness"])
                    self.patients.append(patient)

                self.doctors = []
                for d in data.get("Doctors", []):
                    doctor = Doctor(d["name"], d["specialty"], d["schedule"], d["id"])
                    self.doctors.append(doctor)

                self.appointments = data.get("Appointments", [])

                print("✅ Data loaded successfully!")

        except FileNotFoundError:
            print("⚠️ File not found. Starting with empty data.")
        except json.JSONDecodeError:
            print("❌ Failed to load JSON data. File might be corrupted.")

    def save(self):
        # Convert patients and doctors to dictionaries
        patients_data = [{"name": p.name, "age": p.age, "illness": p.illness} for p in self.patients]
        doctors_data = [{"name": d.name, "specialty": d.specialty, "schedule": d.schedule, "id": d.id} for d in
                        self.doctors]

        all_info = {
            "Patients": patients_data,
            "Doctors": doctors_data,
            "Appointments": self.appointments
        }

        with open("Hospital.json", "w") as f:
            json.dump(all_info, f, indent=4)


class Doctor:
    def __init__(self, name, specialty, schedule: list[str], id_number):
        self.name = name
        self.specialty = specialty
        self.schedule = schedule
        self.id = id_number


class Person:
    def __init__(self, name, age, illness):
        self.name = name
        self.age = age
        self.illness = illness

    def show_info(self):
        print(f"Patient = {self.name}")
        print(f"Age = {self.age}")
        print(f"Illness = {self.illness}")
hospital = HospitalSystem("City Hospital")
hospital.load()  # Load existing data at the start

while True:
    print("\n--- Welcome to City Hospital System ---")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Book Appointment")
    print("4. View Appointments")
    print("5. Show All Doctors")
    print("6. Show All Patients")
    print("7. Exit")

    choice = input("Choose an option (1-9): ")

    if choice == "1":
        hospital.add_patient()
    elif choice == "2":
        hospital.add_doctor()
    elif choice == "3":
        hospital.book_appointment()
    elif choice == "4":
        hospital.view_appointments()
    elif choice == "5":
        hospital.show_doctors()
    elif choice == "6":
        hospital.show_patients()
    elif choice == "7":
        print("👋 Exiting the system. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
