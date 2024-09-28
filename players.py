from random import randint
from utils import Player


default_50_characters = [ Player("Mechanic", 48000, 650, 0),
                        Player("Nurse", 80000, 630, 20000),
                        Player("High School Teacher", 63000, 570, 30000),
                        Player("Accountant", 77000, 820, 45000),
                        Player("IT Support Specialist", 55000, 510, 20000),
                        Player("Grocery Stocker", 25000, 660, 0),
                        Player("Paramedic/EMT", 40000, 710, 5000),
                        Player("Electrician", 60000, 430, 0),
                        Player("School Councelor", 60000, 570, 30000),
                        Player("Insurance Agent", 73000, 410, 0),
                        Player("Doctor", 200000, 480, 250000),
                        Player("Software Developer", 120000, 610, 20000),
                        Player("Barista", 33000, 540, 0),
                        Player("Librarian", 60000, 820, 35000),
                        Player("Welder", 51000, 710, 0),
                        Player("Human Resources Specialist", 65000, 680, 25000),
                        Player("Pharmacist", 13000, 410, 160000),
                        Player("Cybersecurity Analyst", 105000, 570, 20000),
                        Player("Cashier", 22000, 680, 0),
                        Player("Academic Advisor", 52000, 730, 15000),
                        Player("Truck Driver", 50000, 680, 0),
                        Player("Management Consultant", 125000, 580, 55000),
                        Player("Radiological Technologist", 68000, 710, 15000),
                        Player("Web Developer", 79000, 620, 15000),
                        Player("Construction General Laborer", 35000, 470, 0),
                        Player("Substitute Teacher", 38000, 730, 10000),
                        Player("HVAC technician", 55000, 590, 0),
                        Player("Real Estate Agent", 72000, 830, 0),
                        Player("Physical Therapist", 90000, 510, 85000),
                        Player("Cloud Architect", 150000, 470, 35000),
                        Player("Waiter", 28000, 610, 0),
                        Player("College Professor", 95000, 540, 40000),
                        Player("Carpenter", 50000, 680, 0),
                        Player("Marketing Manager", 140000, 710, 25000),
                        Player("Occupational Therapist", 85000, 530, 70000),
                        Player("Mechanical Engineer", 82000, 740, 20000),
                        Player("Retail Service Representative", 31000, 580, 0),
                        Player("Special Education Teacher", 48000, 710, 35000),
                        Player("Landscaper", 35000, 820, 0),
                        Player("Business Analyst", 85000, 730, 30000),
                        Player("Medical Assistant", 38000, 650, 5000),
                        Player("Electronics Engineer", 98000, 560, 20000),
                        Player("Social Worker", 42000, 610, 35000),
                        Player("School Principal", 105000, 740, 45000),
                        Player("Welder", 62000, 540, 0),
                        Player("Construction Project Manager", 85000, 780, 15000),
                        Player("Dentist", 180000, 650, 250000),
                        Player("Civil Engineer", 78000, 590, 20000),
                        Player("Fast Food Cook", 27000, 670, 0),
                        Player("Network Administrator", 80000, 780, 20000)
]

def create_playerbase(given_number_of_players):
    playerbase = []
    start_index = randint(0, 49)
    for idx in range(given_number_of_players):
        playerbase.append(default_50_characters[(start_index + idx) % 50])
    return playerbase
    