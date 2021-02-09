# The implementation should not matter!

def make_review(place, rating):
    return [place, rating]

def get_place(review):
    return review[0]

def get_rating(review):
    return review[1]

# Some reviews found from Google.
google_reviews = [
    make_review('Canyon Vista', 1),
    make_review('Canyon Vista', 3),
    make_review('Canyon Vista', 4),
    make_review('Canyon Vista', 1),
    make_review('Canyon Vista', 2),
    make_review('Foodworx', 3),
    make_review('Foodworx', 5),
    make_review('Foodworx', 1),
    make_review('Foodworx', 5),
    make_review('Foodworx', 3),
    make_review('Pines', 3),
    make_review('Pines', 2),
    make_review('Pines', 4),
    make_review('Pines', 5),
    make_review('Pines', 4),
    make_review('64 Degrees', 4),
    make_review('64 Degrees', 5),
    make_review('64 Degrees', 4),
    make_review('64 Degrees', 3),
    make_review('64 Degrees', 5),
    make_review('OVT', 5),
    make_review('OVT', 4),
    make_review('OVT', 2),
    make_review('OVT', 5),
    make_review('OVT', 4),
    make_review('Cafe Ventanas', 4),
    make_review('Cafe Ventanas', 1),
    make_review('Cafe Ventanas', 5),
    make_review('Cafe Ventanas', 3),
    make_review('Cafe Ventanas', 4)
]