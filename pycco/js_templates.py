# -*- coding: utf-8 -*-
js = """\
// Provides basic UI utilities
var UIUtil = {
    
    // After opening an element, we hide it if the user another part of the app
    hideWhenUserClicksAway: function(selector, onClickAway) {
        $('body').bind('click', function(e) {
            // If the user clicks outside of the form, hide it.
            closestElements = $(e.target).closest(selector);
            elementsOfInterest = $(selector);
            
            // If the element clicked isn't part of what was clicked, hide the element
            if(closestElements.length == 0) {
                if(elementsOfInterest.is(':visible')) {
                    if(typeof(onClickAway) == 'function') onClickAway(selector, e);
                    else elementsOfInterest.hide();
                }
            }
        });
    }
}

var Docs = {
    init: function() {
        this.bindToUIActions();
    },

    bindToUIActions: function() {
        $('#pages-dropdown,#functions-dropdown').on('click', this.showDropdownMenu);

        UIUtil.hideWhenUserClicksAway('#pages-dropdown,#functions-dropdown', this.hideDropdownMenu);
    },

    showDropdownMenu: function() {
        Docs.hideDropdownMenu();
        $(this).closest('.dropdown').addClass('open');
    },

    hideDropdownMenu: function() {
        $('div.dropdown').removeClass("open");
    }

}

$(document).ready(function() {
    Docs.init();
});
"""

import os

jquery_file = open(os.path.dirname(os.path.abspath( __file__ )) + '/jquery.js')
js = jquery_file.read() + js
jquery_file.close()