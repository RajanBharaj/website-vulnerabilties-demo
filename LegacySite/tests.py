import os
import json
from django.test import TestCase, Client
from LegacySite.models import Card

dirname = os.path.dirname(os.path.abspath(__file__))

# Create your tests here.
class MyTest(TestCase):
    # Django's test run with an empty database. We can populate it with
    # data by using a fixture. You can create the fixture by running:
    #    mkdir LegacySite/fixtures
    #    python manage.py dumpdata LegacySite > LegacySite/fixtures/testdata.json
    # You can read more about fixtures here:
    #    https://docs.djangoproject.com/en/4.0/topics/testing/tools/#fixture-loading
    fixtures = ["testdata.json"]

    def setUp(self):
        self.client = Client()

    # Assuming that your database had at least one Card in it, this
    # test should pass.
    def test_get_card(self):
        allcards = Card.objects.all()
        self.assertNotEqual(len(allcards), 0)
        print("Test get card: ", allcards, end="\n\n")

    #success if redirect 302 to "/login.html"
    def test_buy_anon(self):
        response = self.client.post('/buy.html')
        self.assertEqual(response.status_code, 302)
        print("Test anon buy: ", response.has_header, end="\n\n")

    #success if HTTP 200 and no redirect to "/index.html"
    def test_register_existing(self):
        response = self.client.post('/register.html', {"uname": "attacker@good.edu", "pword": "secure123", "pword2": "secure123"})
        self.assertEqual(response.status_code, 200)
        print("Test register existing: ", response.has_header, end="\n\n")

    #success if 'director_content != <script>alert("The director says hello.")</script>
    def test_xss(self):
        response = self.client.get('/buy.html?director=<script>alert("The director says hello.")</script>')
        self.assertEqual(response.status_code, 200)
        content = response.content
        pos = content.find(b'director')
        director_content = content[pos-45:pos+50]
        print("XSS test-> ", director_content, end="\n\n")
    
    #success if recipient = None
    def test_csrf(self):
        self.client.login(username="victim@bad.edu", password="hello123")
        response = self.client.get('/gift/6?username=attacker@good.edu')
        self.assertEqual(response.status_code, 200)
        recipient = response.context["user"]
        print("CSRF test-> Giftcard recieved by: ", recipient, end="\n\n")

    #success "No cards found"
    def test_sqli(self):
        self.client.login(username="attacker@good.edu", password="secure123")
        filename = os.path.join(dirname, '../part1/sql_all_pass.gftcrd')
        with open(filename, "rb") as fp:
            print("SQL giftcard test: ", end="")
            response = self.client.post("/use.html", {"card_data": fp, "card_supplied": True, "card_fname": "NameYourCard"})
            self.assertEqual(response.status_code, 200)
            print("\n\n")

    #success if card binary printed and filename! = exectuable comand
    def test_os_ci(self):
        self.client.login(username="attacker@good.edu", password="secure123")
        filename = os.path.join(dirname, '../part1/command_injection.gftcrd')
        fname = "something & command injection success &"
        with open(filename, "rb") as fp:
            print("Command injection giftcard test-> filename = '", fname, "': ", end="")
            response = self.client.post("/use.html", {"card_data": fp, "card_supplied": True, "card_fname": fname})
            self.assertEqual(response.status_code, 200)
            print("\n\n")
