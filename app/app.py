from typing import Optional

from flask import Flask, request, jsonify

from prisma import Client  # Import Prisma Client


# Initialize Prisma Client with connection string from environment variable
prisma = Client(env("DATABASE_URL"))

app = Flask(__name__)

@app.route("/expenses", methods=["POST"])
def add_expense():
  data = request.get_json()
  
  # Extract expense details from request data
  category = data.get("category")
  amount = data.get("amount")
  date = data.get("date")
  description = data.get("description", None)
  
  # Create a new expense using Prisma Client
  new_expense = prisma.expense.create(
      data={
          "category": category,
          "amount": amount,
          "date": date,
          "description": description,
      }
  )
  
  # Convert Prisma object to a dictionary
  expense_dict = new_expense.dict()
  
  return jsonify(expense_dict), 201

if __name__ == "__main__":
  app.run(debug=True)
