
# coding: utf-8

# In[ ]:

print("ElizaBETE Project (alpha) - https://github.com/marcelotournier/ElizaBETE")
print(" ")
print("===============")
print("DISCLAIMER - this code is only for educational purposes and cannot be used as a therapy of any kind. Seek professional assistance if you have any physical or emotional disorders.")
print(" ")
print("AVISO - Este código e seu uso se destina apenas a objetivos educacionais e de treinamento em programação. Não pode ser usado com propósitos terapêuticos. Se você possui qualquer suspeita de desordens físicas ou emocionais, procure assistência de um profissional.")
print("===============")
print(" ")

import re
import random


reflections = {
    "sou": "é",
    "estou": "está",
    "estava": "estava",
    "eu": "você",
    "eu faria": "você faria",
    "eu tenho": "você tem",
    "eu irei": "você irá",
    "faço": "faz",
    "tenho": "tem",
    "fará": "farei",
    "vou": "vai",
    "irei": "irá",
    "meu": "seu",
    "é": "sou",
    "você tem": "Eu tenho",
    "você irá": "eu irá",
    "você fará": "eu farei",
    "seu": "meu",
    "seus": "meus",
    "me": "se",
    "você": "eu",
}

psychobabble = [
    [r'preciso (.*)',
     ["Por que você precisa {0}?",
      "Realmente ajudaria se você tivesse {0}?",
      "Tem certeza que você necessita de {0}?"]],
    
    [r'por que você não ([^\?]*)\??',
     ["Você realmente acha que eu não {0}?",
      "Talvez, qualquer hora eu irei {0}.",
      "Você realmente quer que eu {0}?"]],

    [r'por que eu não posso ([^\?]*)\??',
     ["Você acha que você deveria ser capaz de {0}?",
      "Se você pudesse {0}, o que você faria?",
      "Eu não sei -- Por que você não {0}?",
      "Você já tentou mesmo?"]],

    [r'não posso (.*)',
     ["Como você sabe que não pode {0}?",
      "Talvez você possa {0} se você tentar.",
      "O que você precisa para conseguir {0}?"]],

    [r'estou (.*)',
     ["Você veio até aqui porque você está {0}?",
      "A quanto tempo você está {0}?",
      "Como você sente por estar {0}?"]],

    [r'você é ([^\?]*)\??',
     ["Importa se sou {0}?",
      "Você preferiria que eu não fosse {0}?",
      "I am Talvez você acredite que sou {0}.",
      "Pode ser que eu seja {0} -- O que você acha?"]],

    [r'você está ([^\?]*)\??',
     ["Importa se estou {0}?",
      "Você preferiria que eu não estivesse {0}?",
      "I am Talvez você acredite que estou {0}.",
      "Pode ser que eu esteja {0} -- O que você acha?"]],

    [r'o que (.*)',
     ["Por que você pergunta?",
      "Como é que uma resposta a esta pergunta ajudaria você?",
      "O que você acha?"]],

    [r'como (.*)',
     ["Como você acha que é isso?",
      "Talvez você mesmo possa responder a sua pergunta.",
      "O que realmente você quer perguntar?"]],

    [r'porque (.*)',
     ["Esta é a verdadeira razão?",
      "Que outras razões vêm na sua mente?",
      "Esta razão pode se aplicar a algo mais?",
      "Se {0}, o que mais pode ser verdade?"]],

    [r'(.*) desculpe (.*)',
     ["Há muitas vezes que não precisamos pedir desculpas.",
      "O que você sente quando pede desculpas?"]],

    [r'olá(.*)',
     ["Olá... Estou feliz por você passar aqui hoje.",
      "Olá... Como você está hoje?",
      "Oi, como vai hoje?"]],

    [r'oi(.*)',
     ["Olá... Estou feliz por você passar aqui hoje.",
      "Olá... Como você está hoje?",
      "Oi, como vai hoje?"]],
    
    [r'acho (.*)',
     ["Você duvida que {0}?",
      "Você realmente acha isso?",
      "Mas você não tem certeza que {0}?"]],

    [r'penso (.*)',
     ["Você duvida que {0}?",
      "Você realmente acha isso?",
      "Mas você não tem certeza que {0}?"]],
    
    [r'(.*) amigo (.*)',
     ["Fale mais sobre seus amigos.",
      "Quando você pensa em um amigo, o que vem na sua mente?",
      "Por que você não me fala mais sobre um amigo de infância?"]],

    [r'(.*) amiga (.*)',
     ["Fale mais sobre seus amigas.",
      "Quando você pensa em uma amiga, o que vem na sua mente?",
      "Por que você não me fala mais sobre uma amiga de infância?"]],
    
    [r'sim',
     ["Você parece muito certo disso.",
      "OK, mas você pode me contar mais?"]],

    [r'(.*) computador(.*)',
     ["Você realmente está falando de mim?",
      "Parece estranho falar com um computador?",
      "Como computadores fazem você se sentir?",
      "Você se sente ameaçado por computadores?"]],

    [r'(.*) robô(.*)',
     ["Você realmente está falando de mim?",
      "Parece estranho falar com um robô?",
      "Como robôs fazem você se sentir?",
      "Você se sente ameaçado por robôs?"]],

    [r'(.*) bot(.*)',
     ["Você realmente está falando de mim?",
      "Parece estranho falar com um bot?",
      "Como computadores fazem você se sentir?",
      "Você se sente ameaçado por computadores?"]],

    
    [r'é (.*)',
     ["Você acha que é {0}?",
      "Quem sabe é {0} -- O que você acha?",
      "Se fosse {0}, o que você faria?",
      "Poderia bem ser que {0}.",
      "Você parece ter muita certeza disso.",
      "Se eu dissesse a você que isso provavelmente não é {0}, o que você sentiria?"]],

    [r'você pode ([^\?]*)\??',
     ["O que faz você pensar que não posso {0}?",
      "Se eu pudesse {0}, o que aconteceria então?",
      "Por que você pergunta se eu posso {0}?"]],

    [r'posso ([^\?]*)\??',
     ["Talvez você não queira {0}.",
      "Você quer ser capaz de {0}?",
      "Se você pudesse {0}, você faria?"]],

    [r'você é (.*)',
     ["Por que você acha que eu sou {0}?",
      "Você teria prazer em pensar que sou {0}?",
      "Talvez você gostaria que eu fosse {0}.",
      "Talvez você realmente esteja falando de você mesmo?",
      "Por que você diz que eu sou {0}?",
      "Por que você pensa que eu sou {0}?",
      "Estamos falando sobre você ou sobre mim?"]],

    [r'eu não (.*)',
     ["Você realmente não {0}?",
      "Por que você não {0}?",
      "Você não quer {0}?"]],

    [r'sinto (.*)',
     ["Bom, conte-me mais sobre estes sentimentos.",
      "Você sente {0} com frequência?",
      "Normalmente, quando você sente {0}?",
      "Quando você sente {0}, o que você faz?"]],

    [r'tenho (.*)',
     ["Por que você me diz que você tem {0}?",
      "Você realmente tem {0}?",
      "Agora que você tem {0}, qual será o próximo passo?"]],

    [r'teria (.*)',
     ["Poderia explicar por que você teria {0}?",
      "Por quê você teria {0}?",
      "Who else knows that you would {0}?"]],

    [r'existe (.*)',
     ["Você acha que existe {0}?",
      "É provável que exista {0}.",
      "Você gostaria que houvesse {0}?"]],

    [r'meu (.*)',
     ["Entendo, seu {0}.",
      "Por que você diz que seu {0}?",
      "Quando seu {0}, como você se sente?"]],

    [r'você (.*)',
     ["Deveríamos estar discutindo sobre você, não sobre mim.",
      "Por que você fala isso de mim?",
      "Por que você se importa que eu {0}?"]],

    [r'por que (.*)',
     ["Por que você não me diz a razão de {0}?",
      "Por que você pensa {0}?"]],

    [r'quero (.*)',
     ["O que significaria para você - conseguir {0}?",
      "Por que você quer {0}?",
      "E se você não conseguir {0}, o que você vai fazer?"]],

    [r'(.*) mãe(.*)',
     ["Diga mais sobre sua mãe.",
      "Fale sobre seu relacionamento com sua mãe?",
      "How do you feel about your mother Como você se sente sobre a sua mãe?",
      "Como isto tem a ver com seus sentimentos agora?",
      "Boas relações na família são importantes."]],

    [r'(.*) pai(.*)',
     ["Diga mais sobre seu pai.",
      "Como pensar em seu pai faz você se sentir?",
      "Como você se sente sobre seu pai?",
      "Seu relacionamento com seu pai tem a ver com o que você sente agora?",
      "Você tem algum problema em mostrar carinho pela sua família?"]],

    [r'(.*) criança(.*)',
     ["Você teve amigos próximos quando era criança?",
      "Qual sua memória favorita da infância?",
      "Você lembra de sonhos ou pesadelos da infância?",
      "Na sua infância, outras crianças provocavam você?",
      "Como você acha que suas experiências de infância se encaixam com o que você sente hoje?"]],

    [r'(.*)\?',
     ["Por que você pergunta isso?",
      "Por favor, peço que avalie se você mesmo é capaz de responder esta pergunta.",
      "Quem sabe a resposta está dentro de você mesmo?",
      "Por que você não me diz a resposta?"]],

    [r'quit',
     ["Obrigado por conversar comigo.",
      "Adeus.",
      "Obrigado, a consulta custará R$150 :) Brincadeira! Até mais."]],

    [r'(.*)',
     ["Por favor, conte mais.",
      "Você pode me explicar com mais detalhes?",
      "Por que você diz -- {0}?",
      "Entendo.",
      "Muito interessante.",
      "{0}.",
      "Entendo.  E o que isto diz a você?",
      "Como isso faz você se sentir?",
      "Como você se sente quando você fala isso?"]]
]


def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)


def analyze(statement):
    for pattern, responses in psychobabble:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])


def main():
    print ("Olá. Como você está hoje?")

    while True:
        statement = input("> ")
        #statement = raw_input("> ")
        print (analyze(statement))

        if statement == "sair":
            break


if __name__ == "__main__":
    main()
main()

