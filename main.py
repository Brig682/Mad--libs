def get_user_input(prompt):
  return input(prompt + ": ")

def create_story():
  # Get words from the user
  noun = get_user_input("Enter a noun")
  verb = get_user_input("Enter a verb")
  adjective = get_user_input("Enter an adjective")
  place = get_user_input("Enter a place")

  # Construct the story
  story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb}."
  story += f" They would often go to the {place} to {verb} and enjoy the beautiful scenery."

  return story

if __name__ == "__main__":
  user_story = create_story()
  print("\nHere's your story:\n")
  print(user_story)
