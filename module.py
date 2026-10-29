from AcademicElement import AcademicElement


class Module(AcademicElement):
    """يمثل مادة دراسية."""

    def __init__(
        self,
        name,
        title,
        coef,
        credit,
        hours_lecture=0,
        hours_td=0,
        hours_tp=0,
        teaching_mode="In-person",
        continous_percent=40,
        exam_percent=60,
    ):
        super().__init__(name, title)

        self.coef = coef
        self.credit = credit

        self.hours_lecture = hours_lecture
        self.hours_td = hours_td
        self.hours_tp = hours_tp

        self.teaching_mode = teaching_mode
        self.evaluation_continous_percent = continous_percent
        self.evaluation_exam_percent = exam_percent

        self._WEEKS = 15
        self.total_hours = self._WEEKS * (
            self.hours_lecture + self.hours_td + self.hours_tp
        )

        # العلامات تبدأ بصفر حتى لا يحدث خطأ عند حساب المعدل.
        self._grades = {
            "tp": 0,
            "td": 0,
            "exam": 0,
        }

    def set_grade(self, tp=None, td=None, exam=None):
        """تسجيل العلامات المتاحة فقط."""

        if tp is not None:
            self._grades["tp"] = tp

        if td is not None:
            self._grades["td"] = td

        if exam is not None:
            self._grades["exam"] = exam

    def calculate_average(self):
        """حساب معدل المادة حسب نسب التقييم."""

        tp = self._grades["tp"]
        td = self._grades["td"]
        exam = self._grades["exam"]

        continuous = self.evaluation_continous_percent

        percent_tp = 0
        percent_td = 0

        # إذا كانت المادة تحتوي على TD وTP،
        # نقسم نسبة التقييم المستمر بينهما بالتساوي.
        if self.hours_tp > 0 and self.hours_td > 0:
            percent_tp = continuous / 2
            percent_td = continuous / 2

        elif self.hours_tp > 0:
            percent_tp = continuous

        elif self.hours_td > 0:
            percent_td = continuous

        average = (
            tp * percent_tp / 100
            + td * percent_td / 100
            + exam * self.evaluation_exam_percent / 100
        )

        return average

    def calculate_credits(self):
        """تُكتسب أرصدة المادة إذا كان معدلها 10 أو أكثر."""

        if self.calculate_average() >= 10:
            return self.credit

        return 0

    def summary(self):
        """إرجاع معلومات المادة في نص."""

        return (
            f"Module: {self.title} ({self.name})\n"
            f"Coefficient: {self.coef}\n"
            f"Credits: {self.credit}\n"
            f"Total hours: {self.total_hours}\n"
            f"Lecture: {self.hours_lecture}, "
            f"TD: {self.hours_td}, TP: {self.hours_tp}\n"
            f"Teaching mode: {self.teaching_mode}\n"
            f"Evaluation: Continuous "
            f"{self.evaluation_continous_percent}%, "
            f"Exam {self.evaluation_exam_percent}%\n"
            f"Average: {self.calculate_average():.2f}"
        )
