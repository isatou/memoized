from rest_framework.routers import DefaultRouter
from api.v1.views import (
    PostViewSet, UpvoteViewSet, DownvoteViewSet,
    PinnedPostViewSet, TagViewSet, CollectionViewSet
)

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'upvotes', UpvoteViewSet, basename='upvotes')
router.register(r'downvotes', DownvoteViewSet, basename='downvotes')
router.register(r'pinnedposts', PinnedPostViewSet, basename='pinnedposts')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'collections', CollectionViewSet, basename='collections')


urlpatterns = router.urls