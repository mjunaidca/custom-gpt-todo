"use server";
import { redirect } from "next/navigation";
import { revalidateTag } from "next/cache";
import * as z from "zod";
import { TodoSchema } from "@/schemas/todo";

export async function createTodoAction(values: z.infer<typeof TodoSchema>) {
  const validatedFields = TodoSchema.safeParse(values);

  if (!validatedFields.success) {
    return { error: "Invalid fields!" };
  }

  const { title, completed, description } = validatedFields.data;

  console.log("updateTodoAction", title, completed, description);

  // Get All Todos
  const update_todo = await fetch(`${process.env.BACKEND_URL}/api/todos`, {
    headers: {
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify({
      title: title,
      description: description,
      completed: completed,
    }),
    cache: "no-store",
    next: { tags: ["get_todos"] },
  });

  console.log("UPDATE_TODO_STATUS", update_todo.status, update_todo.statusText);

  if (update_todo.status === 200) {
    revalidateTag("get_todos");
    redirect("/dashboard/manage");
  }

  return { message: "Failed to Create Todo" };
}
