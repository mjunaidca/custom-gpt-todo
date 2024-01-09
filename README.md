# TODO Buddy: A Custom GPT Synced with NextJS14 Web App

### Chat with Todo Buddy and review the update on NextJS Web App.

- This Custom GPT can view all todos, add new tasks to list, update and delete them. 
- User can manage todos themselves with nextjs14 web app.

Remember currently it is build for a single user and can easily extended to multi user web app.

### A. Web Interface

https://cax-gpt-todo.vercel.app/dashboard/manage

FastAPI Microservice and NextJS web app are deployed on vercel:

### B. Todo Buddy (Custom GPT Conversational Interface)

https://chat.openai.com/g/g-LsLmvsnKo-todo-buddy

## Guide to Develop Custom GPT and Deploy NextJS14 Project on Vercel

#### 1. Clone the project

```
https://github.com/mjunaidca/custom-gpt-todo.git
```

 Run pnpm install to install the missing dependencies

#### 2. Add Environment Variables

Rename .env.template to .env and add environment variables. 
1. For `DB` we are using SQL ALchemy ORM so you can add any database url. I will recommend 
vercel postgress or neon serverless postgress database. 
2. For 2nd during local testing and http://localhost:3000 and in production add vercel deplyment url.

#### 3. Run Database Migrations

In terminal run:

- `alembic revision --autogenerate -m "Add Todos Table`

- `alembic upgrade head`

#### 4. Run Project Locally

Run pnpm install to install the missing dependencies

#### 5. Vercel Deplyment

Delete the .next and __pucache__ and .mypy... cache files and follow the steps:

a. Run `vercel link` and then add all env variables to vercel deplyment. Replace the localhost vars with vercel deoloyment link

b. Finally run `vercel --prod` to deploy the project.

#### 6. Build Custom GPT

1. Got to chat.openai.com open GPT builder
2. Use GPT builder to add your gpt basic settings (name picture etc.)
3. Click on Create Action and in Open AI schema copy gpt-openaispec.json and add it there. 
4. Test and Save it.

#### Some Helpful Tools FOr Building GPTs:
https://editor-next.swagger.io/
https://chat.openai.com/g/g-TYEliDU6A-actionsgpt

## Thoughts

Feel free to ask any questions or provide feedback. Contributions are also welcome!
