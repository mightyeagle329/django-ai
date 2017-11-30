# -*- coding: utf-8 -*-

from django.contrib import admin

# from nested_admin import (NestedModelAdmin, )
from base.admin import DataColumnInline

from .models import (SpamFilter, )


@admin.register(SpamFilter)
class SpamFilterAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', )
        }),
        ("Miscellanous", {
            'classes': ('collapse',),
            'fields': (
                ('engine_meta_iterations', 'engine_iterations'),
                ('counter', 'counter_threshold', 'threshold_actions'),
                ('engine_object_timestamp', ),
                'metadata',
            ),
        }),
        ("Labels", {
            'fields': (
                'labels_column',
            ),
        }),
        ("Classifier", {
            'fields': (
                'classifier',
            ),
        }),
        ("Bag of Words Transformation", {
            'fields': (
                ('bow_enconding', 'bow_decode_error', 'bow_strip_accents', ),
                ('bow_analyzer', 'bow_ngram_range_min',
                 'bow_ngram_range_max', ),
                ('bow_stop_words', 'bow_vocabulary', ),
                ('bow_max_df', 'bow_min_df', 'bow_max_features', ),
                'bow_binary',
            ),
        }),
    )

    inlines = [DataColumnInline, ]

    fieldsets_and_inlines_order = ('f', 'f', 'i', 'f', )

    def get_form(self, request, obj=None, **kwargs):
        # Save obj reference in the request for future processing in Inline
        request._obj_ = obj
        form = super(SpamFilterAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["metadata"].widget.attrs["disabled"] = "disabled"
        return(form)
