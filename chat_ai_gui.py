import tkinter as tk
from tkinter import scrolledtext, END
import os
from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY")

client = OpenAI()


# Function to handle user input and display chatbot response
def handle_user_input():
    user_input = user_input_box.get("1.0", END).strip()
    user_input_box.delete("1.0", END)

    if user_input.lower() == "exit":
        chat_log.insert(tk.END, "Chatbot: Goodbye!\n")
        root.quit()
    else:
        chat_log.insert(tk.END, "You: " + user_input + "\n")

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
                {"role": "user", "content": user_input}
            ]
        )

        generated_text = response.choices[0].message.content
        chat_log.insert(tk.END, "Chatbot: " + generated_text + "\n")


# Main GUI window
root = tk.Tk()
root.title("Chatbot with OpenAI")

# Chat log
chat_log = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD)
chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# User input box
user_input_box = scrolledtext.ScrolledText(root, width=40, height=4, wrap=tk.WORD)
user_input_box.grid(row=1, column=0, padx=10, pady=10)

# Send button
send_button = tk.Button(root, text="Send", command=handle_user_input)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
