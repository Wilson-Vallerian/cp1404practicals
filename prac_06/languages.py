from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
print()
print("The dynamically typed languages are:")
languages = ProgrammingLanguage(python, ruby, visual_basic)
languages = [ruby, python, visual_basic]
for language in languages:
    if language.is_dynamic():
        print(language.field)


