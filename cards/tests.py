from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate,APITestCase, URLPatternsTestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.urls import reverse
from wallet.models import Wallet
import json


class CardViewTestCase(APITestCase):
    fixtures =['wallet/fixtures/users.json','wallet/fixtures/wallets.json','cards/fixtures/cards.json']

    def setUp(self):
        response = self.client.post("/api/auth/", {'username':"test", 'password':'test123'},format="json" )
        self.token = response.data['token']
        self.user_id = response.data['user_id']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        self.wallet = self.client.get("/api/me/wallets/",format="json" )

    #Test create a card
    def test_create_card(self):
        cards = self.client.post("/api/cards/", {'title':"Test Card",'description':'test', 'value':100, 'voucher':1233,'pin':123,'wallet_id': self.wallet.data[0]['id']},format="json" )
        self.assertEqual(cards.status_code, status.HTTP_201_CREATED)
        self.assertTrue(len(cards.data)>0) 
        
    #Test get a cards
    def test_get_a_card(self):
        card = self.client.get("/api/cards/5/",format="json" )
        self.assertEqual(card.status_code, status.HTTP_200_OK)
        self.assertTrue(len(card.data)>0)
        
    #Test get my cards
    def test_get_my_cards(self):
        cards = self.client.get("/api/cards/",format="json" )
        self.assertEqual(cards.status_code, status.HTTP_200_OK)
        self.assertTrue(len(cards.data)>0)