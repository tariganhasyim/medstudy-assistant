"""
MedStudy Assistant

An AI-powered learning assistant for medical students.

Author:
Muhammad Hasyim Ashari

Version:
0.1.0
"""


class MedStudyAssistant:
    def __init__(self):
        self.version = "0.1.0"

    def start(self):
        print("=" * 40)
        print("MedStudy Assistant")
        print(f"Version: {self.version}")
        print("Status: Under Development")
        print("=" * 40)


def main():
    app = MedStudyAssistant()
    app.start()


if __name__ == "__main__":
    main()
