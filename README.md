## Overview
This Python script simulates a bookstore queue system using the `deque` collection from Python's `collections` module. Clients can join the queue, be served, and check the queue size interactively.

## Features
- **Client Class**: Represents a client in the bookstore queue with the following attributes:
  - `name`: The name of the client.
  - `book`: The title of the book the client intends to purchase.
- **BookstoreQueue Class**: Manages the queue of clients with the following methods:
  - `is_empty`: Checks if the queue is empty.
  - `enqueue`: Adds a client to the queue.
  - `dequeue`: Serves and removes the client at the front of the queue.
  - `size`: Returns the number of clients in the queue.

## How It Works
1. **Input**: The user can choose from options to add clients to the queue, serve clients, check the queue size, or exit the program.
2. **Processing**: Clients are added to or removed from the queue based on user input.
3. **Output**: Feedback is provided for each action, such as the addition of a client or serving a client.

## Usage
### Prerequisites
- Python 3.x

### Steps to Run
1. Save the script in a file, e.g., `bookstore_queue.py`.
2. Open a terminal or command prompt.
3. Run the script using the command:
   ```
   python bookstore_queue.py
   ```
4. Follow the interactive prompts to manage the queue.

### Example Interaction
**Sample Input:**
```
1. Add client to queue
2. Serve client
3. Check queue size
4. Exit

Enter your choice (1-4): 1
Enter client's name: Alice
Enter the book title: Python Programming
```

**Sample Output:**
```
Alice has been added to the queue.

Options:
1. Add client to queue
2. Serve client
3. Check queue size
4. Exit

Enter your choice (1-4): 2
Alice has been served and bought the book 'Python Programming'.
```

## Code Structure
### Client Class
- Represents a client with a name and book title.

### BookstoreQueue Class
- Manages the queue using a `deque` object.

### `main` Function
- Provides an interactive menu for the user to manage the bookstore queue.

## Customization
- The script can be extended to include additional features, such as viewing all clients currently in the queue or saving queue data to a file.
- Input validation can be enhanced to handle unexpected or incorrect inputs.

## License
This script is provided "as-is" for educational purposes. Feel free to modify and use it in your projects.

