import { CreateTodo } from "@/components/manage/buttons";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import Link from "next/link";

const page = () => {
  return (
    <div className=" min-h-[75%] rounded-sm h-full flex flex-col items-center justify-center bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-sky-400 to-blue-800">
      <div className="space-y-6 text-center">
        <h1 className={cn(
          "text-3xl lg:text-5xl font-semibold text-white drop-shadow-md"
        )}>
          🔐 ToDo Buddy 
        </h1>
        <p className="text-white text-lg">
          GUI to manage todos with or Chat with Todo Buddy
        </p>
        <div className="flex flex-col justify-center items-center space-y-5">
            <Link href="https://chat.openai.com/g/g-LsLmvsnKo-todo-buddy" target="_blank">
            <Button variant="secondary" size="lg">
              Chat with Todo Buddy 🤖
            </Button>
            </Link>
            <Link href="/dashboard/manage">
            <Button variant="secondary" size="lg">
              View and Mange Todos 📝
            </Button>
            </Link>
            <CreateTodo /> 
        </div>
      </div>
     
    </div>
  );
};

export default page;
