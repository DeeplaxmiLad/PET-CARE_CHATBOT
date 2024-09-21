import tkinter as tk
from tkinter import scrolledtext

# Function to handle the chatbot responses
def get_response(user_input):
    user_input = user_input.lower()

    # Basic responses for the chatbot
    responses =  {
        "hi": "Hello! How can I help you with your pet today?",
        "hello": "Hi! How can I assist you?",
        "dog care": "Make sure to give your dog regular exercise, balanced meals, and regular vet checkups.",
        "cat care": "Cats love clean litter boxes, balanced meals, and occasional vet visits.",
        "how often should i feed my dog": "Adult dogs should be fed twice a day, puppies more frequently.",
        "how often should i feed my cat": "Cats generally should be fed 2-3 small meals a day, but it depends on their health and age.",
        "what food is best for dogs": "High-quality commercial dog food is usually best, but consult your vet for specific needs like allergies or health issues.",
        "what food is best for cats": "Cats thrive on high-protein, grain-free food. Wet food helps with hydration. Consult your vet for the best diet.",
        "how to train my dog": "Consistency is key! Start with basic commands like sit, stay, and come. Positive reinforcement works best.",
        "how to stop my dog from barking": "Identify the reason for barking. Training, exercise, and distraction with toys often help reduce excessive barking.",
        "how to litter train my cat": "Place the litter box in a quiet area, show your cat where it is, and keep it clean. Most cats will naturally use it.",
        "why is my dog shedding a lot": "Shedding is normal, but if it's excessive, ensure your dog is eating a proper diet, and brush them regularly. Consult a vet if needed.",
        "why is my cat not eating": "Cats can stop eating due to stress or illness. If they haven't eaten for 24 hours, consult your vet.",
        "best toys for dogs": "Interactive toys like puzzle feeders, chew toys, and fetch toys are great for mental and physical stimulation.",
        "best toys for cats": "Cats love toys that simulate hunting, like feather toys, laser pointers, and balls they can chase.",
        "how to groom my dog": "Brush your dog regularly to prevent matting, bathe them occasionally, and trim their nails. Regular grooming helps keep them clean and comfortable.",
        "how to groom my cat": "Most cats groom themselves, but you can brush them to reduce shedding and hairballs. Long-haired cats may need more frequent grooming.",
        "how to introduce my dog to a new pet": "Introduce them in a neutral environment, keep both pets calm, and supervise their interactions until they become comfortable with each other.",
        "how to introduce my cat to a new pet": "Cats are territorial, so give them time to adjust. Keep the new pet separate at first and introduce them slowly, supervised.",
        "is there any insurance for pet? one line answer": "Yes, pet insurance exists and covers veterinary expenses for illnesses, accidents, and sometimes routine care.",
        "should i get pet insurance": "Pet insurance can be a great way to cover unexpected medical expenses. Research different plans to see which fits your budget and needs.",
        "how to tell if my pet is sick": "Signs of illness include loss of appetite, lethargy, vomiting, diarrhea, and changes in behavior. Consult a vet if you notice any of these symptoms.",
        "why does my dog eat grass": "Some dogs eat grass to aid digestion or because they like the taste. It's generally harmless unless they vomit frequently afterward.",
        "why is my cat meowing a lot": "Excessive meowing could mean your cat is hungry, bored, or seeking attention. If it continues, check with a vet for any health issues.",
        "why is my dog licking its paws": "Licking could be due to allergies, boredom, or anxiety. If it’s excessive, check with your vet.",
        "why is my cat scratching the furniture": "Cats scratch to mark territory, stretch, and keep their claws sharp. Provide scratching posts and pads to prevent furniture damage.",
        "how often should i walk my dog": "Most dogs benefit from at least two walks per day, but the amount of exercise depends on the breed and age.",
        "can cats and dogs live together": "Yes, with careful introductions and supervision, cats and dogs can live together peacefully. Patience is key!",
        "how to stop my dog from chewing furniture": "Provide chew toys, increase exercise, and use deterrent sprays to discourage chewing. Training is essential.",
        "how to socialize a puppy": "Expose your puppy to different environments, people, and animals at an early age. Positive reinforcement will help them feel safe.",
        "can i give my dog human food": "Some human foods like chicken and rice are safe for dogs, but avoid toxic foods like chocolate, grapes, onions, and garlic.",
        "can i give my cat human food": "Cats should mainly eat cat food, but small amounts of plain meat are okay. Avoid toxic foods like onions, garlic, and chocolate.",
        "why is my dog panting a lot": "Dogs pant to cool down, but excessive panting can indicate stress, pain, or illness. If you're concerned, consult your vet.",
        "why does my cat purr": "Cats purr for various reasons, including contentment, relaxation, and even to self-soothe when in pain or stressed.",
        "how to stop a dog from jumping on people": "Teach your dog to sit when greeting people and reward calm behavior. Consistency and positive reinforcement help prevent jumping.",
        "why is my cat hiding all the time": "Cats hide due to stress, illness, or fear. Make sure they feel safe in their environment and consult a vet if hiding persists.",
        "why is my dog digging holes in the yard": "Dogs dig for fun, to cool off, or to bury objects. Provide distractions, toys, and exercise to curb this behavior.",
        "how to cut my dog’s nails": "Use a dog-specific nail clipper, and only trim small amounts to avoid hitting the quick. A vet or groomer can also help.",
        "how to clean my cat’s ears": "Gently clean your cat’s ears with a cotton ball and vet-approved cleaner. Avoid using cotton swabs inside the ear canal.",
        "why does my dog have bad breath": "Bad breath can indicate dental disease or digestive issues. Regular dental care and checkups can help keep your dog's breath fresh.",
        "why is my cat vomiting": "Occasional vomiting can be normal, but frequent vomiting can signal illness or food intolerance. Consult your vet if it continues.",
        "what should i do if my dog eats chocolate": "Chocolate is toxic to dogs. Contact your vet immediately and monitor for symptoms like vomiting, diarrhea, and restlessness.",
        "how to help a dog with separation anxiety": "Provide comfort toys, gradually increase alone time, and consider crate training. For severe cases, consult a vet or trainer.",
        "why is my cat kneading me": "Cats knead as a sign of comfort and contentment, mimicking a behavior they did as kittens to their mothers.",
        "how to stop my cat from biting": "Biting can be a sign of play or aggression. Redirect biting to toys and stop play if biting occurs. Consult a vet if needed.",
        "what is the best flea prevention for pets": "There are several options like topical treatments, oral medications, and collars. Consult your vet to choose the best method for your pet.",
        "how to help a dog lose weight": "Reduce portion sizes, choose low-calorie food, and increase exercise. Always consult your vet before starting a weight-loss plan.",
        "why does my cat bring me dead animals": "Cats bring prey to their humans as a form of gifting or showing off their hunting skills. It’s an instinctual behavior.",
        "how to keep my dog cool in hot weather": "Provide plenty of water, avoid walks during peak heat, and offer shade or cooling mats. Never leave your dog in a hot car.",
        "what to do if my cat escapes": "Stay calm, search your home and neighborhood, and put out food or bedding with their scent. Consider notifying neighbors and shelters."
    }



    # If user input matches a question, return response, else ask for more info
    return responses.get(user_input, "I'm not sure about that. Can you ask something else?")

# Function to send the user's message and get the response
def send_message():
    user_message = entry.get()
    if user_message.strip():
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + user_message + "\n")
        response = get_response(user_message)
        chat_window.insert(tk.END, "Bot: " + response + "\n\n")
        chat_window.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
        chat_window.yview(tk.END)

# Initialize tkinter window
window = tk.Tk()
window.title("Pet Care Chatbot")

# Chat window
chat_window = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
chat_window.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Entry widget to get user input
entry = tk.Entry(window, width=40)
entry.grid(row=1, column=0, padx=10, pady=10)

# Send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the GUI loop
window.mainloop()
