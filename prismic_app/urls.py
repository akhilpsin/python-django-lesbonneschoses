from django.conf.urls import patterns, url

from prismic_app import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about', views.about, name='about'),
                       url(r'^products/(?P<id>[-_a-zA-Z0-9]{16})/(?P<slug>.*)', views.product, name='product'),
                       url(r'^products/', views.products, name='products'),
                       url(r'^products/by-flavour', views.products_by_flavour),
                       url(r'^jobs/(?P<id>[-_a-zA-Z0-9]{16})/(?P<slug>.*)', views.job, name='job'),
                       url(r'^jobs/', views.jobs, name='jobs'),
                       url(r'^stores/(?P<id>[-_a-zA-Z0-9]{16})/(?P<slug>.*)', views.store, name='store'),
                       url(r'^stores/', views.stores, name='stores'),
                       url(r'^blog', views.stores, name='blog')
                       )

