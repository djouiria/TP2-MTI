
from AcademicElement import AcademicElement


class Unit(AcademicElement):

    def __init__(self, name, title, modules=None):
        super().__init__(name, title)

        self._modules = list(modules) if modules is not None else []

        self.coef = sum(
            module.coef for module in self._modules
        )

        self.credit = sum(
            module.credit for module in self._modules
        )

    def add_module(self, module):

        self._modules.append(module)

        self.coef = sum(
            module.coef for module in self._modules
        )

        self.credit = sum(
            module.credit for module in self._modules
        )

    def calculate_average(self):

        if not self._modules:
            return 0

        total_weighted = sum(
            module.calculate_average() * module.coef
            for module in self._modules
        )

        total_coef = sum(
            module.coef for module in self._modules
        )

        if total_coef == 0:
            return 0

        return total_weighted / total_coef

    def calculate_credits(self):

        if not self._modules:
            return 0
        if self.calculate_average() >= 10:
            return sum(
                module.credit for module in self._modules
            )

        return sum(
            module.calculate_credits()
            for module in self._modules
        )

    def summary(self):
        lines = [
            f"Unit: {self.title} ({self.name})",
            f"Coefficient: {self.coef}",
            f"Total credits: {self.credit}",
            f"Average: {self.calculate_average():.2f}",
            f"Credits earned: {self.calculate_credits()}",
            "Modules:",
        ]

        for module in self._modules:
            lines.append(
                f"  - {module.name}: {module.title}"
            )

        return "\n".join(lines)
