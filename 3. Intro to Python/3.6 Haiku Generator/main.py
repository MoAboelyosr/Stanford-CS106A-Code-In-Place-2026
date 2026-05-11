from ai import call_gpt

def main():
   name = input("Enter your name: ")
   name = str(name)
   topic = input("Enter a topic: ")
   topic = str(topic)
   print("Creating your haiku...")
   print(call_gpt(f"write a haiku for someone called {name} about interested in {topic}."))


if __name__ == "__main__":
    main()