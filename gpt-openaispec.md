openapi: 3.1.0
info:
  title: FastAPI Backend
  description: This is a backend application built with FastAPI.
  version: 0.1.0
servers:
  - url: https://cax-gpt-todo.vercel.app
    description: Production server
paths:
  /api/todos:
    get:
      summary: Get Todos
      operationId: getTodos
      responses:
        "200":
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/TODOResponse"
    post:
      summary: Create Todo
      operationId: createTodo
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/TODOBase"
      responses:
        "200":
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/TODOResponse"
        "422":
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/HTTPValidationError"
  /api/todos/{todo_id}:
    get:
      summary: Get Todo By Id
      operationId: getTodoById
      parameters:
        - name: todo_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        "200":
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/TODOResponse"
        "422":
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/HTTPValidationError"
    put:
      summary: Update Todo
      operationId: updateTodo
      parameters:
        - name: todo_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/TODOBase"
      responses:
        "200":
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/TODOResponse"
        "422":
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/HTTPValidationError"
    patch:
      summary: Update Todo Partial
      operationId: updateTodoPartial
      parameters:
        - name: todo_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/TODOBase"
      responses:
        "200":
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/TODOResponse"
        "422":
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/HTTPValidationError"
    delete:
      summary: Delete Todo
      operationId: deleteTodo
      parameters:
        - name: todo_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        "200":
          description: Successful Response
          content:
            application/json:
              schema: {}
        "422":
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/HTTPValidationError"
components:
  schemas:
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: "#/components/schemas/ValidationError"
      title: HTTPValidationError
    TODOBase:
      type: object
      properties:
        title:
          type: string
        description:
          oneOf:
            - type: string
            - type: null
        completed:
          type: boolean
          default: false
      required:
        - title
      title: TODOBase
      description: Represents a TODO in the database.
    TODOResponse:
      type: object
      properties:
        title:
          type: string
        description:
          oneOf:
            - type: string
            - type: null
        completed:
          type: boolean
          default: false
        id:
          type: string
          format: uuid
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
      required:
        - title
        - id
        - created_at
        - updated_at
      title: TODOResponse
      description: Represents a TODO item to be returned.
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            oneOf:
              - type: string
              - type: integer
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
