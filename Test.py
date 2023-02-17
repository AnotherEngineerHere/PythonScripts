import tkinter as tk
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

def publish_message():
    topic = topic_entry.get()
    message = message_entry.get()
    client.publish(topic, message)

def build_message():
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)

root = tk.Tk()
root.title("MQTT Publisher")

topic_label = tk.Label(root, text="Topic")
topic_label.grid(row=0, column=0, padx=10, pady=10)

topic_entry = tk.Entry(root)
topic_entry.grid(row=0, column=1, padx=10, pady=10)

message_label = tk.Label(root, text="Message")
message_label.grid(row=1, column=0, padx=10, pady=10)

message_entry = tk.Entry(root)
message_entry.grid(row=1, column=1, padx=10, pady=10)

publish_button = tk.Button(root, text="Publish", command=publish_message)
publish_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
