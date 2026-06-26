# Message Class
'''class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def __str__(self):
        return f"{self.sender.username}: {self.content}"


# User Class
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} is not in a chatroom!")
        else:
            message = Message(self, content)
            self.chatroom.broadcast_message(message)


# ChatRoom Class
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.chat_history = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast_message(self, message):
        self.chat_history.append(message)
        print(message)

    def show_history(self):
        print(f"\n--- Chat History of {self.name} ---")
        for msg in self.chat_history:
            print(msg)
        print("-----------------------------------\n")




python_room = ChatRoom("Python Room")
java_room = ChatRoom("Java Room")
ai_room = ChatRoom("AI Room")

# Create users
u1 = User("Adarsh")
u2 = User("Aditi")

# User chooses which room to join
room_choice = input("Choose chat room (1-Python, 2-Java, 3-AI): ")

if room_choice == "1":
    u1.join_chatroom(python_room)
    u2.join_chatroom(python_room)

elif room_choice == "2":
    u1.join_chatroom(java_room)
    u2.join_chatroom(java_room)

elif room_choice == "3":
    u1.join_chatroom(ai_room)
    u2.join_chatroom(ai_room)

else:
    print("Invalid choice!")
    exit()

# Chat simulation
u1.send_message("Hello everyone!")
u2.send_message("Hi! How are you?")

# Show chat history
if u1.chatroom:
    u1.chatroom.show_history()'''
    
'''import datetime
import time

# ==========================================================
# Message Class
# ==========================================================
class Message:
    def __init__(self, sender, content, private_to=None):
        self.sender = sender
        self.content = content
        self.private_to = private_to
        self.timestamp = datetime.datetime.now().strftime("%H:%M:%S")

    def display(self):
        if self.private_to:
            return f"[{self.timestamp}] (Private) {self.sender.username} → {self.private_to.username}: {self.content}"
        return f"[{self.timestamp}] {self.sender.username}: {self.content}"


# ==========================================================
# User Class
# ==========================================================
class User:
    def __init__(self, username, is_admin=False):
        self.username = username
        self.is_admin = is_admin
        self.current_room = None
        self.online = False

    def join_room(self, room):
        if self.current_room:
            print(f"{self.username} left {self.current_room.name}")
            self.current_room.remove_user(self)

        self.current_room = room
        room.add_user(self)
        self.online = True
        print(f"{self.username} joined {room.name}")

    def leave_room(self):
        if self.current_room:
            print(f"{self.username} left {self.current_room.name}")
            self.current_room.remove_user(self)
            self.current_room = None
        self.online = False

    def send_message(self, content):
        if self.current_room:
            msg = Message(self, content)
            self.current_room.add_message(msg)
        else:
            print("You are not in any room!")

    def send_private(self, user, content):
        msg = Message(self, content, private_to=user)
        print(msg.display())  # private message only shown on console


# ==========================================================
# Chat Room Class
# ==========================================================
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def show_users(self):
        print("\n👥 Users in room", self.name)
        for u in self.users:
            print("•", u.username)

    def add_message(self, message):
        self.messages.append(message)
        print(message.display())

    def delete_message(self, index, admin_user):
        if admin_user.is_admin:
            if 0 <= index < len(self.messages):
                removed = self.messages.pop(index)
                print(f"🗑️ Admin removed message: {removed.display()}")
            else:
                print("Invalid message index!")
        else:
            print("Only admin can delete messages!")

    def chat_history(self):
        print(f"\n📜 Chat History of {self.name}")
        for msg in self.messages:
            print(msg.display())


# ==========================================================
# ==========================================================
if __name__ == "__main__":

    # Create rooms
    python_room = ChatRoom("Python Room")
    ml_room = ChatRoom("ML Room")

    # Create users
    admin = User("Sizzi", is_admin=True)
    adarsh = User("Adarsh")
    aditi = User("Aditi")

    # Join rooms
    admin.join_room(python_room)
    adarsh.join_room(python_room)
    aditi.join_room(ml_room)

    print("Adarsh is typing...")
    time.sleep(1)

    # Send messages
    admin.send_message("Welcome to the Python Room!")
    adarsh.send_message("Hello everyone!")
    admin.send_message("Let's start learning OOP.")

    # Private message example
    adarsh.send_private(admin, "Sir, can you explain classes again?")

    # aditi switches room
    aditi.join_room(python_room)
    aditi.send_message("Hi! I also want to learn Python.")

    # Show users
    python_room.show_users()

    # Delete a message (admin only)
    python_room.delete_message(1, admin)

    # Show full chat history
    python_room.chat_history()'''
    
    
import datetime
import time

# ==========================================================
# Message Class
# ==========================================================
class Message:
    def __init__(self, sender, content, private_to=None):
        self.sender = sender
        self.content = content
        self.private_to = private_to
        self.timestamp = datetime.datetime.now().strftime("%H:%M:%S")

    def display(self):
        if self.private_to:
            return f"[{self.timestamp}] (Private) {self.sender.username} → {self.private_to.username}: {self.content}"
        return f"[{self.timestamp}] {self.sender.username}: {self.content}"


# ==========================================================
# User Class
# ==========================================================
class User:
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.current_room = None
        self.online = False

    def join_room(self, room):
        if self.current_room:
            print(f"{self.username} left {self.current_room.name}")
            self.current_room.remove_user(self)

        self.current_room = room
        room.add_user(self)
        self.online = True
        print(f"{self.username} joined {room.name}")

    def leave_room(self):
        if self.current_room:
            print(f"{self.username} left {self.current_room.name}")
            self.current_room.remove_user(self)
            self.current_room = None
        self.online = False

    def send_message(self, content):
        if self.current_room:
            msg = Message(self, content)
            self.current_room.add_message(msg)
        else:
            print("You are not in any room!")

    def send_private(self, user, content):
        msg = Message(self, content, private_to=user)
        print(msg.display())

# ==========================================================
# Chat Room Class
# ==========================================================
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def show_users(self):
        print("\n👥 Users in room", self.name)
        for u in self.users:
            print("•", u.username)

    def add_message(self, message):
        self.messages.append(message)
        print(message.display())

    def delete_message(self, index, admin_user):
        if admin_user.is_admin:
            if 0 <= index < len(self.messages):
                removed = self.messages.pop(index)
                print(f"🗑️ Admin removed message: {removed.display()}")
            else:
                print("Invalid message index!")
        else:
            print("Only admin can delete messages!")

    def chat_history(self):
        print(f"\n📜 Chat History of {self.name}")
        for msg in self.messages:
            print(msg.display())


# ==========================================================
# LOGIN SYSTEM
# ==========================================================
def login(users):
    print("===== LOGIN REQUIRED =====")
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        for user in users:
            if user.username == username and user.password == password:
                print(f"\n✔ Login Successful! Welcome {username}\n")
                return user

        print("❌ Invalid username or password. Try again!\n")

# ==========================================================
# MAIN PROGRAM
# ==========================================================
if __name__ == "__main__":

    # Create chat rooms
    python_room = ChatRoom("Python Room")
    java_room = ChatRoom("Java Room")

    # Create users
    users = [
        User("Sizzi", "admin123", is_admin=True),
        User("Adarsh", "1234"),
        User("Aditi", "9999")
    ]

    # LOGIN FIRST
    current_user = login(users)

    # After login → Menu system
    while True:
        print("\n===== MENU =====")
        print("1. Join Python Room")
        print("2. Join Java Room")
        print("3. Send Message")
        print("4. View Chat History")
        print("5. View Users in Room")
        print("6. Private Message")
        print("7. Leave Room")
        print("8. Exit Program")

        choice = input("Choose option: ")

        if choice == "1":
            current_user.join_room(python_room)

        elif choice == "2":
            current_user.join_room(java_room)

        elif choice == "3":
            msg = input("Type message: ")
            current_user.send_message(msg)

        elif choice == "4":
            if current_user.current_room:
                current_user.current_room.chat_history()
            else:
                print("You are not in any room.")

        elif choice == "5":
            if current_user.current_room:
                current_user.current_room.show_users()
            else:
                print("You are not in any room.")

        elif choice == "6":
            name = input("Send to (username): ")
            message = input("Message: ")

            receiver = None
            for u in users:
                if u.username == name:
                    receiver = u
                    break
            
            if receiver:
                current_user.send_private(receiver, message)
            else:
                print("User not found!")

        elif choice == "7":
            current_user.leave_room()

        elif choice == "8":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice!")


