import time

def typing_speed_test():
    test_sentence = "The quick brown fox jumps over the lazy dog"
    print("Type the following sentence as fast as you can:\n")
    print(test_sentence)
    
    input("Press Enter when you are ready to start...")
    
    start_time = time.time()
    typed_sentence = input("\nStart typing: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words_typed = len(typed_sentence.split())
    typing_speed = (words_typed / elapsed_time) * 60
    
    print(f"\nYou typed {words_typed} words in {elapsed_time:.2f} seconds.")
    print(f"Your typing speed is {typing_speed:.2f} words per minute (WPM).")

if __name__ == "__main__":
    typing_speed_test()

