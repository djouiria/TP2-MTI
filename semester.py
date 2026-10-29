from AcademicElement import AcademicElement


class Semester(AcademicElement):

    def __init__(self, name, title, units=None):
        super().__init__(name, title)

        self._units = list(units) if units is not None else []
        self.coef = sum(unit.coef for unit in self._units)
        self.credit = sum(unit.credit for unit in self._units)

    def add_unit(self, unit):
        self._units.append(unit)
        self.coef += unit.coef
        self.credit += unit.credit

    def find_module(self, code):
        for unit in self._units:
            for module in unit._modules:
                if module.name == code:
                    return module
        return None

    def calculate_average(self):

        if not self._units:
            return 0

        total_weighted = sum(
            unit.calculate_average() * unit.coef
            for unit in self._units
        )

        total_coef = sum(
            unit.coef for unit in self._units
        )

        if total_coef == 0:
            return 0

        return total_weighted / total_coef

    def calculate_credits(self):

        if not self._units:
            return 0
        if self.calculate_average() >= 10:
            return self.credit

        return sum(
            unit.calculate_credits()
            for unit in self._units
        )

    def summary(self):

        lines = [
            f"{self.title} ({self.name})",
            f"Average: {self.calculate_average():.2f}",
            f"Credits earned: {self.calculate_credits()}",
            "",
            "Units:",
        ]

        for unit in self._units:
            lines.append(
                f"  - {unit.name}: {unit.title} | "
                f"Average: {unit.calculate_average():.2f} | "
                f"Credits: {unit.calculate_credits()}"
            )

        return "\n".join(lines)
