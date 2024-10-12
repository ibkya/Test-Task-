from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from .models import TimeSlot

class ScheduleAPITestCase(APITestCase):
    
    def setUp(self):
        # Kullanıcı oluşturma
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.timeslot_data = {
            "day_of_week": "monday",
            "start_time": "09:00:00",
            "stop_time": "10:00:00",
            "ids": [1, 2]
        }
        
        # JWT token alma
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        
        # Authorization başlığı ile işlem yapabilmek için
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_timeslot(self):
        # POST isteği ile yeni bir TimeSlot oluşturma
        url = reverse('timeslot-list')  # urls.py'de ViewSet ile oluşturduğumuz path
        response = self.client.post(url, self.timeslot_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_timeslot_list(self):
        # Zaman aralığı oluşturma
        TimeSlot.objects.create(**self.timeslot_data)
        
        # GET isteği ile TimeSlot listesini alma
        url = reverse('timeslot-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)
    
    def test_update_timeslot(self):
        # Zaman aralığı oluşturma
        timeslot = TimeSlot.objects.create(**self.timeslot_data)
        updated_data = {
            "day_of_week": "monday",
            "start_time": "10:00:00",
            "stop_time": "11:00:00",
            "ids": [3, 4]
        }
        
        # PUT isteği ile TimeSlot güncelleme
        url = reverse('timeslot-detail', args=[timeslot.id])
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_timeslot(self):
        # Zaman aralığı oluşturma
        timeslot = TimeSlot.objects.create(**self.timeslot_data)
        
        # DELETE isteği ile TimeSlot silme
        url = reverse('timeslot-detail', args=[timeslot.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_jwt_authentication(self):
        # JWT authentication testi, başarılı token ile giriş kontrolü
        url = reverse('timeslot-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Başarısız token denemesi
        self.client.credentials()  # Token başlığını kaldırma
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
