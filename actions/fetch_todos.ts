
import { redirect } from 'next/navigation';

export async function fetchAllTodos() {


    // Get All Todos
    const all_todos_request = await fetch(`${process.env.BACKEND_URL}/api/todos`, {
        cache: 'no-store',
        next: { tags: ['get_todos'] }
    });

    if (!all_todos_request.ok) {
        return 'Failes to Load Todos'
    }

    console.log(all_todos_request.status);
    

    const all_todos: TodoList = await all_todos_request.json();

    return all_todos;
}