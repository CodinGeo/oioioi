from django.conf.urls import patterns, include, url

forum_patterns = patterns('oioioi.forum.views',
    url(r'^$', 'forum_view',
        name='forum'),
    url(r'^lock/$',
        'lock_forum_view', name='forum_lock'),
    url(r'^unlock/$',
        'unlock_forum_view', name='forum_unlock'),
    url(r'^(?P<category_id>\d+)/$',
        'category_view', name='forum_category'),
    url(r'^(?P<category_id>\d+)/delete/$',
        'delete_category_view', name='forum_category_delete'),
    url(r'^(?P<category_id>\d+)/(?P<thread_id>\d+)/$',
        'thread_view', name='forum_thread'),
    url(r'^(?P<category_id>\d+)/(?P<thread_id>\d+)/delete/$',
        'delete_thread_view', name='forum_thread_delete'),
    url(r'^(?P<category_id>\d+)/add_thread/$',
        'thread_add_view', name='forum_add_thread'),
    url(r'^(?P<category_id>\d+)/(?P<thread_id>\d+)/(?P<post_id>\d+)/edit/$',
        'edit_post_view', name='forum_post_edit'),
    url(r'^(?P<category_id>\d+)/(?P<thread_id>\d+)/(?P<post_id>\d+)/delete/$',
        'delete_post_view', name='forum_post_delete'),
    url(r'^(?P<category_id>\d+)/(?P<thread_id>\d+)/(?P<post_id>\d+)/report/$',
        'report_post_view', name='forum_post_report'),
    url(r'^(?P<category_id>\d+)/(?P<thread_id>\d+)/(?P<post_id>\d+)/hide/$',
        'hide_post_view', name='forum_post_hide'),
    url(r'^(?P<category_id>\d+)/(?P<thread_id>\d+)/(?P<post_id>\d+)/$',
        'show_post_view', name='forum_post_show'),
)
urlpatterns = patterns('oioioi.forum.views',
    url(r'^c/(?P<contest_id>[a-z0-9_-]+)/forum/', include(forum_patterns)),
)