from opengpt.usesless.model import Model

usesless = Model(model="gpt-4")

while True:

    prompt = input("Enter Query: ")

    usesless.SetupConversation(prompt)

    for r in usesless.SendConversation():

        print(r.choices[0].delta.content, end='')

    print()
