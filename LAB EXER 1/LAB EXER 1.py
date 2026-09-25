tickets = [
    ["INC1392939", "BOT-Inventory", "Failed to generate the daily report"],
    ["INC1392940", "BOT-Email", "Failed to send the scheduled notification"],
    ["INC1392941", "BOT-DataSync", "Encountered an error during data transfer"],
    ["INC1392942", "BOT-Invoice", "Failed to process an invoice"],
    ["INC1392943", "BOT-Report", "Failed to generate the weekly report"],
    ["INC1392944", "BOT-FileTransfer", "Failed to upload the required file"],
    ["INC1392945", "BOT-DataEntry", "Encountered an error while entering records"],
    ["INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"],
    ["INC1392947", "BOT-Validation", "Failed to validate the submitted records"],
    ["INC1392948", "BOT-Notification", "Failed to send the system alert"],
]

while True:
    print("\n1. Add  \n2. Display  \n3. Search  \n4. Remove  \n5. Count  \n6. Exit")
    choice = input("Choice: ")

    if choice == "1":
        tickets.append([input("Incident ID: "), input("Bot: "), input("Description: ")])
        print('Ticket added.')
    elif choice == "2":
        for t in tickets:
            print(t[0], "|", t[1], "|", t[2])
    elif choice == "3":
        id = input("Incident ID: ")
        for t in tickets:
            if t[0] == id:
                print("Found:", t[0], "|", t[1], "|", t[2])
                break
        else:
            print("Not found.")
    elif choice == "4":
        id = input("Incident ID to remove: ")
        for i in range(len(tickets)):
            if tickets[i][0] == id:
                tickets.pop(i)
                print("Removed.")
                break
        else:
            print("Not found.")
    elif choice == "5":
        print("Active tickets:", len(tickets))
    elif choice == "6":
        print("Program terminated.")
        break