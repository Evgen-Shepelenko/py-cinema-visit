from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str | Cleaner,
        movie: str
) -> None:
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer, customer.food)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customers, cleaner)
