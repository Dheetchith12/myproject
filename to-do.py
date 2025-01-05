todo = []
print("Add new tasks : 1\nShow tasks : 2\nDelete task :3\nExit :0")

while True:
    user_selection = int(input("Select the one :"))
    if user_selection == 1:
        task = input("Enter tasks :")
        todo.append(task)
    
    elif user_selection ==2:
        print(todo)
    elif user_selection == 3:
        if todo == []:
            task = input("Enter task :")
            todo.append(todo)
        else:
            todo.pop() 
            print(todo)
    else:
        break