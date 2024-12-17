from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CookieJWTAuthentication(JWTAuthentication):
    def get_validated_token(self, raw_token):
        # Переопределяем метод для получения токена
        return super().get_validated_token(raw_token)

    def authenticate(self, request):
        # Извлекаем токен из куков
        raw_token = request.COOKIES.get('access')
        if raw_token is None:
            return None  # Если токен не найден, возвращаем None

        # Проверяем и валидируем токен
        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token