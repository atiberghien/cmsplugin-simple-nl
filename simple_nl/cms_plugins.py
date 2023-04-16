#-*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models import CMSPlugin

@plugin_pool.register_plugin  # register the plugin
class SimpleNLSubscriberPlugin(CMSPluginBase):
    model = CMSPlugin
    module = "Newsletter"
    name = "Formulaire d'inscription"
    render_template = "simple_nl/subscription_form.html"
