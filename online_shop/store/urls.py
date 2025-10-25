from django.urls import include, path
from rest_framework import routers
from .views import (UserProfileViewSet, ProductImageViewSet, ReviewViewSet, RegisterView,
                    LogoutView, CategoryListViewSet, CategoryDetailView, ProductDetailView, ProductListAPIVView,
                    SubCategoryDetailView,
                    SubCategoryListViewSet, CustomLoginView, CartViewSet, CartItemViewSet, )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'images', ProductImageViewSet, basename='images')
router.register(r'reviews', ReviewViewSet, basename='reviews')





urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login_list'),
    path('logout/', LogoutView.as_view(), name='logout_list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
    path('category/', CategoryListViewSet.as_view(), name='category'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('sub_category/', SubCategoryListViewSet.as_view(), name='sub-category_list'),
    path('sub_category/<int:pk>/', SubCategoryDetailView.as_view(), name='sub-category-detail'),
    path('product/', ProductListAPIVView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartViewSet.as_view(), name='cart_detail'),
    path('cart_items/', CartItemViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('cart_items/<int:pk>/', CartItemViewSet.as_view({'put': 'update', 'delete': 'destroy'})),

]