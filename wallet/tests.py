from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate,APITestCase, URLPatternsTestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.urls import reverse
from wallet.models import Wallet
import json


class ViewTestCase(APITestCase):
    fixtures =['wallet/fixtures/users.json','wallet/fixtures/wallets.json','cards/fixtures/cards.json']
    def setUp(self):
        response = self.client.post("/api/auth/", {'username':"test", 'password':'test123'},format="json" )
        self.token = response.data['token']
        self.user_id = response.data['user_id']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        

    #Test Create User and Wallet  
    def test_create_user_wallet(self):
        user = self.client.post("/api/user/register/", {'username':"testuser", 'password':'test123', 'email':"test@test.com"},format="json" )
        self.assertEqual(user.status_code, status.HTTP_201_CREATED)

    #Test get me
    def test_get_me(self):
        me = self.client.get("/api/me/",format="json" )
        self.assertEqual(me.status_code, status.HTTP_200_OK)
        self.assertEqual(me.data[0]['id'], self.user_id)

    #Test get my wallet
    def test_get_my_wallet(self):
        wallet = self.client.get("/api/me/wallets/",format="json" )
        self.assertEqual(wallet.status_code, status.HTTP_200_OK)
        self.assertEqual(wallet.data[0]['owner'], self.user_id)
        self.assertTrue(len(wallet.data)>0)
    
    #Test get my cards
    def test_get_my_cards(self):
        cards = self.client.get("/api/me/cards/",format="json" )
        self.assertEqual(cards.status_code, status.HTTP_200_OK)
        self.assertTrue(len(cards.data)>0)