from collections import deque


class Client:
    def __init__(self, name, book):
        self.name = name
        self.book = book


class BookstoreQueue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, client):
        self.queue.append(client)
        print(f"{client.name} has been added to the queue.")

    def dequeue(self):
        if not self.is_empty():
            client = self.queue.popleft()
            print(f"{client.name} has been served and bought the book '{client.book}'.")
            return client
        else:
            print("The queue is empty, no clients to serve.")
            return None

    def size(self):
        return len(self.queue)


def main():
    bookstore_queue = BookstoreQueue()
    print("Welcome to the Bookstore Queue System!")

    while True:
        print("\nOptions:")
        print("1. Add client to queue")
        print("2. Serve client")
        print("3. Check queue size")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter client's name: ")
            book = input("Enter the book title: ")
            client = Client(name, book)
            bookstore_queue.enqueue(client)
        elif choice == "2":
            bookstore_queue.dequeue()
        elif choice == "3":
            print(f"The queue size is: {bookstore_queue.size()}")
        elif choice == "4":
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
