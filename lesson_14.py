# p = open("C:/Users/Taras/Desktop/VS Code/Python/file_1.txt", "w")
# p.write("HELLO")
# p.close()


# n1 = int(input("Please enter a number:  "))
# n2 = int(input("Please enter a number:  "))
# p = open("C:/Users/Taras/Desktop/VS Code/Python/file_2.txt", "w")
# for x in range(n1, n2 + 1):
#     p.write(str(x) + "\n")
# p.close()




tasks = []
while True:
    des = input("Write 1 for create, 2 for delete 3 to see all, 4 to exit:  ")

    if des == "1":
        task = input("Write your task:  ")
        tasks.append(task)

    elif des == "2":
        if len(tasks) == 0:
            print("There is no tasks.")
        else:
            print(tasks)
            delete_task = input("Enter a task number to delete:  ")
            tasks.pop(int(delete_task))
            print("Task deleted")

    elif des == "3":
        if len(tasks) == 0:
            print("There is no tasks.")
        else:
            task_number = 1
            for task in tasks:
                print(task_number, task)
                task_number = task_number + 1
                
    elif des == "4":
        print("Goodbye!")
        break
