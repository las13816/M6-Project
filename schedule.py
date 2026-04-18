import csv
from schedule_item import ScheduleItem


class Schedule:
    def __init__(self):
        self.courses = {} 

    def add_entry(self, item):
        self.courses[item.get_key()] = item

    def load_from_csv(self, filename):
        with open(filename, encoding='utf-8-sig', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    item = ScheduleItem(
                        subject=row['Subject'],
                        catalog=row['Catalog'],
                        section=row['Section'],
                        component=row['Component'],
                        session=row['Session'],
                        units=int(row['Units']),
                        tot_enrl=int(row['TotEnrl']),
                        cap_enrl=int(row['CapEnrl']),
                        instructor=row['Instructor']
                    )
                    self.add_entry(item)
                except ValueError:
                    continue

    def print_header(self):
        print(f"{'Subject':<6} {'Catalog':<7} {'Section':<7} "
              f"{'Component':<9} {'Session':<6} {'Units':<5} "
              f"{'TotEnrl':<7} {'CapEnrl':<7} {'Instructor'}")
        print("-" * 70)

    def print(self, items=None):
        if items is None:
            items = self.courses.values()

        self.print_header()
        for item in items:
            item.print()

    def find_by_subject(self, subject):
        return [c for c in self.courses.values()
                if c.subject.lower() == subject.lower()]

    def find_by_subject_catalog(self, subject, catalog):
        return [c for c in self.courses.values()
                if c.subject.lower() == subject.lower()
                and c.catalog == catalog]

    def find_by_instructor_last_name(self, last_name):
        return [c for c in self.courses.values()
                if last_name.lower() in c.instructor.lower()]