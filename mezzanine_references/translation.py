__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '08/12/16'
from modeltranslation.translator import translator, TranslationOptions
from .models import References


class ReferencesEvent(TranslationOptions):
    fields = ()


translator.register(References, ReferencesEvent)
