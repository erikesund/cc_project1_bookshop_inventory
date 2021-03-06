from flask import Flask, render_template, Blueprint, redirect, request
from controllers.ordered_book_controller import ordered_books

from models.order import Order

import repositories.order_repository as order_repository

orders_blueprint = Blueprint("orders", __name__)

@orders_blueprint.route("/orders")
def orders():
  orders = order_repository.select_all()
  return render_template("orders/index.html", orders = orders)

@orders_blueprint.route("/orders/<id>")
def show_order(id):
  ordered_books = order_repository.select_books_in_order(id)
  order = order_repository.select(id)
  return render_template("/orders/show.html", order = order, ordered_books = ordered_books)

@orders_blueprint.route("/orders/<id>/delete", methods = ["POST"])
def delete_order(id):
  order_repository.delete(id)
  return redirect("/orders")