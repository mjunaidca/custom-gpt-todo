'use server'
import { revalidateTag } from 'next/cache'

export async function deleteTodo(id: string) {
    try {
        const all_todos_request = await fetch(`${process.env.BACKEND_URL}/api/todos/${id}`, {
            method: 'DELETE',
            cache: 'no-store',
            next: { tags: ['get_todos'] }
        });

        console.log('DELETE_TODO_STATUS', all_todos_request.status, all_todos_request.statusText);
        

        if (all_todos_request.status === 200) {
            revalidateTag('get_todos')
            return { message: 'Deleted Todo' };
        } 

        return { message: 'Failed to Delete Todo' };

    } catch (error) {
      return { message: 'Database Error: Failed to Delete Invoice.' };
    }
  }