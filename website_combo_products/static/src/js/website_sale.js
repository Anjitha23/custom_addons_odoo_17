/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.combineFilters = publicWidget.Widget.extend({
    selector: '.form-check-input',
    events: {
        'change': '_onChangeAttribute',
    },

    _onChangeAttribute: function (ev) {
        ev.preventDefault();
        console.log('_onChangeAttribute function called');

        // Update the URL with the selected combo_ids
        var url = new URL(window.location.href);
        url.searchParams.set('combo_product', ev.target.value);
        window.location.href = url;

        // Add an input type (hidden) to the form with the selected combo_products value
        var form = $(ev.currentTarget).closest("form");
        console.log('form',form)
        $('<input>').attr({
            type: 'hidden',  // Fix: use 'hidden' instead of 'visible'
            name: 'combo_product',
            value: ev.target.value,
        }).appendTo(form);

        // Submit the form
        form.submit();
    },
});
