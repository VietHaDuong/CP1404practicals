class ProgrammingLanguage:

    def __init__(self, language, typing, reflection, year):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == 'Dynamic'

    def is_reflection(self):
        return self.reflection == 'Yes'

    def __str__(self):
        return f'{self.language}, {self.typing} typing, Reflection = {self.reflection}, First appears in {self.year}'
