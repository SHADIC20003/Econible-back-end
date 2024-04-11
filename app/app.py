from typing import Optional
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from prisma import Client  # Import Prisma Client
# -------------------------------------------------------#
#                       TO DO:                           #
# 1 - Connect User acc from database                     #
# 2 - Write login and signup code                        # 
# 3 - Handle verification and authentication             # 
# 4 - Test it                                            # 
# -------------------------------------------------------# 



# Initialize Prisma Client with connection string from environment variable
prisma = Client("postgresql://Econibledb_owner:bKvV3s9MUhHj@ep-twilight-mode-a2ossjfb-pooler.eu-central-1.aws.neon.tech/Econibledb?sslmode=require")

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
