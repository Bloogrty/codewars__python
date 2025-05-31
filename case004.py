# Name: Welcome!
# Link: https://www.codewars.com/kata/577ff15ad648a14b780000e7/train/python

def greet(language):
  greetings = {
        "english": "Welcome",
        "czech": "Vitejte",
        "danish": "Velkomst",
        "dutch": "Welkom",
        "estonian": "Tere tulemast",
        "finnish": "Tervetuloa",
        "flemish": "Welgekomen",
        "french": "Bienvenue",
        "german": "Willkommen",
        "irish": "Failte",
        "italian": "Benvenuto",
        "latvian": "Gaidits",
        "lithuanian": "Laukiamas",
        "polish": "Witamy",
        "spanish": "Bienvenido",
        "swedish": "Valkommen",
        "welsh": "Croeso"
    }
  
  try:
    return greetings[language]
  except KeyError:
    return greetings["english"]
  # return greetings.get(language, "Welcome")