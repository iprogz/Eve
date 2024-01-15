import tensorflow as tf  # Example using TensorFlow

# Define layers with different functionalities
sensory_layer = tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=(28, 28, 1))
memory_layer = tf.keras.layers.LSTM(64)
reasoning_layer = tf.keras.layers.Dense(10, activation='softmax')

# Connect layers with skip connections
x = sensory_layer(inputs)
x = tf.keras.layers.Add()([x, memory_layer(x)])  # Skip connection
outputs = reasoning_layer(x)

import time
import playsound
import tkinter as tk
from tkinter import messagebox


def gradual_alarm(duration, frequency_start, frequency_end):
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        elapsed_time = time.time() - start_time
        percentage_complete = elapsed_time / duration
        frequency = int(frequency_start + percentage_complete * (frequency_end - frequency_start))

        log_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Frequency: {frequency}"
        log_text.insert(tk.END, log_entry + "\n")
        log_text.see(tk.END)  # Scroll to the end of the log

        winsound.Beep(frequency, 500)  # Beep for 500 milliseconds
        time.sleep(1)  # Wait for 1 second between beeps


def start_alarm():
    try:
        alarm_time = int(entry.get())
        if alarm_time <= 0:
            messagebox.showerror("Error", "Please enter a valid positive time value.")
            return

        start_button["state"] = "disabled"
        entry["state"] = "disabled"

        log_text.delete(1.0, tk.END)  # Clear previous log entries
        log_text.insert(tk.END, "Alarm Log:\n")

        print(f"Setting the alarm for {alarm_time} seconds from now...")
        gradual_alarm(alarm_time, 300, 2000)
        print("Time's up! Alarm complete.")
        messagebox.showinfo("Info", "Time's up! Alarm complete.")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number of seconds.")


app = tk.Tk()
app.title("Gradual Alarm Clock")

frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Enter time in seconds:")
label.pack()

entry = tk.Entry(frame)
entry.pack()

start_button = tk.Button(frame, text="Start Alarm", command=start_alarm)
start_button.pack()

log_text = tk.Text(frame, height=10, width=40)
log_text.pack()

app.mainloop()
