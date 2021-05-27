def decrypt_story():
    storyEncyrpted = CiphertextMessage(get_story_string())
    return storyEncyrpted.decrypt_message()
