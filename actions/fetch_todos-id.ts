export async function fetchTodoById(id: string) {

    const todo_request = await fetch(`${process.env.BACKEND_URL}/api/todos/${id}`, {
        headers: {
            "Content-Type": "application/json",
        },
        cache: 'no-store'
    });

    console.log('FETCH_TODO_STATUS', todo_request.status, todo_request.statusText);

    if (!todo_request.ok) {
        return { error: 'Failed to load todo', status: todo_request.status };
    }

    const todo: TodoItem = await todo_request.json();
    return todo;

}
