from rest_framework.routers import DefaultRouter
from api.v1.views import (
    PostViewSet, UpvoteViewSet, DownvoteViewSet,
    PinnedPostViewSet, TagViewSet, CollectionViewSet,
    DownvoteCollectionViewSet, UpvoteCollectionViewSet
)

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'upvotes-post', UpvoteViewSet, basename='upvotes-post')
router.register(r'downvotes-post', DownvoteViewSet, basename='downvotes-post')
router.register(r'pinnedposts', PinnedPostViewSet, basename='pinnedposts')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'collections', CollectionViewSet, basename='collections')
router.register(r'upvotes-collection', UpvoteCollectionViewSet,
                basename='upvotes-collection')
router.register(r'downvotes-collection', DownvoteCollectionViewSet,
                basename='downvotes-collection')


urlpatterns = router.urls
